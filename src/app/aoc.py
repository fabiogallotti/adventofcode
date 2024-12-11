import typer

from app.constants import PATH
from app.utils import import_module, print_result, read_input

app = typer.Typer()


@app.command()
def execute(year: str = "", day: str = "", part: str = ""):
    module_year = f"year{year}"
    module_day = f"day{day.zfill(2)}"
    module = "exercises.py"
    module_path = PATH / module_year / module_day / module

    exercises = import_module(module_path)
    data = read_input(year, day)

    if not part:
        print_result(exercises, "part_1", data)
        print_result(exercises, "part_2", data)
    else:
        print_result(exercises, f"part_{part}", data)
