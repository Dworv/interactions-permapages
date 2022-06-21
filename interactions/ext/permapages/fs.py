from pathlib import Path
from sys import modules
from typing import Union

from yaml import load, dump, CLoader, CDumper


class PagesFolder:
    """
    The folder housing all pages from the extension.
    """
    def __init__(self, path: Union[Path, str]):
        if not path:
            path = Path(modules["__main__"].__file__).parent.absolute() / "paginators"
            path.mkdir(exist_ok=True, parents=True)
            note = path / "note.md"
            note.write_text("You can set your own path to the paginators folder in `bot.load(...path=YOUR_PATH)`.")
        elif isinstance(path, str):
            path = Path(path)
        self.path = path
    
    def get_page(self, paginator: str, page: int):
        """
        Get a page from the paginators folder.
        """
        path = self.path / (paginator + ".yaml")
        if not path.exists():
            return None
        with open(path, "rb") as file:
            paginator: dict = load(file, CLoader)
            if len(paginator) < page:
                return None
            return paginator["pages"][page]
