"""
This lib is used to sign a request using aws signature version 4. You
need to provide a python dict which represent your request(it typically
contains `verb`, `uri`, `args`, `headers`, `body`), and your access key
and your secret key. This lib will add signature to the request.
"""

from .awssign import (
    Signer,
)

__name__ = "k3awssign"

__all__ = [
    "Signer",
]


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3awssign")
