import pytest
import Anagrams as Anagram

def test_Sanitize():
  word = "hola"
  result = "['a', 'h', 'l', 'o']"
  assert Anagram.sanitize(word) == result

def test_isAnagram():
    word1 = "romo"
    word2 = "moro"
    Anagram.check(word1)
    assert Anagram.check(word2) == True


