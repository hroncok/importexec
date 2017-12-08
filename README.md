Examine the files. Run the following to see the difference:

```console
$ python3 -c 'import foo.bar'
running foo/__init__.py
running foo/bar.py
will import foo
foo.__file__ is .../importexec/foo/__init__.py
foo.thing is 0
$ python3 foo/bar.py 
running foo/bar.py
will import foo
running foo/foo.py
foo.__file__ is .../importexec/foo/foo.py
foo.thing is 1
```

Files in this repo are Public Domain.
