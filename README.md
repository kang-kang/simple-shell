# Simple Shell for MicroPython

Simple shell for MicroPython, tested at ESP32, should work on ESP8266.

Some codes are from https://github.com/dhylands/upy-shell .

# Usage
Ctrl-D(^D) to finish shell or input.
## Commands
### ls
list files

### cd <dir>
change dir

### cat <file>
show file content

### write <file>
create a text file, use ^D on new line to finish input, ^C to exit

### mkdir <dir>
make dir

### rm <path>
remove file or dir

### pwd
get current work dir

## Example
```python
>>> import shell
>>> shell.run()
$ ls
   137 Jan  4 33:34 boot.py
    18 Jan  4 33:34 webrepl_cfg.py
   233 Jan  1 07:02 main.py
  1138 Jan  1 07:10 sub_led.py
     0 Jan  4 55:18 my/
    17 Jan  5 21:28 abc
  2403 Jan  5 15:34 shell.py
$ write abc
foo
bar
^D
$ cat abc
foo
bar
$ cd my
```
