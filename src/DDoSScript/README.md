# DDoSScript

This folder holds code for activating DDoS attacks with known tools like "hping3".

## Experiment

Platform:
Server with 1Gbps ethernet connection.

1. With [DDoS_hping3.py](https://github.com/belongtothenight/CN_Code/blob/main/src/DDoSScript/DDoS_hping3.py), only ICMP mode can deal real impact. For the maximum impact, I achieved around 300Mbps at peak with one machine and creates an inverted parabolic signal-like shape.
2. With [hammering.py](https://github.com/depascaldc/DoS-Tool/blob/master/hammering.py), I achieved a constant 400Mbps network I/O with a single machine. With around 15 machines running 100 hits per run & 50 threads, we were able to bring the NAS file transferring speed from more than 100MBps to around 5 to 20MBps.
3. With [HULK](https://github.com/R3DHULK/HULK), my friend achieved around 800Mbps with one machine, which is nearly the maximum value. One machine doesn't impact the file-transferring speed at all.
