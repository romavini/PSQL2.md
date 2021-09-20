from db2md.helpers import get_env
import pandas as pd  # type: ignore


def create_readme():
    readme = []

    readme.append("# Poesias ✒🤖\n")

    readme.append(
        "[![License: CC-BY-NC-SA]"
        "(https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg)]"
        "(https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)\n\n"
    )

    readme.append(
        "Olá, esse repositório é destinado para arquivo de poesias autorais "
        "em _markdown_.\n"
        "Este repositório faz parte de um projeto de estudo de SQL. As poesias aqui "
        "registradas foram [coletadas, inseridas em uma base de dados]"
        "(https://github.com/romavini/Web-Scraping-Recanto-Das-Letras) "
        "e depois [transformadas em arquivo _markdown_]"
        "(https://github.com/romavini/PSQL_2_.md) "
        "em um processo automatizado.\n\n"
        "_Hello, this repository is intended for the archive of authorial poetry "
        "in markdown extension.\n"
        "This repository is part of a SQL study project. The poems registered here were "
        "[collected, entered into a database]"
        "(https://github.com/romavini/Web-Scraping-Recanto-Das-Letras) and then "
        "[transformed into _markdown_ file](https://github.com/romavini/PSQL_2_.md) "
        "in an automated process._\n\n"
    )

    readme.append("## Índice")
    readme = "".join(readme)

    return readme


def update(df: pd.DataFrame):
    """Update readme with the poems in repository.

    Keyword arguments:
    poems -- DataFrame of poems
    """
    categories = list(df["category"].unique())
    categories.sort()
    try:
        with open(
            f"{get_env('root_folder_path')}\\README.md", "r", encoding="utf-8"
        ) as f:
            readme = f.read()
            if not readme:
                readme = create_readme()
    except FileNotFoundError:
        readme = create_readme()

    text = [readme[: readme.index("## Índice") + 9]]
    text.append("\n\n")

    for category in categories:
        if "›" not in category:
            text.append("".join([f" - [{category}](poemas/{category})", "\n"]))
        else:
            text.append(
                "".join(
                    [
                        f"   - [{category.split(' › ')[-1]}]"
                        f"(poemas/{category.replace(' › ', '%20›%20')})",
                        "\n",
                    ]
                )
            )

    readme = "".join(text)

    with open(f"{get_env('root_folder_path')}\\README.md", "w", encoding="utf-8") as f:
        f.write(readme)
