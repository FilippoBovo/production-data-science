# A - Setup

In the first part of the tutorial, we set up the project, so that we start with an effective working environment.

> Note to Windows users: The commands in tutorial work on the Unix Bash command line. In order to get them to work on Windows, you may use [Cygwin](https://www.cygwin.com/).

## Virtual Environment

Python has a useful feature, called [virtual environment](https://docs.python.org/3/tutorial/venv.html), which allows to hold a collection of packages in an isolated Python enviroment. Because we want to keep the packages associated to this project separated from those associated to other projects, we create a virtual environment.  After making sure that Python 3 is installed in the system, we use [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) to initialise a virtual environment called `titanic`.

```shell
mkvirtualenv --python=python3 titanic
```

The environment should be activated by default after creation. However, if it is not active, you can do it with the command `workon titanic`. We can use the command `which python` to get the path of the Python executable to verify that we are in the correct environment.

## Project Structure

We start by creating a [minimal structure for a Python package](http://python-packaging.readthedocs.io/en/latest/minimal.html), which will be at the core of automation and productionisation.

```
titanic/
	titanic/
		__init__.py
	setup.py
	README.md
```

Names ending with `/` are folders and the others are text files, that you can create using the command `touch <file-path>`:

- The two folders called `titanic/` have to have the same name of the package.

- [`titanic/titanic/__init__.py`](titanic/titanic/__init__.py) is an empty file to [initialise](https://docs.python.org/3/tutorial/modules.html#packages) the titanic package.

- [`titanic/setup.py`](titanic/setup.py) is the [setup script](https://docs.python.org/3/distutils/setupscript.html) that is run when installing the module. You may want to change the `author` and `author_email` fields [in the file](titanic/setup.py) to match your details.

- The Markdown file [`titanic/README.md`](titanic/README.md) should contain a description of the package. [`titanic/titanic/`](titanic/titanic/) is the folder for storing package modules. The `readme()` function in [`titanic/setup.py`](titanic/setup.py) adds the content of [`titanic/README.md`](titanic/README.md) to the long description of the package in `setup()` and requires the package `pypandoc` to be installed.
  ```shell
  pip install pypandoc==1.4
  ```
  > Note that when installing packages with pip, we specify the package version in order to make sure that the we can run the code without issues. When you will create your own setup for different projects, it is better to use updated packages by omitting the version number.


Having created the above files, we can install the `titanic` package in [development mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs),

```shell
pip install -e titanic
```

The option `-e`, standing for `--editable`, installs the package in [development mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs). That is, it installs the `titanic` package [using a symlink](http://python-packaging.readthedocs.io/en/latest/minimal.html#creating-the-scaffolding) to the `titanic/` folder so that we can develop the package while it is installed.

In addition to the Python package structure just created for automation and productionisation, we need a folder that will contain exploratory analyses and a folder where to store data to be used _only for development_. For these, we create the folders `exploration/` and `data/` outside of the package, which should be left outside of the package, as the package should only contain elements aimed at production. For the data, we download `train.csv` from the [Titanic data science competition page](https://www.kaggle.com/c/titanic/data), rename it to  `titanic.csv` and store it in `data/`.

> Note that in this case the data, being small, is store directly in our project folder. If the data is big or is confidential, it should be stored in different places, for example in a secure cloud location.

Finally, we create a [readme file](README.md) for the project, containing the project description (not to be confused with the [`package readme file`](titanic/README.md). Because files called [`README.md`](README.md) are automatically displayed by GitHub as webpage descriptions, [`README.md`](README.md) has been used for the content that you are reading in this moment. Instead of this, you may start this file with,

```markdown
# Analysis of the Titanic dataset

This projects aims at analysing Kaggle's Titanic dataset and build a predictive model for the Titanic data science challenge.
```

and add information as the project progresses.

> It is good to create `README.md`  files in the [`data`](data),  [`exploration`](exploration) folders when something about the data and exploration should be told, like good practices and conventions. For example, it may be useful to store data in zip archives to save some space, and this should be written in  `README.md` so that other people will be consistent with the choice.

Putting all together, we get the following project structure.

```
titanic/
	titanic/
		__init__.py
	setup.py
	README.md
data/
	titanic.csv
exploration/
README.md
```

> Although for data science this is a general base structure for folders outside the module package, some projects may require different ones. To understand what is a suitable base structure for a project, it may be helpful to draw a diagram with a starting point, which for data science is typically data, and an end point, in the form of a goal.
>
> ```
>  ———————           ———————           —————— 
> | Input | ——————> | ? ? ? | ——————> | Goal | 
>  ———————           ———————           ——————
>
>  Titanic          Exploration       Predict
>  input                              Passenger
>  data                               Survival
> ```
>
> Asking question about the box in the middle may help clarify what is needed for the project. This does not mean trying to predict the details of the projects ahead of time, as this would lead to a strict template that prevents flexibility. Instead, this diagram should help understand what is necessary.

Now that the project structure has been set up, note that all the commands in this tutorial are run from the root folder of the project.

## Logging

Logging is an important task for software development that should handle the messages that help user understand what the code does. With the [Python logging module](https://docs.python.org/3/library/logging.html) we can handle messages in different ways using configuration files, without having to change the code.

> Note that it is a good practice to [replace the less flexible `print` function with log messages to the console](https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/). 

In our case, we have two different places where we want to display messages: the terminal when running command line applications and interactive editors, like the [Jupyter notebook](http://jupyter.org/) or [Spyder](https://pythonhosted.org/spyder/). In the terminal, it is useful to display the time, the Python module where the message comes from and the message level (debug, info, warning, ...). In interactive editors, most of the time it is enough to display just the message.

To handle these two different ways of displaying data, we create two configuration files,  [`titanic/titanic/logging.yml`](titanic/titanic/logging.yaml) for messages to the terminal and [`exploration/logging.yml`](exploration/logging.yaml) for messages in Jupyter notebooks. These configuration files use the [YAML format](https://en.wikipedia.org/wiki/YAML), as it is more popular and flexible than the [standard Python configuration files](https://docs.python.org/3/library/configparser.html). For this, we need to install the [PyYAML](https://github.com/yaml/pyyaml) package.

```python
pip install pyyaml==3.12
```

Because the Python logging module does not natively support logging configuration files in YAML format, we create the file [`titanic/titanic/log.py`](titanic/titanic/log.py) with the function `load_yaml_config()` to load them. We will see how to use this function in the [next section](../b-explore) of the tutorial.

> In this tutorial we limit ourselves to messages displayed on the screen as this project is simple. When a project becomes more complex, it is useful to [write log messages to files](https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/).

## Reproducibility

In order for other people to be able to reproduce the same environment that we are using, we create the file [`requirements.txt`](titanic/requirements.txt) containing the [list of packages in our virtual enviroment](https://pip.pypa.io/en/stable/reference/pip_freeze/).

```shell
pip freeze | grep -v titanic > requirements.txt
```

The `grep -v titanic` command omits the local package `titanic` to avoid errors when installing packages from the requirement file, as we will see in section [Collaboration](#collaboration).

We also add the packages we installed as [minimal package requirements](https://packaging.python.org/discussions/install-requires-vs-requirements/) to [`titanic/setup.py`](titanic/setup.py).

```python
...
setup(
	...
    install_requires=[
      	'pypandoc>=1.4',
        'pyyaml>=3.12',
    ]
)
```

We will explain how to use these additions to reproduce the same environment in section [Collaboration](#collaboration). Before that, we need to share our project.

## Git

To allow other people access to the work, we share it on [GitHub](https://github.com/), using the [Git](https://git-scm.com/) command line tools.

Because we want to add to this repository only the necessary files, we create a [list of files to omit](https://git-scm.com/docs/gitignore) by creating a [`.gitignore`](.gitignore) file. The files to omit, are, for example, files that are created in the project folder when we installed the `titanic` package. A list of such files for Python has already been compiled by other people, so that we can simply copy it in our project folder.

```shell
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore
```

Note that operating systems specific files should be [omitted at global level](https://help.github.com/articles/ignoring-files/#create-a-global-gitignore) using the content of one of these files, [Unix](https://github.com/github/gitignore/blob/master/Global/Linux.gitignore), [Mac](https://github.com/github/gitignore/blob/master/Global/macOS.gitignore), [Windows](https://github.com/github/gitignore/blob/master/Global/Windows.gitignore), matching your operating system.

Next, we follow the GitHub guide _[Adding an existing project to GitHub using the command line](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)_ to set up a new repository called `titanic` and push the content we created into it.

> It is important to learn Git well, otherwise it may be easy to mess up a repository. You may start with [this tutorial](https://try.github.io) and later take a proper course, as, for example, the free course [How to Use Version Control in Git & GitHub](https://www.udacity.com/course/how-to-use-git-and-github--ud775)

Finally, the project structure can be explored at the [top of the page](#) and is displayed in the following box.

```
.gitignore
titanic/
	titanic/
		__init__.py
		log.py
		logging.yaml
	setup.py
	README.md
data/
	titanic.csv
exploration/
	logging.yaml
README.md
```
## Collaboration

If other people would like to contribute to the project, they just need to get the repository and reproduce the working environment.

```shell
git clone <git-repository>
cd titanic
mkvirtualenv --python=python3 titanic
pip install -r requirements.txt
pip install -e titanic
```

Now that the project has been set up, we proceed to the next part of the tutorial where we will do some exploratory data analysis.

[**➠   Go to the next part: *B - Explore***](../b-explore)

