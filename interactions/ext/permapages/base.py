"The base of the extension."

from interactions.ext import Base, Version, VersionAuthor
from .permapages import PermaPages

version = Version(
    version="0.1.0",
    author=VersionAuthor(
        name="Dworv",
        email="dwarvyt@gmail.com",
    ),
)

base = Base(
    name="Persistence",
    version=version,
    link=f"https://github.com/dworv/interactions-persistence",
    description="An extension to add simple custom_id encoding to interactions.py.",
    packages="interactions.ext.persistence",
)

def setup(bot, cipher_key=None):
    return PermaPages(bot)
