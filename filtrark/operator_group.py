from typing import Dict, Callable, Union
from abc import ABC, abstractmethod

ComparisonExpression = Callable[
    [str, Union[str, int, float]], Union[bool, str]]

BinaryLogicalExpression = Callable[
    [ComparisonExpression, ComparisonExpression], Union[bool, str]]

UnaryLogicalExpression = Callable[
    [ComparisonExpression], Union[bool, str]]


class OperatorGroup(ABC):

    @abstractmethod
    def comparison_operators(self) -> Dict[str, ComparisonExpression]:
        """Return the group's binary operators"""

    @abstractmethod
    def unary_operators(self) -> Dict[str, BinaryLogicalExpression]:
        """Return the group's binary operators"""

    @abstractmethod
    def binary_operators(self) -> Dict[str, UnaryLogicalExpression]:
        """Return the group's binary operators"""


class SqlOperatorGroup(OperatorGroup):

    def __init__(self):
        self.comparison_dict = {
            '=': lambda x, y:  '='.join(str(x), str(y)),
            '!=': lambda x, y: '!='.join(str(x), str(y)),
            '<=': lambda x, y: '<='.join(str(x), str(y)),
            '<': lambda x, y: '<'.join(str(x), str(y)),
            '>': lambda x, y: '>'.join(str(x), str(y)),
            '>=': lambda x, y: '>='.join(str(x), str(y)),
            'in': lambda x, y: 'in'.join(str(x), str(y)),
        }

        self.binary_dict = {
            '&': lambda a, b: a + ' AND ' + b,
            '|': lambda a, b: a + ' OR ' + b}

        self.unary_dict = {
            '!': lambda a: 'NOT ' + a}

    def comparison_operators(self) -> Dict[str, ComparisonExpression]:
        """Return the group's binary operators"""
        return self.comparison_dict

    def unary_operators(self) -> Dict[str, BinaryLogicalExpression]:
        """Return the group's binary operators"""
        return self.binary_dict

    def binary_operators(self) -> Dict[str, UnaryLogicalExpression]:
        """Return the group's binary operators"""
        return self.unary_dict
