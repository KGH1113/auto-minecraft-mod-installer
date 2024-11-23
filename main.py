from typing import List

import os

from rich.console import Console
import pyfiglet
from Cli import showSelectionScreen

from Mod import Mod

def main():
    console = Console()

    downloadsDir = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(downloadsDir):
        os.mkdir(downloadsDir)

    title = pyfiglet.figlet_format("Auto Minecraft Mod Installer")

    console.clear()
    console.print(f"[bold magenta]{title}[/bold magenta]")
    console.print("[bold magenta]Welcome to auto minecraft mod installer.[/bold magenta]")

    while True:
        choice = console.input("[bold cyan]Press enter to start > [/bold cyan]")
        if choice == "":
            break
    
    mod_names_list: List[str] = []
    mod_list: List[Mod] = []

    with open("mods.txt", "r") as f:
        for line in f.readlines():
            mod_name = line.replace("\n", "")
            if len(mod_name) == 0:
                continue
            mod_names_list.append(mod_name)
    
    console.clear()

    version = ""
    while True:
        version = console.input("[bold cyan]Input version you want > [/bold cyan]")
        if version != "":
            break

    console.clear()

    loaders = ["fabric", "neoforge", "quilt"]
    loaderIndex = showSelectionScreen(title="[bold cyan]Input mod loader you want > [/bold cyan]", options=["fabric", "neoforge", "quilt"], console=console)
    loader = loaders[loaderIndex - 1]


    console.clear()

    with console.status("[bold green]Fetching mod list (Might take a while)...[/bold green]", spinner="dots"):
        for mod_name in mod_names_list:
            mod = Mod(mod_name, version, loader, console=console)
            mod_list.append(mod)

    console.print("[bold green]Done.[/bold green]")

    for mod in mod_list:
        mod.selectMod()

    with console.status("[bold green]Downloading mods...[/bold green]", spinner="dots"):
        for mod in mod_list:
            mod.downloadMod()

    console.clear()
    
    console.print("✅ [bold green]Your installation has been completed. Installed mods are in ./downloads folder.[/bold green]")

try:
    main()
except KeyboardInterrupt:
    pass