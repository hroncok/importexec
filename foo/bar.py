print('running foo/bar.py')
print('will import foo')
import foo
print('foo.__file__ is', foo.__file__)
print('foo.thing is', foo.thing)
if hasattr(foo, 'foo'):
    print('foo.foo exists')
    print('foo.foo.thing is', foo.foo.thing)
else:
    print('foo.foo does not exist')
