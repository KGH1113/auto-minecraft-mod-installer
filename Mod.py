from typing import Literal, List
import requests
from bs4 import BeautifulSoup
import time
import os

from rich.console import Console

from Cli import showSelectionScreen, showWarningScreen

class Mod:
    def __init__(self, name: str, version: str, loader: Literal["fabric", "neoforge", "quilt"], console: Console) -> None:
        self.name = name
        self.version = version
        self.loader = loader
        self.url = f"https://modrinth.com/mod/{name}/versions?g={version}&l={loader}"
        self.searchResult = self.searchMod()
        self.selectedMod: int = 0
        self.console = console

    def searchMod(self):
        response = requests.get(self.url)
        if response.status_code == 429:
            time.sleep(30)
            response = requests.get(self.url)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return
        soup = BeautifulSoup(response.text, "html.parser")
        found_mods_soup = soup.find_all("div", {"class": "versions-grid-row group relative"})
        result = []
        cnt = 1
        for mod_soup in found_mods_soup:
            mod_div = mod_soup.find("div", {"class": "flex flex-col justify-center gap-2 sm:contents"}).find("div")
            mod_kind = mod_div.find("div", {"class": "self-center"}).find("div").find("div").text
            mod_name = mod_div.find("div", {"class": "pointer-events-none relative z-[1] flex flex-col justify-center group-hover:underline"}).find("div", {"class": "text-xs font-medium"}).text
            mod_download_url = mod_soup.find("div", {"class": "flex items-start justify-end gap-1 sm:items-center"}).find("div").find("a")["href"]
            data = {
                "index": str(cnt),
                "kind": mod_kind, 
                "name": mod_name, 
                "url": mod_download_url
            }
            result.append(data)
            cnt += 1
        return result

    def selectMod(self):
        if len(self.searchResult) == 0:
            warningMessage = f"[bold yellow]Warning:[/] Version selection for mod named [bold yellow]{self.name}[/bold yellow] passed (Maybe no mod exist on selected version)"
            showWarningScreen(message=warningMessage, console=self.console)
            return
        
        option = []
        for mod_data in self.searchResult:
            option.append(f"{mod_data["name"]} - {mod_data["kind"]}")
            
        choice = showSelectionScreen(options=option, title=f"{self.name} (R: release / B: beta)", console=self.console)
        print(choice)
        self.selectedMod = choice
        
    def downloadMod(self):
        if self.selectedMod == 0:
            print(f"Warning: {self.name} - Mod not selected, passing installation")
            return

        file_path = os.path.join("downloads", f"{self.name}.jar")
        response = requests.get(self.searchResult[self.selectedMod - 1]["url"], stream=True)

        if response.status_code == 429:
            time.sleep(30)
            response = requests.get(self.searchResult[self.selectedMod]["url"], stream=True)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return
        with open(file_path, "wb") as file:
            file.write(response.content)
