# B - Explore

In the second part of this tutorial, we explore the Titanic data and build a model to predict if a passenger will survive.

[TOC]

![explore](/Users/fil/Satalia/production_data_science/production_data_science/resources/explore.png)

## Branching

In software development, [branching](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) is used to isolate the development of new features. Branching can be easily extended to data science, where instead of developing new features, we explore data.

We start by creating a new branch called `explore_survival`.

```shell
git checkout -b explore_survival
```

It is useful to name the branch by starting with `explore_` when the branch is used for exploration.

> It is important to use explicit names for branching, so that other people can easily understand the purpose of the branch.

## Tools

There are [several tool for exploratory data analysis in Python](https://www.datacamp.com/community/tutorials/data-science-python-ide). Some of the most widely used are,

- [Jupyter Notebook](http://jupyter.org/)
- [Spyder](https://github.com/spyder-ide/spyder) or other IDE specific for data science
- Normal text editors

Even though choosing a single tool for exploratory data analysis across different people would make things tidier, it is better to explore by using your favourite tools. The important thing is to insure that the exploratory work is reproducible and clearly explained to make life easier to other people.

> **In collaborative work, make life easier to other people by following good coding practices and by explaining concepts, intentions and assumptions clearly.**
>
> In particular, it is strongly suggested to read these [PEP](https://www.python.org/dev/peps/) (Python Enhancement Proposals) guides:
>
> - [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
> - [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Exploratory Data Analysis

In this tutorial, as exploratory tool we choose the Jupyter Notebook as it is a self-contained document and it can be displayed on GitHub.

```shell
pip install jupyter
python -m ipykernel install --user --name=titanic
```

We also need some other data science packages.

```shell
pip install watermark==1.5.0 pandas==0.20.3 scikit-learn==0.19.0 scipy==0.19.1 matplotlib==2.1.0
pip freeze | grep -v titanic > titanic/requirements.txt
```

Now we are ready to move to the notebook.

[**➠   Go to the analysis in the Jupyter Notebook**](exploration/cleaning_engineering_logistic_regression.ipynb)

Finally, we commit our changes to the branch and, since we concluded the work on this branch, we merge it with the master branch.

```shell
git commit . -m "predict passenger survival using ridge logistic regression"
git checkout master 
git merge explore_survival
git push
```

> Note that merging should be done with care, as, for example, [rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) may be a better choice.

> Generally, branch names should state the purpose of the branch as they look at the future, while commit messages should state what has been done, as they look at the past.
>
> Moreover, it is effective to follow writing style practices and start both branch and commit messages with _[action verbs](https://books.google.co.uk/books?id=Fp4-7EWkvUgC&lpg=PP1&dq=joshua%20schimel%20writing%20science&pg=PP1#v=onepage&q=joshua%20schimel%20writing%20science&f=false) in [active voice](https://en.wikipedia.org/wiki/The_Elements_of_Style#Content) and [present tense](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project)_, as they are much more direct that nouns.

## Organisation of the Exploration Folder

The exploratory folder is the place where to store exploratory projects.

To make it easy for other people and your future-self to navigate the exploratory projects we suggest the following rules.

- ***Single Result*** — Each exploratory project should prove a single result.
- ***Dedicated Folder*** — Each exploratory project should be placed in a dedicated folder. If the project involves a single document, like a Jupyter Notebook, no folder is needed.
- ***Meaningful Name*** — Giving the exploratory project a name that shows what is done inside, like `cleaning_engineering_logistic_regression` for the notebook just seen. In this case, in the file name we stated the content, but, depending on the *main message of the notebook*, the name can state the (single) intention or result of the notebook.
- ***Exploration = Document*** — Treat the exploratory project as a document to explain the logic of the analysis. In a Jupyter Notebook this can be done using the Markdown feature. With other tools, it may be useful to write explanation in code comments and in the `README.md`, which will also be displayed automatically by GitHub.
- ***Author Contact*** — Write the author name(s), GitHub account and, if necessary, email(s). This ensures that if the content of the notebook is not clear, it is easy to reach someone who can clarify.
- ***Achievement*** — State the (single) achievement at the beginning of the notebook. This allows people to know the result, without having to go through the whole notebook.
- ***Introduction*** — Guide the reader with an introduction to the notebook, like the introduction to a chapter of a book. If you can, write the introduction in the form of a story.
- ***Clear Code*** — Making sure that the code is clear by following good coding practices. Exploratory work is not an excuse for bad code. As long as it is work that has to be shared with other people or to be reviewed in the future, make it easy for the reader.

As an example, if this project were to expand the structure of the folder `exploration` may look like this:

```
exploration/
	cleaning_engineering_logistic_regression.ipynb        # Jupyter Notebook
	feature_selection/                                    # Spider (IDE)
		.spyproject/
			<spyder_stuff>
		analysis.py
	logistic_regression_vs_svm/                           # Normal text editor
		analysis.py
		plots/
		README.md
```

In this part of the tutorial we saw a simple data analysis using the Jupyter Notebook and suggested some rules to ease collaborations and develop clear exploratory analyses. In the next part of the tutorial we will refactor the analysis of this part into the [Titanic package](titanic) that we prepared in the [previous section](../a-setup).

[**➠   Go to the next part: *C - Refactor***](../c-refactor)

