# DE:NET
The DE:NET toolchain is a  scripting interface for hacking tools, with a suite of packages designed to transform your Raspberry Pi into a powerful hacking machine.

1. Network 
2. Operating systems
3. 125khz RFID 
4. NFC

And to add cherry on top you can program your own hacking scripts using build in `denet-cli`.
## Included Packages

## Installation

## Building Packages
To build packages using `denet-cli` run command `python denet make-package <suite_name> <package_name>`
This will result in a package inside `<project_root>/suites/<suite_name>/<package_name>` containing two files `<package_name>.py` and `<package_name>.run`

py file will contain script to run the hack, you should note that you have to use only system arguments and no inputs in between the scripts.

run file will include syntax to run the command 

sample.run
```
python3 package_name.py <Input_variable_1> <Input_variable_2> 
```

`<Input_variable_1>` and `<Input_variable_2>` are variable names which will be reflected in the GUI interface

