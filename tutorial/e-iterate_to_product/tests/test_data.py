from titanic import data
import pandas as pd
from pandas.util.testing import assert_frame_equal


def test_extract_title():

    df = pd.DataFrame.from_dict(
        {
            'Capt': 'Crosby, Capt. Edward Gifford',
            'Col': 'Simonius-Blumer, Col. Oberst Alfons',
            'Don': 'Uruchurtu, Don. Manuel E',
            'Dr': 'Minahan, Dr. William Edward',
            'Jonkheer': 'Reuchlin, Jonkheer. John George',
            'Lady': 'Duff Gordon, Lady. (Lucille Christiana Sutherland) ("Mrs Morgan")',
            'Major': 'Peuchen, Major. Arthur Godfrey',
            'Master': 'Palsson, Master. Gosta Leonard',
            'Miss': 'Heikkinen, Miss. Laina',
            'Mlle': 'Sagesser, Mlle. Emma',
            'Mme': 'Aubart, Mme. Leontine Pauline',
            'Mr': 'Braund, Mr. Owen Harris',
            'Mrs': 'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
            'Ms': 'Reynaldo, Ms. Encarnacion',
            'Rev': 'Byles, Rev. Thomas Roussel Davids',
            'Sir': 'Duff Gordon, Sir. Cosmo Edmund ("Mr Morgan")',
            'the Countess': 'Rothes, the Countess. of (Lucy Noel Martha Dyer-Edwards)'
        },
        orient='index',
    ).rename(columns={0: 'Name'})

    result = data.extract_title(df)

    expected = pd.DataFrame.from_dict(
        {'Name': {'Capt': 'Crosby, Capt. Edward Gifford',
                  'Col': 'Simonius-Blumer, Col. Oberst Alfons',
                  'Don': 'Uruchurtu, Don. Manuel E',
                  'Dr': 'Minahan, Dr. William Edward',
                  'Jonkheer': 'Reuchlin, Jonkheer. John George',
                  'Lady': 'Duff Gordon, Lady. (Lucille Christiana Sutherland) ("Mrs Morgan")',
                  'Major': 'Peuchen, Major. Arthur Godfrey',
                  'Master': 'Palsson, Master. Gosta Leonard',
                  'Miss': 'Heikkinen, Miss. Laina',
                  'Mlle': 'Sagesser, Mlle. Emma',
                  'Mme': 'Aubart, Mme. Leontine Pauline',
                  'Mr': 'Braund, Mr. Owen Harris',
                  'Mrs': 'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
                  'Ms': 'Reynaldo, Ms. Encarnacion',
                  'Rev': 'Byles, Rev. Thomas Roussel Davids',
                  'Sir': 'Duff Gordon, Sir. Cosmo Edmund ("Mr Morgan")',
                  'the Countess': 'Rothes, the Countess. of (Lucy Noel Martha Dyer-Edwards)'},
         'Title': {'Capt': 'Officer',
                   'Col': 'Officer',
                   'Don': 'Royalty',
                   'Dr': 'Officer',
                   'Jonkheer': 'Royalty',
                   'Lady': 'Royalty',
                   'Major': 'Officer',
                   'Master': 'Master',
                   'Miss': 'Miss',
                   'Mlle': 'Miss',
                   'Mme': 'Mrs',
                   'Mr': 'Mr',
                   'Mrs': 'Mrs',
                   'Ms': 'Mrs',
                   'Rev': 'Officer',
                   'Sir': 'Royalty',
                   'the Countess': 'Royalty'}}
    )
    expected['Title'] = expected['Title'].astype('category')

    assert_frame_equal(result, expected)
