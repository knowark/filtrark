import inspect
import unittest

from filtrark.operator_group import OperatorGroup, SqlOperatorGroup


class TestOperatorGroup(unittest.TestCase):
    """Tests for `filtrark` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_operator_group_interface(self):
        self.assertTrue(
            inspect.isabstract(OperatorGroup))

    def test_sql_operator_group(self):
        self.assertTrue(issubclass(SqlOperatorGroup, OperatorGroup))

    def test_sql_operator_group_implementation(self):
        sql_operator_group = SqlOperatorGroup()

        self.assertTrue(sql_operator_group.comparison_operators())
        self.assertTrue(sql_operator_group.binary_operators())
        self.assertTrue(sql_operator_group.unary_operators())
