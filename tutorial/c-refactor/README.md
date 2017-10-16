# C - Refactor

In the third part of this worked example, we refactor the code of the exploration in the Jupyter Notebook into the Titanic package that we prepared in [part A - Setup](../a-setup).

[TOC]

![refactor](/Users/fil/Satalia/production_data_science/production_data_science/resources/refactor.png)

## Refactoring for Exploration

The code in the Jupyter Notebook that we saw in the previous part of this tutorial is written as a script. The idea of refactoring for exploration is to **restructure code _and_ text so that analyses are easier to understand and further exploration becomes faster to do**. For this, it is useful to introduce the concept of _code to text ratio_,
$$
\frac{\text{code}}{\text{text}}
$$
Because the main purpose of an exploratory analysis is to prove a point rather than showing code, refactoring for exploration should aim at _reducing the code to text ratio, within reason_. In this way, a notebook would look more like a document that uses words (and plots) to reason and prove a point.

However, with this criterion, we may as well increase the number of words, just to decrease the code to text ratio. This leads to longer documents that are both text and code heavy and, in turn, harder to read. A better solution is to **simplify both code and text, while keeping the code to word ratio reasonably low**.

It is important to understand that this is just a _qualitative criterion_ which should act more as a principle rather than a rule. This is why the words "within reason" and "reasonably" were specified in the italic sentences above. For example, if an analysis just needs few words to prove a point, it does not make sense to forcefully simplify the code to obtain a better code to word ratio. In other words, _rather than blindly following rules, understand the principles and the motivations behind them, and do what makes most sense_.[^1]

Note that if an analysis does not lead to any useful result or did not develop useful tools, _it may as well be useless to refactor it_.

Following the principle above, a possible workflow for refactoring notebooks is the following.

1. At first, we can move repeated scripts into functions that are called multiple times, reducing the amount of code in the notebook and, therefore, improving readability.
2. Functions that become widely used in the analysis, can be moved into [Python modules](https://docs.python.org/3/tutorial/modules.html) located in the same directory of the exploratory analysis. This further reduces the code in the notebook and allows the functions to be called from other notebooks or scripts in the same folder of the analysis.
3. Functions that become particularly important, can be made more solid by writing unit tests, as explained in the section below.
4. Functions that are particularly useful can be moved into a Python package in the [`exploration`](exploration) folder, that is, outside the folder of a particular analysis, so that they can be used for different analyses.

The same workflow is easily adapted to IDEs and text editors.

## Refactoring for Production

Once an exploratory analysis has taken a certain direction, it is useful to refactor the parts of the code that are going into production, as, for example, the functions and methods that will form data pipelines.

Because refactoring data science for production is closer to software development than refactoring for exploration, we can rely more on unit testing methodologies. Moreover, data science broadly involve data preprocessing and predictive modelling, for which testing can be done differently.

In data processing, the general idea to [write tests](https://pandas.pydata.org/pandas-docs/stable/contributing.html#test-driven-development-code-writing) is to,

1. Create an input dataset with peculiar cases
2. Create the output dataset that we expect from processing the input dataset
3. Compare the processed input dataset and expected output dataset


In predictive modelling, the situation is similar if we take the model predictions as output and we fix the random seed if random processes are involved. However, if we would like to improve the model along the way, we must allow the output to change, meaning that, instead of testing the exact output, we *test properties* of the output. For this purpose, there are some testing tools for Python:

- [Hypothesis](https://hypothesis.readthedocs.io) — A package for creating unit tests which are simpler to write and more powerful when run, finding edge cases in your code you wouldn’t have thought to look for
- [Engarde](http://engarde.readthedocs.io/) — A package for defensive data analysis
- [Faker](https://faker.readthedocs.io) — A package to generate fake data
- [Feature Forge](https://feature-forge.readthedocs.io) — A package that provides some help with the boilerplate of defining features and help you testing them

## Refactoring the Notebook

In this section, we refactor some of the [notebook](exploration/cleaning_engineering_logistic_regression.ipynb) code into the [`titanic`](titanic) package for production. We do this by creating the modules [`titanic/titanic/data.py`](titanic/titanic/data.py) and [`titanic/titanic/models.py`](titanic/titanic/models.py) where we put respectively functions for data processing and predictive modelling.

We will also use the [NumPy docstring format](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt), as it is more readable that the standard [Python reStructuredText format](https://www.python.org/dev/peps/pep-0287/).

> When refactoring, keep in mind that [**code is read much more often than it is written**](https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds).
>
> In particular, these three actions help a lot:
>
> - Use explicit variable names
> - Write docstrings
> - Comment your code
> - Commenting too much may mean that you should improve your code instead

First, we create a new branch called `refactor_explore_survival`.

```shell
git checkout -b refactor_explore_survival
```

Then, click on the following links to see the refactoring.

- [**➠   Refactored Jupyter Notebook**](exploration/cleaning_engineering_logistic_regression.ipynb) (See sections _Feature Engineering_ and _Predictions_)
- [**➠   Data manipulation module: *data.py***](titanic/titanic/data.py)
- [**➠   Predictive models module: *models.py***](titanic/titanic/models.py)

## Unit Tests

For these functions, we also create unit tests in [`titanic/titanic/tests/`](titanic/titanic/tests/) by using [PyTest](https://docs.pytest.org), as this library is more user-friendly than the standard [unittest](https://docs.python.org/3/library/unittest.html) library.

```shell
mkdir titanic/titanic/tests/
pip install pytest==3.2.3 pytest-runner==2.12.1
```

Add the following content to [`titanic/setup.py`](titanic/setup.py):

```python
...
setup(
	...
    install_requires=[
		...
        'pytest>=3.2.3',
        'pytest-runner>=2.12.1',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
```

To tell Python to use PyTest for testing, create the configuration file [`titanic/setup.cfg`](titanic/setup.cfg) with the following content.

```ini
[aliases]
test=pytest
```

The tests for the functions in the [data.py](titanic/titanic/data.py) and [models.py](titanic/titanic/models.py) modules are in the following files:

- [**➠   Tests for the data manipulation module: *test_data.py***](titanic/titanic/tests/test_data.py)
- [**➠   Tests for the predictive modelling module: *test_models.py***](titanic/titanic/tests/test_models.py)

Finally, you can run the tests.

```shell
python -m pytest
```

## Data Pipeline

If we are happy with our data processing and predictive model, we can implement the work into a pipeline in the [Titanic package](titanic).

[**➠   Go to the data pipeline module: *pipelines.py***](titanic/titanic/pipelines.py)

Moreover, it is useful to implement a command line tool to run the pipeline. For this, we use the [Click](http://click.pocoo.org/) library instead of the standard [argparse](https://docs.python.org/3/library/argparse.html), as it is more [user-friendly](http://click.pocoo.org/5/why/).

```shell
pip install click==6.7
```

We also add the following lines to [titanic/setup.py](titanic/setup.py).

```python
...
setup(
    ...
    install_requires=[
        ...
        'click>=6.7'
    ],
	...
    entry_points='''
        [console_scripts]
        titanic_analysis=titanic.command_line:titanic_analysis
    '''
)
```

The command line tool is implemented in the following file.

[**➠   Go to the command line module: *command_line.py***](titanic/titanic/command_line.py)

We can run the pipeline from the command line.

```shell
titanic_analysis --filename data/titanic.csv
```

Finally, we commit the changes and push the content to the GitHub repository.

```shell
git commit . -m "refactor exploratory analysis of passenger survival predictions using ridge logistic regression"
git checkout master 
git merge refactor_explore_survival
git push
```

In this part of the tutorial we saw how to refactor for exploration and production, and refactored for production the notebook into the [Titanic package](titanic).

For your next project, you can now use the Cookiecutter template based on this tutorial.

[**➠   Go to the Project Template**](../../template)

[^1]: A similar concept is stated in the Python PEP 8 document: [A Foolish Consistency is the Hobgoblin of Little Minds](https://www.python.org/dev/peps/pep-0008/#id15).