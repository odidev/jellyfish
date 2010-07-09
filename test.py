import unittest
import strfry


class StrfryTestCase(unittest.TestCase):

    def test_jaro_winkler(self):
        cases = [("DIXON", "DICKSONX", 0.8133),
                 ("DIXON", "dicksonx", 0.8133),
                 ("MARTHA", "MARHTA", 0.9611),
                 ("DWAYNE", "DUANE", 0.84),
                 ]

        for (s1, s2, value) in cases:
            self.assertAlmostEqual(strfry.jaro_winkler(s1, s2), value,
                                   places=4)

    def test_jaro_winkler_case_sensitive(self):
        self.assertAlmostEqual(
            strfry.jaro_winkler("DIXON", "dicksonx", False), 0, places=4)
        self.assertAlmostEqual(
            strfry.jaro_winkler("DIXON", "dicksonx", ignore_case=False),
            0, places=4)

if __name__ == '__main__':
    unittest.main()
