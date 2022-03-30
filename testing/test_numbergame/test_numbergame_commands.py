import unittest


class Test_WHAT_TO_TEST(unittest.TestCase):
    def TESTMETHODE1(self):
        self.assertEqual("foo".upper(), "FOO")

    def TESTMETHODE2(self):
        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    unittest.main()


# HOW TO RUN THE TEST:
# python -m unittest testing/test_GAME.test_FILE.py
