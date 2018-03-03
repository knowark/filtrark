import inspect
import unittest

from filtrark.operator_group import (
    OperatorGroup, SqlOperatorGroup, ExpressionOperatorGroup)


@unittest.skip("TEMP")
class TestOperatorGroup(unittest.TestCase):
    """Tests for `filtrark` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def test_operator_group_interface(self):
        self.assertTrue(
            inspect.isabstract(OperatorGroup))

    def test_operator_group_methods(self):
        abstract_methods = OperatorGroup.__abstractmethods__
        self.assertIn('comparison_operators', abstract_methods)
        self.assertIn('unary_operators', abstract_methods)
        self.assertIn('binary_operators', abstract_methods)


@unittest.skip("TEMP")
class TestSqlOperatorGroup(unittest.TestCase):
    def setUp(self):
        self.sql_operator_group = SqlOperatorGroup()

    def test_sql_operator_group(self):
        self.assertTrue(issubclass(SqlOperatorGroup, OperatorGroup))

    def test_sql_operator_group_implementation(self):
        self.assertTrue(self.sql_operator_group.comparison_operators())
        self.assertTrue(self.sql_operator_group.binary_operators())
        self.assertTrue(self.sql_operator_group.unary_operators())


@unittest.skip("TEMP")
class TestExpressionOperatorGroup(unittest.TestCase):
    def setUp(self):
        self.expression_operator_group = ExpressionOperatorGroup()

    def test_expression_operator_group(self):
        self.assertTrue(issubclass(ExpressionOperatorGroup, OperatorGroup))

    def test_expression_operator_group_implementation(self):
        self.assertTrue(
            self.expression_operator_group.comparison_operators())
        self.assertTrue(
            self.expression_operator_group.binary_operators())
        self.assertTrue(
            self.expression_operator_group.unary_operators())
