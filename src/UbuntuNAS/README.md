# Setup NAS on Ubuntu

<details><summary>NAS Setup Sources</summary>

- webmin samba configuration (outdated): https://webmin.com/samba-howto.html
- setup samba in ubuntu (partially used): https://phoenixnap.com/kb/ubuntu-samba
- How to create a NAS with ubuntu server (partially used): https://www.youtube.com/watch?v=-5Z_-3EBIHE
- File of detail of the above YT video: https://quidsup.net/downloads/CreatingaNASwithUbuntuServer.pdf
- Ubuntu Server: Getting started with a linux server: https://www.youtube.com/watch?v=2Btkx9toufg

</details>

***

<details><summary>SECTION 1 - New VM</summary>
(VM from lab518 would encounter SSH problem)

1. Download VM ISO file from "https://releases.ubuntu.com/18.04/".
2. With VMware, "Create New Virtual Machine", and finish the entire setup.

- full name: dachuan
- user name: user
- password:  123456

</details>

***

<details><summary>SECTION 2 - Establish SSH connection</summary>

- Setup process: https://www.youtube.com/watch?v=Wlmne44M6fQ
- SSH error: https://stackoverflow.com/questions/20840012/ssh-remote-host-identification-has-changed

1. In VM, use "sudo apt-get update".
2. In VM, use "sudo apt-get dist-upgrade".
3. In VM, use "sudo apt-get install openssh-server"
4. In VM, use "sudo systemctl status ssh" to check SSH server status. Make sure its running, and "ctrl+C" to exit.
5. In VM, use "ip a". Find IPv4 address like "inet 192.168.xxx.xxx/xx brd 192.168.xxx.xxx scope global dynamic noprefixroute ens33"
6. In windows CMD, use "ssh user@192.168.xxx.xxx" to obtain access.

</details>

***

<details><summary>SECTION 3 - Install Samba</summary>

1. In VM, use "sudo apt-get install samba" to install.
2. In VM, use "whereis samba" to locate directory containing it.
3. In VM, use "samba -V" to check samba version.
4. In VM, use "sudo systemctl status smbd" to check samba status, which should be running.

</details>

***

<details><summary>SECTION 4 - Install Webmin</summary>

- Webmin Files: https://sourceforge.net/projects/webadmin/files/webmin/ (go in each version to find .deb file)

1. In VM, use "sudo apt-get install libapt-pkg-perl libnet-ssleay-perl libauthen-pam-perl libio-pty-perl apt-show-versions" for desktop iso, or "sudo apt-get install libapt-pkg-perl libnet-ssleay-perl libauthen-pam-perl libio-pty-perl apt-show-versions unzip" for server iso to install necessary libraries.
2. In VM, use "cd ~" to go to directory to download webmin.
3. In VM, use "wget http://prdownloads.sourceforge.net/webadmin/webmin_x.xxx_all.deb" to download. ("x.xxx" corresponds to the newest version of webmin. If the download is unsuccessful, download it in other machines and use software like WinSCP to send the file into server)
4. In VM, use "sudo dpkg -i webmin*.deb" to install webmin.
5. In VM, use "sudo reboot" to force reboot to complete the setup.
6. In VM, use "sudo systemctl status webmin" to check its status, which should be running.

</details>

***

<details><summary>SECTION 5 - Samba setup (add user / set sharing folder)</summary>

- windows explorer error: https://superuser.com/questions/496326/you-dont-have-permission-to-copy-files-to-this-location-over-the-network-erro
- samba service can't restart: https://ubuntuforums.org/showthread.php?t=2398403

1. In windows browser, go to "https://192.168.xxx.xxx:10000" and login.
2. In VM, use "sudo smbpasswd -a username" and follow with password to add new samba user.
3. In VM, use "cd /etc/samba", and use "sudo cp smb.conf smb.bk" to backup samba config file.
4. In VM, use "sudo nano smb.conf" to edit, go to end of tile, type the following message and save it.:

[directory_display_name]
path = <path_to_share>
valid users = <username>
read only = no

If you want to share entire disk, you'll need to add, partition, format, mount, ... the drive. And go to path of "/media/<drive_name>".

5. In VM, use "sudo systemctl restart smbd.service" to restart samba. 
6. In VM, use "testparm" to check samba details. (make sure newly added settings are presented)
7. In windows file explorer, go to directory "\\192.168.xxx.xxx\<directory_display_name>", filled in user and password and now it can be accessed.

</details>

***

<details><summary>SECTION 6 - Tools for experiments</summary>

- https://askubuntu.com/questions/31618/how-can-i-find-my-hardware-details
- https://unix.stackexchange.com/questions/394362/whats-the-shortcut-to-delete-a-word-forward-in-a-unix-terminal
- https://www.tecmint.com/commands-to-collect-system-and-hardware-information-in-linux/
- https://unix.stackexchange.com/questions/106480/how-to-copy-files-from-one-machine-to-another-using-ssh
- https://askubuntu.com/questions/73160/how-do-i-find-the-amount-of-free-space-on-my-hard-drive

1. Generate large files: 
    "fallocate -l 10G this_is_a_test_file.img"
2. See file stats: 
    "stat this_is_a_test_file.img", or "file this_is_a_test_file.img".
3. Monitor server resource: 
    Use webmin webpage "Dashboard" to monitor.
4. Monitor CPU & Mem directly: 
    Use "sudo apt-get install htop", "htop" to monitor.
5. Monitor Disk Activity directly: 
    Use "sudo apt-get install iotop", "sudo iotop" to monitor.
6. Monitor Network directly: 
    Use "sudo apt-get install iftop", "sudo iftop" to monitor.
7. Multiple monitor: 
    Use "sudo apt-get install terminator", "sudo terminator" to monitor.
8. Monitor network traffic on server: 
    Use "sudo apt-get install tshark", "sudo tshark -i eth0 -w something.pcap" to capture all traffic on etho0 to a pcap file. Which can be transfered and later analyse with wireshark.
9. Check hardware info: 
    1. PCI
        Use "lspci" following with parameter ("-v", "-vv", "-nnk"). 
        Use "lspci -nnk | grep VGA -A1" to find graphics. 
        Use "lspci -v | grep -A7 -i "audio"" to find audio. 
        Use "lspci -nnk | grep net -A2" to find networking.
    2. Hardware Comprehensive Detail
       1. method 1
            Use "sudo lshw" to display comprehensive detail of hardware
            Use "sudo lshw | less" to display less info.
            Use "sudo lshw > hardwareInfo.txt" to export detail to file.
            Use "sudo lshw -short" to display summary info.
            Use "sudo lshw -html > x.html" to export info to html page.
       2. method 2
        Use "sudo apt-get install hardinfo" (most readable)
        Use "sudo hardinfo" on desktop iso to display info in GUI, on server iso to display info with benchmarking result.
        Use "sudo hardinfo > hardinfo.txt" to export full detail in txt. We can later open it up with "sudo nano hardinfo.txt".
    3. USB Connection
        Use "lsusb" to display usb connection info.
    4. CPU
        Use "lscpu" to display CPU info.
    5. Block Device (disk, partition, rom...)
        Use "lsblk" to display block device info.
        Use "lsblk -a" to display all devices.
    6. SCSI/SATA
        Use "lsscsi" to display SCSI/SATA devices info.
    7. File System
        Use "sudo fdisk -l" to display file system information.
10. Copy file with SSH connection
    In windows, without SSH connected, use "scp user@192.168.xxx.xxx:*.txt ./" to copy all text file at current directory.
11. Link/Mount directory
    Use "sudo apt-get install sshfs" to install sshfs.
    Use "sshfs user@192.168.xxx.xxx:/remote/dir /home/dir" to link/mount two directories.
    Use "fusermount -u /home/dir" to unlink/unmount directories.
12. Hard Drive Usage
    Use "df -h"

</details>

***

<details><summary>SECTION 7 - VM Details</summary>

1. NAS setup with Ubuntu 18.04 Desktop
    - User: user
    - Password: 123456
    - Webmin: https://192.168.161.131:10000
    - Directory: \\\\192.168.161.131\share

2. NAS setup with Ubuntu 18.04 live-server
    - User: user
    - Password: 123456
    - Webmin: https://192.168.161.133:10000
    - Directory: \\\\192.168.161.133\share

</details>

***

<details><summary>SECTION 8 - DDoS Simulation</summary>

1. Launch two VMs.
2. In windows, open cmd, ssh into both VMs at the same time.
3. In windows cmd VM1, use "sudo iftop" to monitor network activity.
4. In windows browser, open webmin dashboard page to monitor other activities at the same time.
5. In windows cmd new tab, use "ping -t 192.168.xxx.xxx" to ping VM1 continuously.
6. In windows cmd VM2, use multiple "sudo hping3 -1 -d 1000 --flood 192.168.xxx.xxx" to start DDoSing.
7. In windows cmd new tab and webmin webpage, monitor how stats varies.
8. In windows cmd VM2, use "sudo kill PID1 PID2 PID3 ..." to kill all DDoS processes.

</details>