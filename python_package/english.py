"""English dictionary module."""
from typing import Dict, List, Optional, Union

from enchant import Dict as Spell
from PyDictionary import PyDictionary

from .utils.io import CaptureStdStreams

__all__ = ['English']


class English:
    """English dictionary.

    Attributes:
        TypeMeanings: Type of the returned meanings from `meanings()`.
        TypeDefinition: Type of the returned definition from `define()`.

    """

    # https://mypy.readthedocs.io/en/latest/cheat_sheet.html
    TypeMeanings = Dict[str, List[str]]
    TypeDefinition = Dict[str, Union[List[str], TypeMeanings]]

    def __init__(self):
        # type: () -> None
        """Initialize the dictionaries."""
        self._spell = Spell('en_US')
        self._dictionary = PyDictionary('html.parser')

    def check(self, word):
        # type: (str) -> bool
        """Check if a word is in the English dictionary.

        Args:
            word: The word to check.

        Returns:
            True if it is and False otherwise.

        """
        out = self._spell.check(word)  # type: bool
        return out

    def suggest(self, misspelled_word):
        # type: (str) -> List[str]
        """Suggest corrections for a misspelled word.

        Args:
            misspelled_word: The word to use.

        Returns:
            A list of suggestions.

        """
        out = self._spell.suggest(misspelled_word)  # type: List[str]
        return out

    def meanings(self, word):
        # type: (str) -> English.TypeMeanings
        """Get the meanings of a word if they exists.

        Args:
            word: The word to use.

        Returns:
            A list of meanings.

        """
        with CaptureStdStreams():
            out = self._dictionary.meaning(
                word)  # type: Optional[English.TypeMeanings]
        if out is None:
            return {}
        return out

    def synonyms(self, word):
        # type: (str) -> List[str]
        """Get the synonyms of a word if they exists.

        Args:
            word: The word to use.

        Returns:
            A list of synonyms.

        """
        with CaptureStdStreams():
            out = self._dictionary.synonym(word)  # type: Optional[List[str]]
        if out is None:
            return []
        return out

    def antonyms(self, word):
        # type: (str) -> List[str]
        """Get the antonyms of a word if they exists.

        Args:
            word: The word to use.

        Returns:
            A list of synonyms.

        """
        with CaptureStdStreams():
            out = self._dictionary.antonym(word)  # type: Optional[List[str]]
        if out is None:
            return []
        return out

    def define(self, word):
        # type: (str) -> English.TypeDefinition
        """Define a word and find its synonyms and antonyms.

        Args:
            word: The word to define.

        Returns:
            A dict of meanings, synonyms and antonyms.

        """
        out = {
            'Meanings': self.meanings(word),
            'Synonyms': self.synonyms(word),
            'Antonyms': self.antonyms(word),
        }  # type: English.TypeDefinition
        # we have to put the above type comment because mypy cannot
        # infer the type correctly. Instead, it infers
        # `Dict[str, Collection[str]]`. However, we can do:
        # `return {...}` and it would infer it correctly.
        return out
