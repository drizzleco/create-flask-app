from PyInquirer import prompt, Separator


questions = [
    {"type": "input", "name": "project_name", "message": "Name your project:"},
    {
        "type": "checkbox",
        "message": "What else do you want to generate?",
        "name": "extras",
        "choices": [
            {"name": "Test Suite(tox, pytest)"},
            {"name": "Docker"},
            {"name": "Heroku"},
            {"name": "Job Scheduler"},
            Separator("Flask Libraries"),
            {"name": "Flask-Login"},
            {"name": "Flask-Admin"},
            {"name": "Flask-WTF"},
            Separator("JS Libraries"),
            {"name": "Vue.js(CDN Version)"},
            {"name": "jQuery"},
            Separator("CSS"),
            {"name": "Sass"},
            {"name": "Bootstrap"},
            Separator("Database"),
            {"name": "SQLite(Flask-SQLAlchemy)"},
            {"name": "MongoDB(Flask-PyMongo)"},
        ],
    },
]

answers = prompt(questions)
name = answers["project_name"]
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

# generate the files and copy them here

# run make install

print("Successfully created %s!" % (name,))
print('To get started, do:')
print('\t1) cd', name)
print('\t2) make start')
