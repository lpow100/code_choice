import random
from utils import *
import typer

cli = typer.Typer()

projects = ["Chat Bot","Menu","Platformer","Falling x","Flying x"]
@cli.command("random")
def random_project():
    current_project = random.choice(projects)
    print(f"Make: {current_project}.")
    reply = input("Is that good? [y/n]: ").lower()
    if reply == "y":
        print(f"Ok go and make {current_project}.")
    else:
        print("Ok I'll take that as a no.")
        random_project()
        
@cli.command("save")
def save_project(name:str,filepath:str):
    project = [name,filepath]
    save(project,"projects.json")
    print(f"saved: {name}.\npath: {filepath}")
    
if __name__ == "__main__":
    cli()
