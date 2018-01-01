# Template

We can use [Cookiecutter](http://cookiecutter.readthedocs.io/en/latest/readme.html), to initialise a project using a template with the same structure seen in the tutorial.

We start by [creating a repository on GitHub](https://help.github.com/articles/creating-a-new-repository/) *without* initialising a readme file. In the following, *\<project_name\>* refers to the GitHub repository name.

Install Coockiecutter if you do not have it already.

```shell
pip install cookiecutter
```

Clone this repository to the system temporary folder, `$TMPDIR`.

```shell
git clone git@github.com:Satalia/production-data-science.git $TMPDIR/production_data_science_template
```

Go to the folder where you would like to store the project and create the project template.

```shell
cd <folder_to_store_project>
cookiecutter $TMPDIR/production_data_science_template/template
```

You will be prompted with values to fill, like the project name (use *\<project_name\>*), the package name and the author name.

Create a virtual environment and install the package.

```shell
cd <project_name>
mkvirtualenv <package_name>
pip install -e <package_name>
pip freeze | grep -v <package_name> > requirements.txt
git init
git add .
git commit -m "First commit"
git remote add origin <remote_repository_url>
git push -u origin master
```

Here, *\<package_name\>* is the name of the Python package to be used to productionise the exploratory work, and should match the respective value you imputed in Cookiecutter.

Moreover, if you are planning to use the Jupyter Notebook, you have to install the kernel of the environment.

```shell
python -m ipykernel install --user --name <package_name>
```

Now, create a branch, switch to it,

```shell
git checkout -b <branch_name>
```

and you are ready! 🎉