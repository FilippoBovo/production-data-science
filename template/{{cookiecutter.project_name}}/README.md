## {{cookiecutter.project_name}}

*[ TODO Add project description]*

## How to Run

First, make sure that you have [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) installed and install the project.

```shell
mkvirtualenv {{cookiecutter.project_name}}
pip install -e 'git+{{cookiecutter.project_url}}.git#egg={{cookiecutter.package_name}}'
```

> For a private repository accessible only through an SSH authentication, substitute `git+https://github.com` with `git+ssh://git@github.com`.

*[ TODO Add instructions to run package scritps ]*

## How to Contribute

First, make sure that you have [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) installed and install the project in development mode.

```shell
mkvirtualenv {{cookiecutter.project_name}}
git clone {{cookiecutter.project_url}}.git
cd {{cookiecutter.project_name}}
pip install -r requirements.txt
pip install -e .
pip freeze | grep -v {{cookiecutter.package_name}} > requirements.txt
```

> For a private repository accessible only through an SSH authentication, substitute `https://github.com/` with `git@github.com:`.

Then, create or select a GitHub branch and have fun... 