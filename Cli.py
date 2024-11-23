from typing import List

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

def showSelectionScreen(options: List[str], title: str, console: Console) -> str:
    while True:
        # Create a Table for the selection screen
        table = Table(title=title, title_justify="left", min_width=60, expand=True)
        table.add_column("No.", justify="left", style="cyan", width=1)
        table.add_column("Option", style="bold magenta", justify="left")

        # Add options to the table
        for idx, option in enumerate(options, start=1):
            table.add_row(str(idx), option)

        # Clear the screen and display the table
        console.clear()
        # console.print(Panel(table, border_style="blue"))
        console.print(table)
        
        # Prompt for user selection
        console.print("\n[bold cyan]Enter the number of your choice ('ctrl+c' to quit):[/bold cyan]")
        choice = console.input("> ")

        # Validate user input
        if choice.isdigit():
            choice_idx = int(choice)
            if 0 <= choice_idx <= len(options):
                return choice_idx
            else:
                console.print("[bold red]Invalid choice, please try again.[/bold red]")
        else:
            console.print("[bold red]Invalid input, please try again.[/bold red]")

def showWarningScreen(message: str, console: Console):
    while True:
        console.clear()

        console.log(message, style="yellow")
        choice = console.input("[bold yellow]ok(y)/quit(ctrl+c) > [/bold yellow]")

        if choice.lower() == 'y':
            break
        else:
            console.print("[bold red]Invalid input, please try again.[/bold red]")

if __name__ == "__main__":
    console = Console()
    showSelectionScreen(title="armor-chroma-for-fabric (R: release / B: beta)", options=["v1.2.9 - R"], console=console)
