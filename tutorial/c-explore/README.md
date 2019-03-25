# C - Explore

![explore](../../resources/explore.png)

In the third part of this tutorial, we explore the Titanic data and build a model to predict if a passenger will survive.

> Before starting the tutorial, remember to re-activate the Python virtual environment, if it is not already active.
> ```shell
> workon titanic_datascience
> ```

## Tools

There are [several softwares for exploratory data analysis in Python](https://www.datacamp.com/community/tutorials/data-science-python-ide). Some of the most widely used are,

- [Jupyter Notebook](http://jupyter.org/)
- [Spyder](https://github.com/spyder-ide/spyder) or other IDEs specific to data science
- Normal text editors

Even though choosing a single software for exploratory data analysis across different people would be more consistent, it may be better to explore by using your favourite one, so that you can be more effective in your analyses. The important thing is to make sure that the exploratory work is reproducible and clearly explained to make life easier to other people.

> **In collaborative work, make life easier to other people by following good coding practices and by explaining concepts, intentions and assumptions clearly.**
>
> In particular, it is strongly suggested to read these [PEP](https://www.python.org/dev/peps/) (Python Enhancement Proposals) guides:
>
> - [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
> - [Style Guide for Python Code, commonly known as PEP 8](https://www.python.org/dev/peps/pep-0008/)
>
> Moreover, have a look at [The Best of the Best Practices (BOBP) Guide for Python](https://gist.github.com/sloria/7001839).

For the purpose of this tutorial, as exploratory tool, we choose the Jupyter Notebook as it is a self-contained document that can be displayed on GitHub.

## Exploratory Data Analysis

We start our analysis by creating a new branch called `explore_passenger_survival`, as discussed in the [previous section](../b-collaborate).

```shell
git checkout -b explore_passenger_survival
```

> It is important to use explicit names for branching, so that other people can easily understand the purpose of each branch.

Next, we install Jupyter.

```shell
pip install jupyter
python -m ipykernel install --user --name=titanic_datascience  # Install the Jupyter kernel
```

We also need some other data science packages.

```shell
pip install watermark==1.8.1 pandas==0.24.2 scikit-learn==0.20.3 scipy==1.2.1 matplotlib==3.0.3
pip freeze | grep -v titanic > requirements.txt
```

Now, click on the following link to go to the notebook.

[**➠   Go to the analysis in the Jupyter Notebook**](exploration/predict_survival_using_logistic_regression_with_sex_age_title/analysis.ipynb)

After the analysis in the notebook is completed, we commit our changes to the `explore_passenger_survival` branch, merge the branch to the master branch and push to GitHub.

```shell
git add .
git commit -m "Predict passenger survival using ridge logistic regression"
git checkout master
git merge explore_passenger_survival
git push
```

## Organisation of the Exploration Folder

The exploratory folder is the place where to store exploratory analyses.

To make it easy for other people and your future-self to navigate exploratory analyses we suggest the following rules:

- **Single Result** — Each exploratory project should prove a single result.
- **Dedicated Folder** — Each exploratory project should be placed in a dedicated folder. Even if you start with a single file, use a dedicated folder as more files are likely to be created later on. Moreover, in this way the structure of the exploratory folder is consistent.
- **Meaningful Name** — Give the exploratory project a name that shows what is done inside, like `predict_passenger_survival` for the one just seen.
- **Exploration = Document** — Treat the exploratory project as a document to explain the logic of the analysis. In a Jupyter Notebook this can be done using the Markdown feature. With tools other than Jupyter, it may be useful to write the explanation in code comments and in a `README.md` file, which will also be displayed automatically by GitHub.
- **Author Contact** — Write the author name(s), GitHub account(s) and, if necessary, email(s). This ensures that if the content of a notebook is not clear, it is easy to reach someone who can clarify.
- **Achievement** — State the (single) achievement at the beginning of the notebook or readme file. This allows people to know the result, without having to go through the whole notebook.
- **Introduction** — Guide the reader with an introduction to the notebook, like the introduction to a chapter of a book. If you can, write the introduction in the form of a story.
- **Clear Code** — Making sure that the code is clear by following good coding practices. Exploratory work is not an excuse for bad code. As long as it is work that has to be shared with other people or to be reviewed in the future, make it easy for the reader.

As an example, if this project were to expand, the structure of the folder `exploration` may look like this:

```
📁 exploration/
    📁 predict_survival_using_logistic_regression_with_sex_age_title/    # Jupyter Notebook
        📄 analysis.ipynb
    📁 relation_between_age_and_survival/                                # Spyder (IDE)
        📁 .spyproject/
            📄 <spyder_stuff>
        📄 analysis.py
        📄 README.md
    📁 logistic_regression_vs_svm/                                       # Normal text editor
        📄 analysis.py
        📁 plots/
        📄 README.md
```

In this part of the tutorial we saw a simple data analysis using the Jupyter Notebook and suggested some rules to ease collaborations and develop clear exploratory analyses. In the next part of the tutorial, we will refactor the analysis of this part into the [Titanic package](titanic).

[**➠   Go to the next part: *D - Refactor***](../d-refactor)
