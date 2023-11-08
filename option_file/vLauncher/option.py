"""vLauncher test case"""
from option_file.vLauncher.title.option import vLauncherTitle
from option_file import item_strategy


class vLauncher(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "vLauncher title",
    }

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def run_all(self):
        vLauncherTitle(self.event_gen, self.driver, self.reporter).run()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    vLauncherTitle(self.event_gen, self.driver, self.reporter).run()
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    pass
                case "7":
                    pass
                case "8":
                    pass
                case "9":
                    pass
                case "10":
                    pass
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
