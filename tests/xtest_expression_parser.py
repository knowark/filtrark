# import unittest

# from filtrark.filtrark import Filtrark
# from filtrark.operator_group import DefaultOperatorGroup


# class TestFiltrark(unittest.TestCase):
#     """Tests for `filtrark` package."""

#     def setUp(self):
#         """Set up test fixtures, if any."""
#         self.operator_group = DefaultOperatorGroup() 
#         self.filtrark = Filtrark(self.operator_group)

#     def tearDown(self):
#         """Tear down test fixtures, if any."""

#     def test_filtrark_object_creation(self):
#         """Test something."""
#         self.assertTrue(isinstance(self.filtrark, Filtrark))

#     def test_filtrark_parse_tuple(self):
#         filter_tuple = ('field', '=', 99)
#         expected = 'field = 99'
#         result = self.filtrark._parse_term(filter_tuple)
#         self.assertEqual(result, expected)

#     def test_filtrark_parse_single_term(self):
#         domain = [('field', '=', 7)]
#         expected = 'field = 7'
#         result = self.filtrark.string(domain)
#         self.assertEqual(result, expected)

#     def xtest_filtrark_default_join(self):
#         stack = ['field2 <> 8', 'field = 7']
#         expected = 'field = 7 AND field2 <> 8'
#         result = self.filtrark._default_join(stack)
#         self.assertEqual(result, [expected])

#     def xtest_filtrark_parse_multiple_terms(self):
#         test_domains = [
#             ([('field', '=', 7), ('field2', '!=', 8)],
#              'field = 7 AND field2 <> 8'),
#             ([('field', '=', 7), ('field2', '!=', 8), ('field3', '>=', 9)],
#              'field = 7 AND field2 <> 8 AND field3 >= 9'),
#             (['|', ('field', '=', 7), ('field2', '!=', 8), ('field3', '>=', 9)],
#              'field = 7 OR field2 <> 8 AND field3 >= 9'),
#             (['|', ('field', '=', 7),
#               '!', ('field2', '!=', 8), ('field3', '>=', 9)],
#              'field = 7 OR NOT field2 <> 8 AND field3 >= 9'),
#             (['!', ('field', '=', 7)], 'NOT field = 7'),
#         ]

#         for test_domain in test_domains:
#             result = self.filtrark.parse(test_domain[0])
#             expected = test_domain[1]
#             self.assertEqual(result, expected)
