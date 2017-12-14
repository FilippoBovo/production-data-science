## {{cookiecutter.project_name}}

*[ TODO Add project description]*

## How to Run

First, make sure that you have [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) installed and install the project.

```shell
mkvirtualenv {{cookiecutter.package_name}}
pip install {{cookiecutter.project_url}}
```

Then, look at the instructions that follow and those in [README.md]({{cookiecutter.package_version}}/README.md).

*[ TODO Add instructions ... ]*

## How to Contribute

First, make sure that you have [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) installed and install the project in development mode.

```shell
mkvirtualenv {{cookiecutter.package_name}}
git clone {{cookiecutter.project_url}}
pip install -r requirements.txt
pip install -e {{cookiecutter.package_name}}
pip freeze | grep -v {{cookiecutter.package_name}} > requirements.txt
```

Then, check the [README.md]({{cookiecutter.package_version}}/README.md), and create or select a GitHub branch and have fun... :smiley: