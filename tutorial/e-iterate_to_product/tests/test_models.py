from titanic import models, data
import pandas as pd
import os
from sklearn.metrics import accuracy_score

validation_data = os.path.join(os.path.dirname(__file__), "validation_data/titanic.csv")


# NOTE: In this test we used a data pipeline to go from the validation data to the
# train and test set arrays. For more information about the *data pipeline*, see
# "Part D: Iterate to Product" of this tutorial.
def test_run_logistic_regression():
    processed_data = (
        pd.read_csv(validation_data, usecols=['Name', 'Sex', 'Age', 'Survived'])
        .pipe(lambda df: df.fillna({'Age': df.Age.median(), }))
        .pipe(lambda df: df.astype({'Age': 'float64',
                                    'Name': 'object',
                                    'Sex': 'category',
                                    'Survived': 'int64'}))
        .pipe(data.extract_title)
    )

    X_train, X_test, y_train, y_test = models.data_preparation(processed_data,
                                                               test_size=0.2,
                                                               random_state=0)

    majority_vote = models.run_majority_vote(X_train, X_test, y_train, y_test)
    linear_regression = models.run_logistic_regression(X_train, X_test, y_train, y_test)

    accuracy_majority_vote = accuracy_score(y_true=y_test, y_pred=majority_vote.predict(X_test))
    accuracy_linear_regression = accuracy_score(y_true=y_test, y_pred=linear_regression.predict(X_test))

    assert accuracy_linear_regression > accuracy_majority_vote
