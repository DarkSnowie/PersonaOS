from pathlib import Path

def load_theme(theme="persona"):
    theme_path = (
        Path(__file__).parent.parent
        / "themes"
        / f"{theme}.qss"
    )
    return theme_path.read_text(encoding="utf-8")
