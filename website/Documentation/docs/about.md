# About
DE:NET is a toolchain scripting interface for hacking tools which includes multiple suite and packages to make your raspberry pi into an ultimate hacking machine able to hack 

1. Network 
2. Operating systems
3. 125khz RFID 
4. NFC

And to add cherry on top you can program your own hacking scripts using build in `denet-cli`.
## Included Packages

### Network

#### Sniffing:
Sniffing refers to the process of capturing and analyzing network data packets as they are transmitted over a network. This allows network administrators to monitor network activity and identify any potential problems or security threats. However, it can also be used for malicious purposes, such as stealing sensitive information by intercepting network traffic.

#### Spoofing: 
Spoofing involves altering the source address of a network packet to make it appear as if it came from a different source. This technique can be used for malicious purposes, such as launching a denial-of-service attack, sending spam emails, or redirecting traffic to a fake website in order to steal sensitive information.

#### Wifi Password Cracking: 
This involves attempting to gain unauthorized access to a wifi network by guessing the network password. This is often accomplished through a dictionary attack, where a computer program automatically tries every word in a dictionary as the password until the correct one is found. Wifi password cracking is illegal and unethical and can result in serious consequences for the individual attempting to do so.

#### Finding Devices IP in a Network: 
Every device connected to a network is assigned a unique IP address, which allows it to communicate with other devices on the network. Network administrators can use tools such as network scanning software or the command line interface to find all the IP addresses of devices on their network.

#### Changing the MAC Address: 
The MAC (Media Access Control) address is a unique identifier assigned to each device on a network. Changing the MAC address of a device, also known as MAC spoofing, can be done for a variety of reasons, such as bypassing network security measures, making it appear as if a device is a different type of device, or masking the identity of a device. However, changing the MAC address of a device can sometimes have unintended consequences and may not always be possible, depending on the device and network configuration.

### Third Party Tools
Two Third party tools are required `Python3.9.2 or above` and `ZeroTier`

ZeroTier is required to dynamicaly make peer to peer connection between raspberry pi and user computer to gain complete axis to raspberry pi from anywhere and from any network and to access web GUI interface 

## Installation


## Building Packages
To build packages using `denet-cli` run command `python denet make-package <suite_name> <package_name>`
This will reselt in a package inside `<project_root>/suites/<suite_name>/<package_name>` containing two files `<package_name>.py` and `<package_name>.run`

py file will contain script to run the hack, you should note that you have to use only system arguments and no inputs in between the scripts.

run file will include syntax to run the command 

sample.run
```
python3 package_name.py <Input_variable_1> <Input_variable_2> 
```

`<Input_variable_1>` and `<Input_variable_2>` are variable names which will be reflected in the GUI interface