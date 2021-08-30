class StringCharacterTree:
	"""Represents a set of strings phrases via a tree of characters."""
	root = None

	def parse_string(self, text, seperator = '\n', trimWhiteSpace = True):
		"""Imports a string into the StringCharacterTree, phrases are seperated by the seperator character."""
		phrases = text.split(seperator)
		root = StringCharacterNode()

		for current_phrase in phrases:
			if trimWhiteSpace:
				current_phrase.strip()

			#Starting at the root, add each character sequentially down the tree

		#TODO

	def to_string(self):
		text = ""
		#TODO
		return text

class StringCharacterNode:
	"""A node of StringCharacterTree, contains a dictionary of its children and a flag for end of phrase."""
	character = '\0'
	children = {}			#Dictionary of child nodes, keyed by their character
	validPhraseEnd = False