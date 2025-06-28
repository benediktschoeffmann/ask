from typing import Optional
from engine import ask

import typer

from __init__ import __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} version {__version__}\n")
        raise typer.Exit()

def _ask_callback() -> None:
    """
    Run the ask script from the command line.
    """
    ask()

@app.callback()     
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=False,
    ),
    ask: Optional[bool] = typer.Option(
        None,
        "--ask",
        "-a",
        help="Run the ask script.",
        callback=_ask_callback,
        is_eager=True,
    ),
        
) -> None:
    return

