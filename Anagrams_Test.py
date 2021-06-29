import pytest
import Anagrams as Anagram

def test_Sanitize():
  word = "hola"
  result = "['a', 'h', 'l', 'o']"
  assert Anagram.Sanitize(word) == result
