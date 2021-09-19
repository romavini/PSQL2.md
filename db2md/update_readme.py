from db2md.helpers import get_env
import pandas as pd


def update(df: pd.DataFrame):
    """Update readme with the poems in repository.

    Keyword arguments:
    poems -- DataFrame of poems
    """
    categories = df["category"].unique()
    with open(f"{get_env('readme_folder_path')}\\README.md", "r") as f:
        readme = f.read()

    print(readme)
    for category in categories:
        pass
