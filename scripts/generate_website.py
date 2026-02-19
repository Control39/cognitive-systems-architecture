"""
Генерирует профессиональный сайт-портфолио с поддержкой Mermaid и Git-статуса.
С полной аннотацией типов.
"""

import os
from pathlib import Path
import markdown as md
from typing import List, Tuple, Dict

INPUT_DIR: Path = Path("docs/obsidian-map")
OUTPUT_DIR: Path = Path("docs/website")
LOGO_PATH: str = "assets/logo.svg"


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>{title} — portfolio-system-architect</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    <style>
        :root {{ --primary: #1a73e8; }}
        body {{ background: #f8f9fa; color: #212529; font-family: 'Segoe UI', sans-serif; }}
        .sidebar {{ 
            background: linear-gradient(to bottom, var(--primary), #0d47a1);
            height: 100vh; 
            position: fixed; 
            color: white;
        }}
        .sidebar h5, .sidebar a {{ color: white; }}
        .sidebar a:hover {{ background: rgba(255,255,255,0.2); border-radius: 8px; }}
        .content {{ margin-left: 240px; padding: 2rem; }}
        pre {{ background: #f1f3f5; border-radius: 8px; padding: 1rem; overflow: auto; }}
        code {{ background: #e9ecef; padding: 0.2em 0.4em; border-radius: 4px; }}
        h1, h2, h3 {{ color: var(--primary); }}
        .footer {{ margin-top: 5rem; text-align: center; color: #6c757d; font-size: 0.9rem; }}
        .mermaid {{ margin: 2rem 0; }}
    </style>
</head>
<body>
    <div class="container-fluid">
        <div class="row">
            <nav class="col-md-3 col-lg-2 d-md-block sidebar">
                <div class="position-sticky pt-3">
                    <div class="text-center mb-4">
                        <img src="{logo}" alt="Logo" width="40" class="rounded">
                        <h6 class="mt-2">Portfolio Architect</h6>
                    </div>
                    <hr>
                    <ul class="nav flex-column">
{navigation}
                    </ul>
                </div>
            </nav>
            <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 content">
                <div class="d-flex justify-content-between flex-wrap align-items-center pt-3 pb-2 mb-3 border-bottom">
                    <h1>{title}</h1>
                    <a href="index.html" class="btn btn-outline-primary btn-sm"><i class="bi bi-house"></i> Home</a>
                </div>
                {content}
                <footer class="footer">
                    <p>Сгенерировано автоматически • <code>portfolio-system-architect</code></p>
                </footer>
            </main>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""


def generate_nav_links() -> str:
    """Генерирует HTML-список навигации."""
    sections: List[Tuple[str, str]] = [
        ("index", "[+] Главная"),
        ("projects", "[*] Проекты"),
        ("methodology", "[#] Методология"),
        ("architecture", "[@] Архитектура"),
        ("components", "[$] Компоненты"),
        ("career_development_system", "[!] Развитие"),
    ]
    links: List[str] = []
    for file_stem, display in sections:
        active: str = "active" if file_stem == "index" else ""
        link: str = f'                        <li><a class="nav-link {active}" href="{file_stem}.html">{display}</a></li>'
        links.append(link)
    return "\n".join(links)


def md_to_html(content: str) -> str:
    """Конвертирует Markdown в HTML с расширениями."""
    try:
        return md.markdown(
            content.replace("]]", "").replace("[[", ""),
            extensions=['fenced_code', 'codehilite', 'tables']
        )
    except Exception as e:
        return f"<p>[X] Ошибка парсинга Markdown: {e}</p>"


def convert() -> None:
    """Основная функция генерации сайта."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    navigation: str = generate_nav_links()
    logo: str = LOGO_PATH if (Path(LOGO_PATH)).exists() else "https://via.placeholder.com/40"

    index_content: str = """
# [~] Добро пожаловать в моё портфолио

> Я — **архитектор когнитивных систем**, создаю новые роли в IT, где человек управляет ИИ для проектирования сложных экосистем.

## [*] Что здесь?

- [D] Полная структура проекта
- [R] Автоматизированное документирование
- [S] Защита секретов
- [U] Самообновление
"""

    try:
        result: str = os.popen("git log -1 --format=%h%d%n%s%n(%cr)").read().strip()
        if result:
            lines: List[str] = result.split('\n')
            if len(lines) >= 3:
                commit_hash: str = lines[0].strip()
                subject: str = lines[1].strip()
                time_rel: str = lines[2].strip()
                last_commit: str = f"{commit_hash} {subject} ({time_rel})"
                index_content += f"\n- [G] Последний коммит: `{last_commit}`\n"
    except Exception:
        index_content += "\n- [E] Статус Git: не удалось получить информацию\n"

    pages: Dict[str, Tuple[str, str]] = {"index": ("Главная", index_content)}

    # Генерируем HTML для всех .md файлов
    for md_file in INPUT_DIR.glob("*.md"):
        # Сохраняем оригинальное имя без расширения
        filename = md_file.stem  # Например: "career-development-system"

        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Заголовок: заменяем - и _ на пробелы
            title = filename.replace("-", " ").replace("_", " ").title()

            # Ключ — это имя файла (с дефисами)
            pages[filename] = (title, content)

            print(f"[OK] Обработан: {filename}.md -> {filename}.html")

        except Exception as e:
            print(f"[!] Не удалось прочитать {md_file}: {e}")

    # Генерируем HTML файлы для всех страниц
    stem: str
    title: str
    content_md: str
    for stem, (title, content_md) in pages.items():
        html_content: str = md_to_html(content_md)
        html: str = HTML_TEMPLATE.format(
            title=title,
            navigation=navigation,
            content=html_content,
            logo=logo
        )
        output_path: Path = OUTPUT_DIR / f"{stem}.html"
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html)
        except Exception as e:
            print(f"[X] Не удалось записать {output_path}: {e}")

    print(f"[V] Портфолио успешно сгенерировано: {OUTPUT_DIR / 'index.html'}")


if __name__ == "__main__":
    convert()