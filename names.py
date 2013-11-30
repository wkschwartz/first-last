import re


# A regular expression is a string like what you see below between the quote
# marks, and the ``re`` module interprets it as a pattern. Each regular
# expression describes a small program that takes another string as input and
# returns information about that string. See
# http://docs.python.org/library/re.html. The ``re`` module provides the
# ``compile`` function, which prepares regex patterns for use in searching input
# strings.
#
# We put an ``r`` before the string so that Python doesn't interpret the
# backslashes before the ``re`` module gets to see them. (E.g., ``\n`` means a
# newline character, so ``\n`` is a single character, not two as they appear in
# the source code.)
#
# The Unicode flag lets us handle words with accented characters.
FIRST_LAST = re.compile(r"(\w*)\s+((?:\w|\s|['-]){2,})", flags=re.UNICODE)


def split_names(names):
	'''Return iterable of ("First", "Last") tuples from  strings like "First Last".

	``names`` is a an iterable of strings. This function returns a generator
	over strings. When a non-matching string is encoutered, we yield ``None``.
	'''
	for name in names:
		match = FIRST_LAST.search(name)
		if match is None:
			yield None
		else:
			yield match.group(1), match.group(2)
