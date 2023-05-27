# Wifi Cracking

## Testing Environment

1. OS: Kali-Linux 2023.1 64-bit NetInstaller image.
2. Wifi Adapter (monitor mode supported)
   1. tp-link WN722NV4
      1. Driver installation: <https://github.com/varkmarker/Tp-linkWN722NV2> (only successful installation method we found)
   2. tp-link AC600 / Archer T2U Plus
      1. Driver doesn't work. <https://github.com/nlkguy/archer-t2u-plus-linux>

## Experiment guide

1. [Use Aircrack-ng to brute force WPA/WPA2 encrypted wifi password](http://shazikai.blogspot.com/2015/01/aircrack-ng-wpawpa2-wifi.html) (main)
2. [Wifi internet encryption and cracking](https://ithelp.ithome.com.tw/articles/10189183)

Note: Extra time is needed to gather packets of 4-way handshake. (like 1000 times)

## Extra link

1. [Common password credentials by danielmiessler/SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials)
