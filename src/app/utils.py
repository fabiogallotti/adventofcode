import os
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import requests
import typer
from dotenv import load_dotenv

from app.constants import INPUTS_PATH

load_dotenv()


def import_module(module_path):
    if not module_path.exists():
        typer.echo(f"Module file {module_path} does not exist!")
        raise typer.Exit(code=1)

    spec = spec_from_file_location("exercises", module_path)
    exercises = module_from_spec(spec)
    spec.loader.exec_module(exercises)

    return exercises


def read_cached_input(filename):
    with open(filename) as f:
        return [x.rstrip("\n") for x in f.readlines()]


def read_input(year, day):
    filename = INPUTS_PATH / year / f"{day}.txt"

    if Path.is_file(filename):
        return read_cached_input(filename)

    session = add_session_cookie()
    try:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        response = session.get(url)
        content = response.text
    except Exception as e:
        typer.echo(f"error downloading input: {e}")
        raise typer.Exit(code=1) from e

    if not (year_folder := Path(INPUTS_PATH / year)).exists():
        year_folder.mkdir(parents=True)

    with open(filename, "w", newline="") as f:
        f.write(content.rstrip("\n"))

    return [x.rstrip("\n") for x in content.split("\n") if x.rstrip("\n")]


def add_session_cookie():
    session_id = os.getenv("SESSION_ID")
    session = requests.Session()
    session.cookies.set("session", session_id)
    return session


def print_result(exercises, function, data):
    if not hasattr(exercises, function):
        typer.echo(f"{function=} not found!")
        raise typer.Exit(code=1)

    part = getattr(exercises, function)
    result = part(data)
    typer.echo(f"Result {function}: {result}")
