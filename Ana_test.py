import pytest
import Ana as a 




def test_ana_1():
   lst = ['Hazelton', 'Hazleton']
   for i in lst:
      a.ana(i)
   assert a.dic ==  { "['H', 'a', 'e', 'l', 'n', 'o', 't', 'z']": ['Hazelton', 'Hazleton']}


