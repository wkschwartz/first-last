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

    $ git clone https://github.com/wkschwartz/first-last

or by going to https://github.com/wkschwartz/first-last/archive/master.zip.

Usage
-----

The module `names` provides the function `split_names`. Its input is any
iterable (some `y` for which you can write `for x in y`) of strings. It is a
generator, which means it too is iterable. For example if you have a list
containing your names as strings (either byte strings or Unicode strings), you
can write

    names = list(split_names(names))

Testing
-------

This code has been tested on Python 2.7.6 and Python 3.3.3, both on Mac OS X
10.8. To run the tests on your system, run `test_names.py` from the command
line, like so:

    $ python test_names.py

License
-------

See the `LICENSE` file.