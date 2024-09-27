"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""

import unittest

def solution(a, b):
    return a.endswith(b)

class TestSolution(unittest.TestCase):
    
    def test_fixed_true(self):
        # Test cases where the function should return True
        self.assertTrue(solution("samurai", "ai"))
        self.assertTrue(solution("ninja", "ja"))
        self.assertTrue(solution("sensei", "i"))
        self.assertTrue(solution("abc", "abc"))
        self.assertTrue(solution("abcabc", "bc"))
        self.assertTrue(solution("fails", "ails"))
    
    def test_fixed_false(self):
        # Test cases where the function should return False
        self.assertFalse(solution("sumo", "omo"))
        self.assertFalse(solution("samurai", "ra"))
        self.assertFalse(solution("abc", "abcd"))
        self.assertFalse(solution("ails", "fails"))
        self.assertFalse(solution("this", "fails"))
        self.assertFalse(solution("spam", "eggs"))

if __name__ == '__main__':
    unittest.main()
