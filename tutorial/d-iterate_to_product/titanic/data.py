import logging


def extract_title(df):
    """Extract the title from the passenger names.

    Parameters
    ----------
    df : pandas.DataFrame
        Data-frame containing the column `Name`

    Returns
    -------
    pandas.DataFrame
        Data-frame with additional column with titles
    """

    logging.info("Extracting the titles from the name column")

    simplify_title = {
        "Capt": "Officer",
        "Col": "Officer",
        "Major": "Officer",
        "Jonkheer": "Royalty",
        "Don": "Royalty",
        "Sir": "Royalty",
        "Dr": "Officer",
        "Rev": "Officer",
        "the Countess": "Royalty",
        "Dona": "Royalty",
        "Mme": "Mrs",
        "Mlle": "Miss",
        "Ms": "Mrs",
        "Mr": "Mr",
        "Mrs": "Mrs",
        "Miss": "Miss",
        "Master": "Master",
        "Lady": "Royalty"
    }

    title = df['Name'].apply(
        lambda full_name: (
            simplify_title[
                # Example: Uruchurtu, Don. Manuel E --> Don
                full_name.split(',')[1].split('.')[0].strip()
            ]
        )
    )

    merged = df.merge(title.to_frame(name='Title'),
                      left_index=True, right_index=True)
    merged['Title'] = merged['Title'].astype('category')

    return merged
