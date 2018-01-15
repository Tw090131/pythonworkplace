import unittest
from name_function import get_formatted_name

#自定义类继承unittest。testcase
class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name = get_formatted_name('zhang','zhiwei')
		self.assertEqual(formatted_name,'Zhang Zhiwei')

unittest.main()