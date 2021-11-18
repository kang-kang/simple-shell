import os
import time

def tree(d='/'):
    p = d
    for i in os.listdir(d):
        if d != '/':
            fn = d + '/' + i
        else:
            fn = d + i
        stat = os.stat(fn)
        size = stat[6]
        mtime = time.localtime(stat[8])
        if stat[0] == 0x4000:
            tree(fn)
        else:
            print('{:6d} {:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} {}'.format(
            size,
            mtime[0],
            mtime[1],
            mtime[2],
            mtime[3],
            mtime[4],
            mtime[5],
            fn,
            ))
