import string
import unittest


def word_count(filename):
    text_file = open(filename, "r")
    data1 = text_file.read()
    text_file.close()
   
    counts = dict()
    words = str.split(data1)

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count('test1.txt'))



class TestWordCount(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dict = word_count('test1.txt')

    def test_word_present1(self):
        self.assertIn("the", self.dict.keys(), "Word not in count")
    def test_word_present2(self):
        self.assertIn("look", self.dict.keys(), "Word not in count")
    
    def test_word_count1(self):
        self.assertEqual(self.dict.get("the"), 3, "Count is not correct")
    def test_word_count2(self):
        self.assertEqual(self.dict.get("way"), 3, "Count is not correct")




unittest.main()