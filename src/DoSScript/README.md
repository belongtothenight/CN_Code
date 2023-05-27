# DoSScript

This folder holds code for activating DDoS attacks with known tools like "hping3". <br>
DO NOT USE THESE SCRIPTS FOR MALICIOUS PURPOSES. THESE ARE PREPARED ONLY FOR EDUCATIONAL PURPOSES.

## Files

| Filename      | Description                                                                                                                                                                          |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| main.py       | Intergrated DoS starter script for testing and debugging.                                                                                                                            |
| config.py     | Manages all of the settings.                                                                                                                                                         |
| hping3.py     | <code style="color:Blue">/MULTI/</code> Multiprocess attacker with hping3.                                                                                                           |
| hammer.py     | <code style="color:Orange">/TCP + HTTP/</code> Slim version of [hammering.py](https://github.com/depascaldc/DoS-Tool/blob/master/hammering.py).                                      |
| hulk.py       | <code style="color:Lime">/UDP/</code> Slim version of [HULK](https://github.com/R3DHULK/HULK).                                                                                       |
| tcp1.py       | <code style="color:Violet">/TCP/</code> Experiment version of [flood.py](https://github.com/Leeon123/TCP-UDP-Flood/blob/master/flood.py).                                            |
| tcp2.py       | <code style="color:Violet">/TCP/</code> Experiment version of [Make SYN Flooding Attack in Python](https://www.thepythoncode.com/article/syn-flooding-attack-using-scapy-in-python). |
| slowloris.py  | <code style="color:Violet">/TCP/</code> Slim version of [slowloris.py](https://github.com/gkbrk/slowloris/blob/master/slowloris.py).                                                 |
| integrated.py | Intergrate the above scripts (tested) into a single file.                                                                                                                            |

## Future Options

1. botnet
2. other protocols

## Attack Target

Samba server.

1. Samba is based on SMB protocol.
2. SMB is based on NetBIOS API.
3. NetBIOS based on
   1. TCP: port 445(main), 137, 139.
   2. UDP: ports 137, 138.

## Experiment

Platform:
Server with 1Gbps ethernet connection.

1. With [hping3.py](https://github.com/belongtothenight/CN_Code/blob/main/src/DDoSScript/hping3.py), only ICMP mode can deal real impact. For the maximum impact, I achieved around 300Mbps at peak with one machine and creates an inverted parabolic signal-like shape.
2. With [hammering.py](https://github.com/depascaldc/DoS-Tool/blob/master/hammering.py), I achieved a constant 400Mbps network I/O with a single machine. With around 15 machines running 100 hits per run & 50 threads, we were able to bring the NAS file transferring speed from more than 100MBps to around 5 to 20MBps.
3. With [HULK](https://github.com/R3DHULK/HULK), my friend achieved around 800Mbps with one machine, which is nearly the maximum value. One machine doesn't impact the file-transferring speed at all.
4. With HULK and Hammering launched on 11 machines, we successfully DDoS a Samba NAS server to be unable to transfer any data. [click to see experiment video](https://youtu.be/nqfeB_wc9l4)
