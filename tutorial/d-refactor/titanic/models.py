import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def data_preparation(df, test_size, random_state=None):
    """Permute and split DataFrame index into train and test.

    Parameters
    ----------
    df: pandas.DataFrame
    test_size: float
        Fraction between 0.0 and 1.0
    random_state: int

    Returns
    -------
    tuple of numpy.ndarray,
        X_train, X_test, y_train, y_test
    """

    logging.info("Splitting the data-frame into train and test parts")

    df = df[['Age', 'Sex', 'Title', 'Survived']]

    df = pd.get_dummies(df, columns=['Sex', 'Title'])

    X_train, X_test, y_train, y_test = train_test_split(
        df.drop('Survived', axis=1).values,
        df['Survived'].values,
        test_size=test_size,
        random_state=random_state
    )

    return X_train, X_test, y_train, y_test


class MajorityVoteClassifier:
    """Majority Vote Classifier

    This class contains the `fit` and `predict` methods that are compatible
    with the SciKit-Learn model classes.
    """
    def __init__(self):
        self.majority_vote = None

    def fit(self, X, y):
        self.majority_vote = round(y.mean())
        return self

    def predict(self, X):
        if self.majority_vote is None:
            raise ValueError("The majority vote classifier has to be trained before making predictions")
        return [self.majority_vote] * len(X)


def run_majority_vote(X_train, X_test, y_train, y_test):
    """Use the majority vote to predict survival.

    Parameters
    ----------
    X_train: numpy.ndarray
    X_test: numpy.ndarray
    y_train: numpy.ndarray
    y_test: numpy.ndarray

    """

    logging.info("Running the majority vote classifier")

    majority_vote_classifier = MajorityVoteClassifier()
    majority_vote_classifier.fit(X_train, y_train)
    y_test_predictions = majority_vote_classifier.predict(X_test)

    accuracy = accuracy_score(y_true=y_test, y_pred=y_test_predictions)

    logging.info('The prediction accuracy with the majority vote classifier is {:.1f}%'.format(accuracy * 100))

    return majority_vote_classifier


def run_logistic_regression(X_train, X_test, y_train, y_test):
    """Use ridge logistic regression to predict survival.

    The ridge parameter is found using 10-fold cross-validation.

    Parameters
    ----------
    X_train: numpy.ndarray
    X_test: numpy.ndarray
    y_train: numpy.ndarray
    y_test: numpy.ndarray

    """

    logging.info("Running the ridge logistic regression classifier")

    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import GridSearchCV

    lr = LogisticRegression(random_state=0, solver='lbfgs')

    param_range = [2 ** x for x in range(-10, 10)]

    gs = GridSearchCV(
        estimator=lr,
        param_grid={'C': param_range},
        scoring='accuracy',
        cv=10,
        n_jobs=-1
    )

    gs.fit(X_train, y_train)

    accuracy = accuracy_score(y_true=y_test, y_pred=gs.predict(X_test))

    logging.info('The prediction accuracy with the ridge logistic regression classifier is {:.1f}%'.format(accuracy * 100))

    return gs
