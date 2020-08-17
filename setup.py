import setuptools

setuptools.setup(
    name="create-flask-app",
    version="1.0",
    packages=setuptools.find_packages(),
    install_requires=['PyInquirer', 'jinja2'],
    entry_points={
        'console_scripts': [
            'create-flask-app=create_flask_app:prompt_user',
        ],
    },
    include_package_data=True,
    )
