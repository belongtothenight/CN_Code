"""
1. Parameter settings
2. Install dependencies
"""


class Config:
    def __init__(self):
        self.Platform = "win"

        self.ATKIPv4 = "192.168.137.203"
        self.ATKPort = 445  # default 80
        self.ATKBytes = 2450

        self.HPING3 = False
        self.Hammer = True
        self.HULK = True

        self.waitTime = 5  # seconds
        self.printColor = False

        self.HPING3_PARAMETERS = [
            ("  ", 1e9, "--flood", "", 0),
            ("-0", 1e9, "--flood", "", 0),
            ("-1", 1e9, "--flood", "", 3),
            ("-2", 1e9, "--flood", "", 3),
        ]
        """
        (mode, data, freq, extra args, processes)
        Recommand to use the total number of processes equal to the number of CPU cores.
        """
        self.Hammer_PARAMETERS = {
            "threads": 50,
            "hits": 100,
        }

        # ==============================================================================
        # DO NOT TOUCH !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # ==============================================================================
        self.Platform1 = "win"
        self.Platform2 = "linux"

        if self.Platform == self.Platform1:
            # windows
            self.HPING3 = False
        if self.Platform == self.Platform2:
            # linux
            if self.printColor:
                print(
                    f'{Bcolors.WARNING} Make sure to be "sudo su" before executing this script. {Bcolors.ENDC}'
                )
            else:
                print("Make sure to be 'sudo su' before executing this script.")


class Bcolors:
    # https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
