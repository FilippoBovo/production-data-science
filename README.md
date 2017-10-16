# Production Data Science

<!--Why-->

Data scientists, like software developers, implement tools using computer code, but, unlike software developers, do not typically receive a proper training on good practices and effective tools to collaborate and build products.

<!--What-->

For this reason, this guide attempts to merge the gap that data scientists may have in software development practices. We will look at a data science workflow in Python that adapts ideas from software development that ease collaborations and keeps the coding environment close to production.

<!--How-->

At the core of this idea is an adaptation of the feature development and refactoring cycle typical of software development. In this cycle, new features are added to the code base and the code base is refactored to be simpler, more intuitive and, as a consequence, more stable. Instead of feature development, data science focuses on data exploration, and, with this analogy, the cycle loops through exploration and refactoring.

![exploration_refactoring_cycle](resources/explore-refactor_loop.png)

In the exploratory phase, the code base is expanded through data analysis, feature engineering and modelling, and, in the refactoring phase, the most useful results and tools from the exploratory phase are translated into modules and packages.

The nice thing about this approach is that we can use the tools and methods that software developers have used for a long time, such as Git and Unit Testing.

To show the workflow and how these tools are used, we will go through a tutorial in the form of a worked example based on the popular [Kaggle's Titanic data science challenge](https://www.kaggle.com/c/titanic), formed of three parts: *setup*, *explore* and *refactor*.

This tutorial assumes that you are familiar with Python 3, and relies on the assumption that you are skilled enough to use Google, StackExchange and other resources to fill some of the knowledge gaps that you may have. Another useful resource to get you started on new topics is [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/), which also includes references to more detailed material.

> Finally, quoted text is devoted to suggestions and observations.

Let's start the tutorial,

[**➠   Start the Tutorial**](tutorial/a-setup)

