from __future__ import annotations

import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
OUTPUT_FILE = DOCS_DIR / "conteudos.md"


CATEGORIES: dict[str, dict[str, str]] = {
    "inteligencia-artificial": {
        "title": "Inteligência Artificial",
        "icon": ":material-robot-outline:",
        "description": (
            "IA Generativa, LLMs, agentes, documentação e "
            "desenvolvimento de software assistido por IA."
        ),
    },
    "python": {
        "title": "Python",
        "icon": ":fontawesome-brands-python:",
        "description": (
            "Bibliotecas, processamento assíncrono, ETL, "
            "validação de dados e Engenharia de Dados."
        ),
    },
    "django": {
        "title": "Django",
        "icon": ":simple-django:",
        "description": (
            "Django ORM, integridade de dados, performance "
            "e consultas avançadas."
        ),
    },
    "arquitetura": {
        "title": "Arquitetura de Software",
        "icon": ":material-vector-arrange-above:",
        "description": (
            "Sistemas distribuídos, resiliência, eventos, "
            "mensageria e integração entre serviços."
        ),
    },
    "cloud-devops": {
        "title": "Cloud e DevOps",
        "icon": ":material-cloud-outline:",
        "description": (
            "Kubernetes, observabilidade, produção, deploys "
            "e operação de aplicações."
        ),
    },
    "engenharia-software": {
        "title": "Engenharia de Software",
        "icon": ":material-code-braces:",
        "description": (
            "Práticas para desenvolver, documentar e entregar "
            "software com mais qualidade."
        ),
    },
    "produto-colaboracao": {
        "title": "Produto e Colaboração",
        "icon": ":material-account-group-outline:",
        "description": (
            "Comunicação, refinamentos, ferramentas, dashboards "
            "e colaboração entre Produto e Engenharia."
        ),
    },
}


def extract_front_matter_title(content: str) -> str | None:
    if not content.startswith("---"):
        return None

    match = re.match(
        r"^---\s*\n(.*?)\n---",
        content,
        flags=re.DOTALL,
    )

    if not match:
        return None

    front_matter = match.group(1)

    title_match = re.search(
        r"^title:\s*(.+?)\s*$",
        front_matter,
        flags=re.MULTILINE,
    )

    if not title_match:
        return None

    title = title_match.group(1).strip()

    if (
        len(title) >= 2
        and title[0] == title[-1]
        and title[0] in {'"', "'"}
    ):
        title = title[1:-1]

    return title.strip()


def extract_heading_title(content: str) -> str | None:
    match = re.search(
        r"^#\s+(.+?)\s*$",
        content,
        flags=re.MULTILINE,
    )

    if not match:
        return None

    return match.group(1).strip()


def article_title(path: Path) -> str:
    content = path.read_text(encoding="utf-8")

    title = (
        extract_front_matter_title(content)
        or extract_heading_title(content)
    )

    if title:
        return title

    return path.stem.replace("-", " ").title()


def find_articles(folder_name: str) -> list[dict[str, str]]:
    folder = DOCS_DIR / folder_name

    if not folder.exists():
        return []

    articles: list[dict[str, str]] = []

    for path in folder.glob("*.md"):
        if path.name == "index.md":
            continue

        articles.append(
            {
                "title": article_title(path),
                "link": f"{folder_name}/{path.name}",
            }
        )

    return sorted(
        articles,
        key=lambda article: article["title"].casefold(),
    )


def build_category_card(
    folder_name: str,
    category: dict[str, str],
) -> str:
    articles = find_articles(folder_name)

    if not articles:
        return ""

    links = "\n".join(
        f"    - [{article['title']}]({article['link']})"
        for article in articles
    )

    return f"""-   {category["icon"]}{{ .lg .middle }} **{category["title"]}**

    ---

    {category["description"]}

{links}
"""


def generate_contents_page() -> None:
    cards: list[str] = []
    total_articles = 0

    for folder_name, category in CATEGORIES.items():
        articles = find_articles(folder_name)
        total_articles += len(articles)

        card = build_category_card(
            folder_name=folder_name,
            category=category,
        )

        if card:
            cards.append(card)

    cards_content = "\n".join(cards)

    content = f"""---
title: Todos os conteúdos
description: Artigos sobre Python, Django, arquitetura de software, Cloud, DevOps, Inteligência Artificial e colaboração.
hide:
  - navigation
  - toc
---

<div class="grid cards" markdown>

{cards_content}
</div>

---

Esta página é atualizada automaticamente com base nos artigos publicados.
"""

    OUTPUT_FILE.write_text(
        content,
        encoding="utf-8",
    )

    print(
        f"Página de conteúdos atualizada: "
        f"{total_articles} artigos encontrados."
    )


def build_navigation() -> list[dict[str, Any]]:
    nav: list[dict[str, Any]] = [
        {"Início": "index.md"},
        {"Conteúdos": "conteudos.md"},
    ]

    for folder_name, category in CATEGORIES.items():
        articles = find_articles(folder_name)

        if not articles:
            continue

        category_items = [
            {article["title"]: article["link"]}
            for article in articles
        ]

        nav.append(
            {
                category["title"]: category_items,
            }
        )

    nav.extend(
        [
            {"Sobre": "sobre.md"},
        ]
    )

    return nav


def on_config(config: Any, **kwargs: Any) -> Any:
    generate_contents_page()

    config["nav"] = build_navigation()

    print("Menu de navegação atualizado automaticamente.")

    return config