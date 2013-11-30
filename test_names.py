#! /usr/bin/env python
# ~*~ encoding: utf-8 ~*~
import unittest

from names import split_names


class TestSplitNames(unittest.TestCase):

	"Test the ``names.split_names`` function to ensure it works as intended."

	# The test data below is called a "data fixture" because it's fixed ahead of
	# when the test is run. Constant values like the ones below usually get
	# all-caps names.
	NAMES = (u"William Schwartz", # Strings prepended with ``u`` are Unicdoe.
			  "Jillian Foley", # Strings without ``u`` prepended are raw bytes.
			 u"bLeRdiE flAdElStEiN",
			 u"Pred_alpop Gormer-tin",
			 u"James Van Der Beek",
			 u"Daniel O'Hanlon",
			 u"Piña colada",
			 u"colada Piña",
	)

	EXPECTED = ((u"William",    u"Schwartz"),
				( "Jillian",     "Foley"),
				(u"bLeRdiE",    u"flAdElStEiN"),
				(u"Pred_alpop", u"Gormer-tin"),
				(u"James",      u"Van Der Beek"),
				(u"Daniel",     u"O'Hanlon"),
				(u"Piña",       u"colada"),
				(u"colada",     u"Piña"),
	)

	def test_split_names(self):
		"Test that input matches the expected output."
		self.assertEqual(sorted(split_names(self.NAMES)), sorted(self.EXPECTED))

	def test_bad_input(self):
		"Test ``split_names`` responds with appropriate errors to bad input."
		for bad_names in 1, 1.0, 1j, [1, 1.0], {1: 1.0}:
			# Check that ``list(split_names(bad_names))`` raises a
			# ``TypeError``. We call ``list`` to force the generator to start
			# running.
			self.assertRaises(TypeError, list, split_names, bad_names)

	def test_None_on_non_matching_strings(self):
		"Test that we yield ``None`` on non-matching strings."
		# Sorry, Yao Ming.
		names = (u"姚明", "Sam Jones", "1234")
		self.assertEqual(list(split_names(names)), [None, ('Sam', 'Jones'), None])


if __name__ == '__main__':
	unittest.main()
