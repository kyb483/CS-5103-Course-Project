import string
import unittest


class All_Count:
    def __init__(self, filename):              
        self.WordCount = None
        self.LineCount = None
        self.CharCount = None
        self.New_word =  None
        
        self.get_counts(filename)
    def word_count(self, filename):
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

        self.WordCount = counts
        print("\nWord count: ", self.WordCount)
        print("\n-----------------")

    def line_count(self, filename):
        text_file = open(filename, "r")
        count = len(text_file.readlines())
        text_file.close()
        self.LineCount = count
        print("\nLine count: ", self.LineCount)
        print("\n-----------------")

    def char_count(self, filename):
        text_file = open(filename, "r")
        data1 = text_file.read()
        text_file.close()
        count =  len(data1)
        self.CharCount = count
        print("\nCharacter count: ", self.CharCount)
        print("\n-----------------")
       
    def get_counts(self,filename):
        self.word_count(filename)
        self.line_count(filename)
        self.char_count(filename)
        self.word_replace(filename)

    def word_replace(self,filename):
        text_file = open(filename, "r")
        data1 = text_file.read()
        text_file.close()
        for punctuation in string.punctuation:
            data1 = data1.replace(punctuation, '')
        new_word = []
        words = str.split(data1)
        o_word = "you"
        n_word = "hello"
        print(words)
        for word in words:
            if word.lower() == o_word:
                word=word.replace(o_word,n_word)
                new_word.append(word)
            else:
                new_word.append(word)
        print(new_word)
        self.New_word = new_word 



    





class TestWordCount(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dict = All_Count('test1.txt')
        

    def test_word_present1(self):
        self.assertIn("the", self.dict.WordCount.keys(), "Word not in count")
    def test_word_present2(self):
        self.assertIn("look", self.dict.WordCount.keys(), "Word not in count")
    
    def test_word_count1(self):
        self.assertEqual(self.dict.WordCount.get("the"), 3, "Count is not correct")
    def test_word_count2(self):
        self.assertEqual(self.dict.WordCount.get("way"), 3, "Count is not correct")

    def test_line_count1(self):
        self.assertEqual(self.dict.LineCount, 6, "Count is not correct")
    def test_line_count2(self):
        self.assertEqual(self.dict.LineCount, 10, "Count is not correct")
    
    def test_char_count1(self):
        self.assertEqual(self.dict.CharCount, 521, "Count is not correct")
    def test_char_count2(self):
        self.assertEqual(self.dict.CharCount, 1000, "Count is not correct")
    
    def test_new_word_present1(self):
        self.assertIn("hello", self.dict.New_word, "Word not in String")
    def test_new_word_present2(self):
        self.assertIn("hotel", self.dict.New_word, "Word not in String")



unittest.main()