from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich import box
from random import randint
console = Console()


menu_panel = Panel(
    "[light_green][1] start game\n[2] game's history\n[3] exit",
    title ="[bold red]=-=-=-MENU-=-=-=",
    title_align="center",
    border_style="cyan",
    box=box.DOUBLE, 
    expand=False,       
    padding=(2, 2)       
)

game_panel = Panel(
    "[firebrick][1]"
)

while True:
    console.clear()
    console.print(menu_panel)
    choice = Prompt.ask(
        "SELECT", 
        choices=["1", "2", "3"], 
    )
    match choice:
        case "1":

        case "2": 
        case "3": break