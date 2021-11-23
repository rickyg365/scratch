import time
import numpy as np

from rich import pretty, inspect

from rich.tree import Tree
from rich.table import Table
from rich.progress import track
from rich.console import Console
from rich.markdown import Markdown


# pretty.install()

console = Console()


def test_print():
    """ Rich console print and print """
    '''
    from rich import print
        - the regular print function also adds any rich syntax!
    '''

    sample_text = f"\n[bold blue]Guess what?[/bold blue] \n[i red]Chicken butt[/i red] \nHAHAHA"
    
    print("\nPrint: ", sample_text)
    print(f"\nPrint f-string: {sample_text}")
    
    console.print("\nRich console print: ", sample_text)
    console.print(f"\nRich console print f-string: {sample_text}")


def test_inspect():
    """ Rich Object Inspect w/ methods"""
    sample_obj = [f"item {x}" for x in np.arange(10)]
    numpy_obj = np.arange(1, 11)

    # inspect(sample_obj, methods=True)
    inspect(numpy_obj, methods=True)


def test_log():
    """ Rich Log, almost like print except adds timestamp """
    test_data = [
        {"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1",},
        {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
        {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
    ]
   
    enabled = False
    context = {
        "foo": "bar",
    }
    movies = ["Deadpool", "Rise of the Skywalker"]
    console.log("Hello from", console, "!")
    console.log(test_data, log_locals=True)


def test_emoji():
    """ Rich Emojis """
    console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")


def test_table():
    """ Rich Tables """
    '''
    from rich import box
    table = Table(title="Star Wars Movies", box=box.MINIMAL_DOUBLE_HEAD)
    
            box.ASCII                   box.SQUARE                box.MINIMAL       
    +------------------------+  ┌────────────┬───────────┐
    | Header 1   | Header 2  |  │ Header 1   │ Header 2  │    Header 1  │ Header 2 
    |------------+-----------|  ├────────────┼───────────┤   ───────────┼──────────
    | Cell       | Cell      |  │ Cell       │ Cell      │    Cell      │ Cell     
    | Cell       | Cell      |  │ Cell       │ Cell      │    Cell      │ Cell     
    |------------+-----------|  ├────────────┼───────────┤   ───────────┼──────────
    | Footer 1   | Footer 2  |  │ Footer 1   │ Footer 2  │    Footer 1  │ Footer 2 
    +------------------------+  └────────────┴───────────┘


    box.MINIMAL_HEAVY_HEAD     box.MINIMAL_DOUBLE_HEAD           box.SIMPLE       

    Header 1   │ Header 2       Header 1   │ Header 2       Header 1    Header 2 
    ━━━━━━━━━━━━┿━━━━━━━━━━━    ════════════╪═══════════   ────────────────────────
    Cell       │ Cell           Cell       │ Cell           Cell        Cell     
    Cell       │ Cell           Cell       │ Cell           Cell        Cell     
    ────────────┼───────────    ────────────┼───────────   ────────────────────────
    Footer 1   │ Footer 2       Footer 1   │ Footer 2       Footer 1    Footer 2 



        box.SIMPLE_HEAVY            box.HORIZONTALS              box.ROUNDED       
                                ──────────────────────────  ╭───────────┬──────────╮
    Header 1     Header 2       Header 1     Header 2     │ Header 1  │ Header 2 │
    ╺━━━━━━━━━━━━━━━━━━━━━━━━╸  ──────────────────────────  ├───────────┼──────────┤
    Cell         Cell           Cell         Cell         │ Cell      │ Cell     │
    Cell         Cell           Cell         Cell         │ Cell      │ Cell     │
    ╺━━━━━━━━━━━━━━━━━━━━━━━━╸  ──────────────────────────  ├───────────┼──────────┤
    Footer 1     Footer 2       Footer 1     Footer 2     │ Footer 1  │ Footer 2 │
                                ──────────────────────────  ╰───────────┴──────────╯


            box.HEAVY                 box.HEAVY_EDGE             box.HEAVY_HEAD     
    ┏━━━━━━━━━━━━┳━━━━━━━━━━━┓  ┏━━━━━━━━━━━━┯━━━━━━━━━━━┓  ┏━━━━━━━━━━━┳━━━━━━━━━━┓
    ┃ Header 1   ┃ Header 2  ┃  ┃ Header 1   │ Header 2  ┃  ┃ Header 1  ┃ Header 2 ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━┫  ┠────────────┼───────────┨  ┡━━━━━━━━━━━╇━━━━━━━━━━┩
    ┃ Cell       ┃ Cell      ┃  ┃ Cell       │ Cell      ┃  │ Cell      │ Cell     │
    ┃ Cell       ┃ Cell      ┃  ┃ Cell       │ Cell      ┃  │ Cell      │ Cell     │
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━┫  ┠────────────┼───────────┨  ├───────────┼──────────┤
    ┃ Footer 1   ┃ Footer 2  ┃  ┃ Footer 1   │ Footer 2  ┃  │ Footer 1  │ Footer 2 │
    ┗━━━━━━━━━━━━┻━━━━━━━━━━━┛  ┗━━━━━━━━━━━━┷━━━━━━━━━━━┛  └───────────┴──────────┘


            box.DOUBLE               box.DOUBLE_EDGE      
    ╔════════════╦═══════════╗  ╔════════════╤═══════════╗
    ║ Header 1   ║ Header 2  ║  ║ Header 1   │ Header 2  ║
    ╠════════════╬═══════════╣  ╟────────────┼───────────╢
    ║ Cell       ║ Cell      ║  ║ Cell       │ Cell      ║
    ║ Cell       ║ Cell      ║  ║ Cell       │ Cell      ║
    ╠════════════╬═══════════╣  ╟────────────┼───────────╢
    ║ Footer 1   ║ Footer 2  ║  ║ Footer 1   │ Footer 2  ║
    ╚════════════╩═══════════╝  ╚════════════╧═══════════╝
    
    '''
    # empty table
    # print(table) if table.columns else print("[i]No data...[/i]")    

    table = Table(title="Star Wars Movies")

    table.add_column("Released", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Box Office", justify="right", style="green")

    table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
    table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
    table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
    table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

    console.print(table)


def test_status():
    """ Status """

    tasks = [f"task {n}" for n in range(1, 11)]

    with console.status("[bold green]Working on tasks...") as status:
        while tasks:
            task = tasks.pop(0)
            time.sleep(1)
            # task = "task $"
            console.log(f"{task} complete")  # => task $ complete


def test_progress_bar():
    """ Progress bar """
    # the step is just whatever the iterable/ generator yields as it loops, in this case the numbers 1-99

    for step in track(range(100)):
        time.sleep(.5)
        # do_step(step)


def test_tree():
    # Create root
    # tree = Tree("Rich Tree")
    tree = Tree("Rich Tree", guide_style="bold bright_blue")

    # add branches
    tree.add("foo")
    tree.add("bar")
    
    baz_tree = tree.add("baz")
    baz_tree.add("[red]Red").add("[green]Green").add("[blue]Blue")

    console.print(tree)


def test_markdown():
    """ Rich Markdown """
    with open("rich_readme.md") as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)


if __name__ == "__main__":
    print("")

    test_print()
    # test_inspect()
    # test_log()
    # test_emoji()
    # test_table()
    # test_status()
    # test_progress_bar()
    # test_tree()
    # test_markdown()
