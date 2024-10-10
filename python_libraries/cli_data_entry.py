from rich.console import Console
from rich.table import Table
import json  # you can switch to txt or csv depending on your preferred format

# Create a Console instance
console = Console()

# Function to display initial data using a Rich table
def display_initial_data():
    console.print("Here is some initial data:", style="bold cyan")
    table = Table(title="Hockey_Players")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Age", style="magenta")
    table.add_column("Team", justify="right")
    table.add_row("Connor Bedard", "19 Years Old", "Blackhawks")
    table.add_row("Patrick Kane", "35 Years Old", "Red Wings")
    table.add_row("Artemi Panarin", "32 Years Old", "Rangers")
    console.print(table)

# Function to collect movie data from the user
def collect_player_data():
    players = []
    while True:
        player = {}
        player["Name"] = console.input("Enter the player's name:")
        player["Age"] = console.input("Enter the player's age:")
        player["Team"] = console.input("Enter the player's team:")
        
        # Display entered data and ask for confirmation
        console.print(f"\n[bold yellow]You entered:[/bold yellow] {player}")
        confirm = console.input("[bold cyan]Is this data correct? (yes/no): [/bold cyan]").strip().lower()

        if confirm == 'yes':
            players.append(player)
            another = console.input("[bold cyan]Do you want to add another player? (yes/no): [/bold cyan]").strip().lower()
            if another != 'yes':
                break
        else:
            console.print("[bold red]Please re-enter the player data.[/bold red]")
    return players

# Function to save the data to a file
def save_data_to_file(data, file_name='players.json'):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    console.print(f"[bold green]Data has been saved to {file_name}.[/bold green]")

# Main script execution
if __name__ == "__main__":
    display_initial_data()
    user_players = collect_player_data()
    save_data_to_file(user_players)
