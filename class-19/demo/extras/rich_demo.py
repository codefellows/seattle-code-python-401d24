from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

# Instantiate a console object
console = Console()

# Greet the user
console.print("Hello, [bold green]User[/bold green]!")

# Ask user's name
name = Prompt.ask("What is your name?")

# Display a message to the user
console.print(f"Nice to meet you, [bold blue]{name}[/bold blue]!")

# Create a table
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Name", style="dim", width=20)
table.add_column("Age")
table.add_column("Country")

# Add rows to the table
table.add_row("John Doe", "30", "USA")
table.add_row("Jane Doe", "25", "Canada")
table.add_row(name, Prompt.ask("What is your age?"), Prompt.ask("What is your country?"))

# Display the table
console.print(table)

# More examples:

# To change the color of the text, you can use square brackets to
# enclose the name of the color and the text you want to colorize:
console.print("[red]Hello, World![/red]")  # Prints "Hello, World!" in red
# `rich` supports a wide variety of colors, including `red`, `green`, `blue`, `cyan`, `magenta`, `yellow`, and `black`.

# You can make text bold, italic, underline, or strikethrough:
console.print("[bold]Hello, World![/bold]")         # Prints "Hello, World!" in bold
console.print("[italic]Hello, World![/italic]")     # Prints "Hello, World!" in italic
console.print("[underline]Hello, World![/underline]") # Prints "Hello, World!" with an underline
console.print("[strikethrough]Hello, World![/strikethrough]") # Prints "Hello, World!" with a strikethrough

# Styles can be combined with colors:
console.print("[bold red]Hello, World![/bold red]")  # Prints "Hello, World!" in bold red
# You can nest styles within each other. The innermost style takes precedence:
console.print("[red]Hello, [bold]World![/bold][/red]")  # Prints "Hello, " in red, and "World!" in bold red

# Remember to close your tags with `[/]`. This tells `rich` where the style or color should end:
console.print("[red]Hello, World![/red] This is not red.")  # Only "Hello, World!" is red
