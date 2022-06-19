from pathlib import Path
from typing import Union

from .fs import PagesFolder

from interactions import Extension

class PermaPages(Extension):
    """
    The main class for the PermaPages extension.
    """
    def __init__(self, bot, path: Union[Path, str]=None):
        self.bot = bot
        self.folder = PagesFolder(path)
        
        print(self.folder.get_page("test", 1))