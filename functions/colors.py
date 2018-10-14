from colorama import Fore, Style, init
import random

init()


class Colors:
    def __init__(self):
        self.blue = Fore.BLUE
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.yellow = Fore.YELLOW
        self.cyan = Fore.CYAN
        self.magenta = Fore.MAGENTA
        self.reset = Style.RESET_ALL
        self.colors = [self.blue, self.red, self.green, self.yellow, self.cyan, self.magenta]
        self.colors_left = [self.blue, self.red, self.green, self.yellow, self.cyan, self.magenta]

    def pick(self):
        i = random.randint(0, len(self.colors_left))
        color = self.colors_left[i]
        del self.colors_left[i]
        return color