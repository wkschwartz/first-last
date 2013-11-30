first-last
==========

Demonstration of using regular expressions to split first names from last
names. The main thing to know is that regular expressions are strings that
express patterns against which other strings are matched.

Download
--------

To use the provided `names` module in your project, download `names.py` (and
optionally `test_names.py`, which contains the unit tests for `names`). You can
do this with git by running

```bash
    $ git clone https://github.com/wkschwartz/first-last
```

or by going to https://github.com/wkschwartz/first-last/archive/master.zip.

Usage
-----

Copy the `names.py` file into your project and the `test_names.py` file into
your project's tests. The module `names` provides the function `split_name`. Its
input is a string containing a name. It returns a two-tuple of strings
containing the first and last names respectively. For example if you have a
string (either byte strings or Unicode strings) called ``name``, you can write

```python
    from names import split_name
    first_name, last_name = split_name(name)
```

Testing
-------

This code has been tested on Python 2.7.6 and Python 3.3.3, both on Mac OS X
10.8. To run the tests on your system, run `test_names.py` from the command
line, like so:

```bash
    $ python test_names.py
```

License
-------

See the `LICENSE` file.