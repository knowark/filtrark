import unittest

from filtrark.string_parser import StringParser
from filtrark.operator_group import DefaultOperatorGroup


@unittest.skip("TEMP")
class TestStringParser(unittest.TestCase):
    """Tests for StringParser"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.operator_group = DefaultOperatorGroup() 
        self.parser = StringParser(self.operator_group)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_string_parser_object_creation(self):
        """Test something."""
        self.assertTrue(isinstance(self.parser, StringParser))

    def test_string_parser_parse_tuple(self):
        filter_tuple = ('field', '=', 99)
        expected = 'field = 99'
        result = self.parser._parse_term(filter_tuple)
        self.assertEqual(result, expected)

    def test_string_parser_parse_single_term(self):
        domain = [('field', '=', 7)]
        expected = 'field = 7'
        result = self.parser.parse(domain)
        self.assertEqual(result, expected)

    def test_string_parser_default_join(self):
        stack = ['field2 <> 8', 'field = 7']
        expected = 'field = 7 AND field2 <> 8'
        result = self.parser._default_join(stack)
        self.assertEqual(result, [expected])

    def test_string_parser_parse_multiple_terms(self):
        test_domains = [
            ([('field', '=', 7), ('field2', '!=', 8)],
             'field = 7 AND field2 <> 8'),
            ([('field', '=', 7), ('field2', '!=', 8), ('field3', '>=', 9)],
             'field = 7 AND field2 <> 8 AND field3 >= 9'),
            (['|', ('field', '=', 7), ('field2', '!=', 8), ('field3', '>=', 9)],
             'field = 7 OR field2 <> 8 AND field3 >= 9'),
            (['|', ('field', '=', 7),
              '!', ('field2', '!=', 8), ('field3', '>=', 9)],
             'field = 7 OR NOT field2 <> 8 AND field3 >= 9'),
            (['!', ('field', '=', 7)], 'NOT field = 7'),
        ]

        for test_domain in test_domains:
            result = self.parser.parse(test_domain[0])
            expected = test_domain[1]
            self.assertEqual(result, expected)
