import os
import time


MONTH = ('', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
WEEKDAY = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')


def get_mode(filename):
    try:
        return os.stat(filename)[0]
    except OSError:
        return 0


def get_stat(filename):
    try:
        return os.stat(filename)
    except OSError:
        return (0,) * 10


def mode_exists(mode):
    return mode & 0xc000 != 0


def mode_isdir(mode):
    return mode & 0x4000 != 0


def mode_isfile(mode):
    return mode & 0x8000 != 0


def print_long(filenames):
    """Prints detailed information about each file passed in."""
    for filename in filenames:
        stat = get_stat(filename)
        mode = stat[0]
        if mode_isdir(mode):
            mode_str = '/'
        else:
            mode_str = ''
        size = stat[6]
        mtime = stat[8]
        localtime = time.localtime(mtime)
        extra_str = ''
        if mtime == 0 and mode == 0:
            extra_str = ' <<< Weird Filename???'
        print('%6d %s %2d %02d:%02d %s%s%s' % (size, MONTH[localtime[1]],
              localtime[2], localtime[4], localtime[5], filename, mode_str, extra_str))


def ls(path='/'):
    print_long(os.listdir(path))


def cd(path):
    os.chdir(path)


def cat(filename):
    mode = get_mode(filename)
    if not mode_exists(mode):
        print("Cannot access '%s': No such file\n" %
                          filename)
        return False
    if not mode_isfile(mode):
        print("'%s': is not a file\n" % filename)
        return False
    with open(filename, 'r') as txtfile:
        for line in txtfile:
            print(line, end='')


def write(filename):
    content = []
    while True:
        try:
            line = input()
            content.append(line)
        except EOFError:
            print('exit')
            break
    with open(filename, 'w+') as txtfile:
        txtfile.write('\n'.join(content)+'\n')


def mkdir(target):
    mode = get_mode(target)
    if not mode_exists(mode):
        os.mkdir(target)
    else:
        print('%s already exists.' % target)

def pwd():
    print(os.getcwd())

def rm(filename):
    try:
        os.remove(filename)
    except:
        try:
            os.rmdir(filename)
        except:
            print('%s is not a file or directory.' % filename)

def run():
    while True:
        try:
            cmd_line = input('$ ')
            if cmd_line:
                cmd, *args = cmd_line.split()
                try:
                    eval(cmd)(*args)
                except NameError:
                    print('not such command')
        except EOFError:
            print('exit')
            break
        except KeyboardInterrupt:
            print('^C, use ^D to exit')
