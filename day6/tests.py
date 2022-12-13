import unittest
import main


class TestExamples(unittest.TestCase):

    def test_getstartofpackage(self):
        self.assertEqual(main.getposition("bvwbjplbgvbhsrlpgdmjqwftvncz", 4), 5)
        self.assertEqual(main.getposition("nppdvjthqldpwncqszvftbrmjlhg", 4), 6)
        self.assertEqual(main.getposition("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4), 10)
        self.assertEqual(main.getposition("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4), 11)
        self.assertEqual(main.getposition("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4), 7)

    def test_getstartofmessage(self):
        self.assertEqual(main.getposition("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14), 19)
        self.assertEqual(main.getposition("bvwbjplbgvbhsrlpgdmjqwftvncz", 14), 23)
        self.assertEqual(main.getposition("nppdvjthqldpwncqszvftbrmjlhg", 14), 23)
        self.assertEqual(main.getposition("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14), 29)
        self.assertEqual(main.getposition("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14), 26)


if __name__ == '__main__':
    unittest.main()
