from typing import List
from InquirerPy import prompt
from InquirerPy.separator import Separator
from shutil import copy, copytree
import os, errno, subprocess
from jinja2 import Template

scaffold_path = "app/"


def resource_path(path: str) -> str:
    """
    return the absolute path for a file
    """
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), path)


def extras_includes(extra: str) -> bool:
    """
    check if extra is included in extras selected by user
    """
    return any(extra in s.lower() for s in extras)


def render_and_copy(src: str, dest: str) -> None:
    """
    read in src as a jinja template and save the rendered output to dest
    """
    with open(resource_path(src)) as f:
        template = Template(f.read())
        template.globals["extras_includes"] = extras_includes
    parsed = template.render(name=name, extras=extras)
    if not os.path.exists(os.path.dirname(dest)):
        try:
            os.makedirs(os.path.dirname(dest))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(dest, "w") as f:
        f.write(parsed)


def render_and_copy_files(list_of_files: List[str]) -> None:
    """
    run render_and_copy for a list of files
    """
    for file in list_of_files:
        render_and_copy(scaffold_path + file, name + "/" + file)


def prompt_user() -> None:
    """
    prompt user for selections, copy files, and run make install
    """
    questions = [
        {"type": "input", "name": "project_name", "message": "Name your project:"},
        {
            "type": "checkbox",
            "message": "What else do you want to generate?",
            "name": "extras",
            "choices": [
                "Test Suite(tox, pytest)",
                "Docker",
                "Heroku",
                "Job Scheduler",
                Separator("Flask Libraries"),
                "Flask-Login",
                "Flask-Admin",
                "Flask-WTF",
                Separator("JS Libraries"),
                "Vue.js(CDN Version)",
                "jQuery",
                Separator("CSS"),
                "Sass",
                "Bootstrap",
                Separator("Database"),
                "SQLite(Flask-SQLAlchemy)",
                "MongoDB(Flask-PyMongo)",
            ],
        },
    ]

    answers = prompt(questions)
    global name
    name = answers["project_name"]
    global extras
    extras = answers["extras"]
    if "SQLite(Flask-SQLAlchemy)" in extras and "MongoDB(Flask-PyMongo)" in extras:
        print("You can only choose one database type!")
        exit()

    print("Here are your selections:")
    print("Project name:", name)
    for extra in extras:
        print("-", extra)

    confirm_q = [
        {
            "type": "confirm",
            "message": "Is this what you want?",
            "name": "continue",
            "default": False,
        }
    ]
    confirm = prompt(confirm_q)
    if not confirm["continue"]:
        print("Ok. Bye.")
        exit()

    print("Copying files...")
    os.makedirs(name, exist_ok=True)

    base_folders = ["static/css", "static/js", "templates"]
    base_files = [
        "app.py",
        "config.py",
        "Makefile",
        "README.md",
        "requirements.txt",
        "setup.py",
        ".gitignore",
    ]

    # render and copy flask static and template dirs
    for folder in base_folders:
        copytree(
            resource_path(scaffold_path + folder),
            name + "/" + folder,
            dirs_exist_ok=True,
            copy_function=render_and_copy,
        )

    # render and copy root files: app.py, README, Makefile, etc
    render_and_copy_files(base_files)

    test_suite_files = ["tests/client.py", "tests/test_app.py", "tox.ini"]
    if extras_includes("test"):
        render_and_copy_files(test_suite_files)

    docker_files = [".dockerignore", "docker-compose.yml", "Dockerfile"]
    if extras_includes("docker"):
        render_and_copy_files(docker_files)

    heroku_files = ["Procfile", "runtime.txt"]
    if extras_includes("heroku"):
        render_and_copy_files(heroku_files)

    if extras_includes("sass"):
        copytree(
            resource_path(scaffold_path + "static/scss"),
            name + "/static/scss",
            dirs_exist_ok=True,
            copy_function=render_and_copy,
        )

    sqlite_files = ["models.py"]
    if extras_includes("sqlite"):
        render_and_copy_files(sqlite_files)

    print("Running make install...")
    subprocess.check_output(["make", "install"], cwd=name)

    print("Successfully created %s!" % (name,))
    print("To get started, do:")
    print("\t1) cd", name)
    print("\t2) make start")


if __name__ == "__main__":
    prompt_user()
