#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, use_local_variable
from src.question_b.question_b import get_day_of_week
from src.question_c.question_c import reverse_string
from src.question_d.question_d import get_random_number

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    #def test_use_local_variable(self):
        #self.assertEqual (100, use_local_variable(num))
    
    def test_get_day_of_week_1(self):
        self.assertEqual ("Invalid number", get_day_of_week(0))

    def test_get_day_of_week_2(self):
        self.assertEqual ("Monday", get_day_of_week(1))

    def test_get_day_of_week_3(self):
        self.assertEqual ("Tuesday", get_day_of_week(2))

    def test_get_day_of_week_4(self):
        self.assertEqual ("Wednesday", get_day_of_week(3))
    
    def test_get_day_of_week_5(self):
        self.assertEqual ("Invalid number", get_day_of_week(8))
    
    def test_reverse_string_1(self):
        self.assertEqual ("dlrow olleh", reverse_string("hello world"))
    
    def test_reverse_string_2(self):
        self.assertEqual ("olleh", reverse_string("hello"))

    def test_get_random_number(self):
        self.assertIn (get_random_number(), range(1,6))