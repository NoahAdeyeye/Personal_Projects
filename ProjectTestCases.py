from DictsForCompSciProject import option1dict, option2dict, option3dict, option4dict
import WildeCard
import unittest

dict_1_ex = ("Soccer", "Northeast")
dict_2_ex = ("Action", "0-12")
dict_3_ex = ("Playstation", "Puzzle")
dict_4_ex = ("Country", "25+")

def test_dicts_in(self):
    if dict_1_ex in option1dict.values():
        return True
    else:
        return False
    if dict_2_ex in option2dict.values():
        return True
    else:
        return False
    if dict_3_ex in option3dict.values():
        return True
    else:
        return False
    if dict_4_ex in option4dict.values():
        return True
    else:
        return False
    
def test_dicts_out(self):
    if dict_1_ex not in option2dict.values() or option3dict.values() or option4dict.values():
        return True
    else:
        return False
    if dict_2_ex not in option1dict.values() or option3dict.values() or option4dict.values():
        return True
    else:
        return False
    if dict_3_ex not in option2dict.values() or option1dict.values() or option4dict.values():
        return True
    else:
        return False
    if dict_4_ex not in option2dict.values() or option3dict.values() or option1dict.values():
        return True
    else:
        return False

class WildeCardTestCases(unittest.TestCase):
    
    def test_dicti(self):
        self.assertTrue(test_dicts_in(self))
        
    def test_dicto(self):
        self.assertTrue(test_dicts_out(self))
   
if __name__ == '__main__' :
  unittest.main()
