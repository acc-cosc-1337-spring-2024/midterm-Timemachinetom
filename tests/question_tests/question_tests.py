#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, use_local_variable
from src.question_b.question_b import get_day_of_week

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