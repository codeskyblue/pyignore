pyignore
==========================

Parse file like `.gitignore`.
I write this because, there are no good ignore parsers lib for python.

## Usage
    ign = Ignore(['foo/', '/*/*.pyc', '*.txt'])
    print ign
    names = ['/log/foo/', '/foo', '/bar/', '/x.pyc', '/foo/a.pyc', '/foo/a.py', '/foo/a.txt']
    print 'names', names
    print ign.exclude(names)
	print ign.filter(names)

Licence under [MIT](LICENSE)
