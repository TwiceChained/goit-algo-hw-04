from pathlib import Path
import sys
from colorama import init, Fore, Style

def print_tree(directory, prefix=""):
    try:
        items = list(Path(directory).iterdir())
    except PermissionError:
        print(prefix + "[Немає доступу]")
        return

    folders = []
    files = []

    for item in items:
        if item.is_dir():
            folders.append(item)
        else:
            files.append(item)

    sorted_items = folders + files



    for index, item in enumerate(sorted_items):
        if index == len(sorted_items) - 1:
            branch = "└── "
            new_prefix = prefix + "    "
        else:
            branch = "├── "
            new_prefix = prefix + "│   "

        if item.is_dir():
            print(prefix + branch + Fore.CYAN + item.name + Style.RESET_ALL)
            print_tree(item, new_prefix)
        else:
            print(prefix + branch + Fore.WHITE + item.name + Style.RESET_ALL)



def main():
    if len(sys.argv) != 2:
        print("Використання: python main.py + |шлях_до_директорії|")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"❌ Шлях {path} не існує.")
        return

    if not path.is_dir():
        print(f"❌ {path} — це не директорія.")
        return

    init()
    print(Fore.YELLOW + path.name + Style.RESET_ALL)
    print_tree(path)

if __name__ == "__main__":
    main()


#Для запуску використав команду: python .\Third_task\main.py D:\GoIt\Repositories\fourth_repo\goit-algo-hw-04\Third_task