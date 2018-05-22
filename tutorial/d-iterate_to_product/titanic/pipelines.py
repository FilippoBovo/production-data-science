import logging
import pandas as pd
from titanic import data, models


def run_titanic_analysis(filename):
    """Data pipeline and predictions.

    Parameters
    ----------
    filename: str
        Path to the Titanic CSV input data
    """

    logging.info('Starting the data analysis pipeline')

    processed_data = (
        pd.read_csv(filename, usecols=['Name', 'Sex', 'Age', 'Survived'])
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

    models.run_majority_vote(X_train, X_test, y_train, y_test)
    models.run_logistic_regression(X_train, X_test, y_train, y_test)

    logging.info('The data analysis pipeline has terminated')

    return
