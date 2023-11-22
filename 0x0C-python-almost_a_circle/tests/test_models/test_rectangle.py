#!/usr/bin/python3
"""testing rectangle module"""


import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
from io import StringIO
class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        r1 = Rectangle(4, 6)
        #r1 = Rectangle(2, 3, 2, 2)
        #correct_output_r1 = "  ##\n  ##\n  ##"
        correct_output_r1 = "####\n####\n####\n####\n####\n####\n"

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), correct_output_r1)
        
        r2 = Rectangle(2, 2)
        #r2 = Rectangle(3, 2, 1, 0)
        #correct_output = " ###\n ###"
        correct_output = "##\n##\n"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), correct_output)
    
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        correct_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), correct_output)

        r2 = Rectangle(5, 5, 1)
        correct_output = "[Rectangle] ({}) 1/0 - 5/5".format(r2.id)
        self.assertEqual(str(r2), correct_output)
    
    def test_update_1(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
    
    def test_update_one_1(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_two(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_three(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_four(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_five(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
    def test_update_hgt(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_hgt_1(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

#    def test_update_hgt_2(self):
 #       r1 = Rectangle(10, 10, 10, 10)
  #      r1.update(width=1, x=2)
   #     self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")

    #def test_update_hgt_3(self):
     #   r1 = Rectangle(10, 10, 10, 10)
      #  r1.update(y=1, width=2, x=3, id=89)
       # self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

   # def test_update_hgt_4(self):
   #     r1 = Rectangle(89, 10, 10, 10)
    #    r1.update(x=1, height=2, y=3, width=4)
     #   self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")


if __name__ == '__main__':
    unittest.main()