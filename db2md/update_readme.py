from db2md.helpers import get_env
import pandas as pd  # type: ignore


def create_readme():
    readme = []

    readme.append("# Poesias")

    readme.append(
        "[![License: CC-BY-NC-SA]"
        "(https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg)]"
        "(https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)"
    )

    readme.append(
        "Olá, esse repositório é destinado para arquivo de poesias autorais "
        "em _markdown_.\n\n_Hello, this repository is intended for the archive "
        "of authorial poetry in markdown extension_."
    )

    readme.append("## Índice")
    readme = "".join(readme)

    return readme


def update(df: pd.DataFrame):
    """Update readme with the poems in repository.

    Keyword arguments:
    poems -- DataFrame of poems
    """
    categories = df["category"].unique()
    try:
        with open(
            f"{get_env('root_folder_path')}\\README.md", "r", encoding="utf-8"
        ) as f:
            readme = f.read()
    except FileNotFoundError:
        readme = create_readme()
    # TODO: Add personalization of README
    print(str(readme))

    for category in categories:
        pass
