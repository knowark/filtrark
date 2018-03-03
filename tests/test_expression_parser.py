import unittest
from unittest.mock import Mock

from filtrark.expression_parser import ExpressionParser
from filtrark.operator_group import DefaultOperatorGroup


class TestExpressionParser(unittest.TestCase):
    """Tests for `filtrark` package."""

    def setUp(self):
        self.parser = ExpressionParser()

    def test_filtrark_object_creation(self):
        self.assertTrue(isinstance(self.parser, ExpressionParser))

    def test_filtrark_parse_tuple(self):
        filter_tuple = ('field', '=', 99)

        def expected(obj):
            return getattr(obj, 'field') == 99

        mockObject = Mock()
        mockObject.field = 99

        function = self.parser._parse_term(filter_tuple)

        self.assertTrue(callable(function))
        self.assertTrue(function(mockObject))
        self.assertEqual(function(mockObject), expected(mockObject))

        mockObject.field = 87
        self.assertFalse(function(mockObject))

    def test_filtrark_parse_single_term(self):
        domain = [('field', '=', 7)]
        expected = 'field = 7'

        def expected(obj):
            return getattr(obj, 'field') == 7

        mockObject = Mock()
        mockObject.field = 7

        function = self.parser.parse(domain)

        self.assertTrue(callable(function))
        self.assertTrue(function(mockObject))
        self.assertEqual(function(mockObject), expected(mockObject))

        mockObject.field = 5
        self.assertFalse(function(mockObject))

    # def test_filtrark_default_join(self):
    #     stack = ['field2 <> 8', 'field = 7']
    #     expected = 'field = 7 AND field2 <> 8'
    #     result = self.filtrark._default_join(stack)
    #     self.assertEqual(result, [expected])

    # def test_filtrark_parse_multiple_terms(self):
    #     test_domains = [
    #         ([('field', '=', 7), ('field2', '!=', 8)],
    #          'field = 7 AND field2 <> 8'),
    #         ([('field', '=', 7), ('field2', '!=', 8),
    #           ('field3', '>=', 9)],
    #             'field = 7 AND field2 <> 8 AND field3 >= 9'),
    #         (['|', ('field', '=', 7), ('field2', '!=', 8),
    #           ('field3', '>=', 9)],
    #             'field = 7 OR field2 <> 8 AND field3 >= 9'),
    #         (['|', ('field', '=', 7),
    #           '!', ('field2', '!=', 8), ('field3', '>=', 9)],
    #          'field = 7 OR NOT field2 <> 8 AND field3 >= 9'),
    #         (['!', ('field', '=', 7)], 'NOT field = 7'),
    #     ]

    #     for test_domain in test_domains:
    #         result = self.filtrark.parse(test_domain[0])
    #         expected = test_domain[1]
    #         self.assertEqual(result, expected)
