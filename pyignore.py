#!/usr/bin/env python
# coding: utf-8
#

__version__ = '0.1'

import fnmatch
import os

class Ignore(object):
    def __init__(self, filename_or_lines):
        if isinstance(filename_or_lines, basestring):
            with open(filename_or_lines) as file:
                lines = file.readlines()
        else:
            assert isinstance(filename_or_lines, list)
            lines = filename_or_lines

        self._pats = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            self._pats.append(line)

    def __str__(self):
        return 'ignore: ' + str(self._pats)

    def match(self, name):
        base = os.path.basename(name)

        for pat in self._pats:
            if fnmatch.fnmatch(name, pat):
                return True
            if base and fnmatch.fnmatch(base, pat):
                return True
            if name.endswith('/'+pat):
                return True

    def filter(self, names):
        ''' Return the subset of the list NAMES that match PAT '''
        return [n for n in names if self.match(n)]

    def exclude(self, names):
        return [n for n in names if not self.match(n)]

if __name__ == '__main__':
    # test
    ign = Ignore(['foo/', '/*/*.pyc', '*.txt'])
    print ign
    names = ['/log/foo/', '/foo', '/bar/', '/x.pyc', '/foo/a.pyc', '/foo/a.py', '/foo/a.txt']
    print 'names', names
    print ign.exclude(names)

    import os
    ign = Ignore('.gitignore')
    print '\n'.join(ign.exclude(os.listdir('.')))
