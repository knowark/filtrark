from typing import NewType, List, Tuple, Union, Callable
from filtrark.operator_group import OperatorGroup

TermTuple = NewType('TermTuple', Tuple[str, str, Union[str, float]])


class ExpressionParser:
    def __init__(self) -> None:
        def expected(obj): getattr(obj, 'field') == 99
        self.comparison_dict = {
            '=': lambda field, value: (
                lambda obj: getattr(obj, field) == value),
            '!=': lambda x, y: ' <> '.join([str(x), str(y)]),
            '<=': lambda x, y: ' <= '.join([str(x), str(y)]),
            '<': lambda x, y: ' < '.join([str(x), str(y)]),
            '>': lambda x, y: ' > '.join([str(x), str(y)]),
            '>=': lambda x, y: ' >= '.join([str(x), str(y)]),
            'in': lambda x, y: ' in '.join([str(x), str(y)])}

        self.binary_dict = {
            '&': lambda a, b: a + ' AND ' + b,
            '|': lambda a, b: a + ' OR ' + b}

        self.unary_dict = {
            '!': lambda a: 'NOT ' + a}

    def parse(self, domain: List[Union[str, TermTuple]]) -> Callable:
        stack = []  # type: List[Callable]
        for item in list(reversed(domain)):
            if item in self.binary_dict:
                first_operand = stack.pop()
                second_operand = stack.pop()
                string_term = str(
                    self.binary_dict[str(item)](
                        first_operand, second_operand))
                stack.append(string_term)
            elif item in self.unary_dict:
                operand = stack.pop()
                stack.append(
                    str(self.unary_dict[str(item)](
                        operand)))

            stack = self._default_join(stack)

            if isinstance(item, (list, tuple)):
                result = self._parse_term(item)
                stack.append(result)

        result = self._default_join(stack)[0]
        return result

    def _default_join(self, stack: List[str]) -> List[str]:
        if len(stack) == 2:
            first_operand = stack.pop()
            second_operand = stack.pop()
            value = str(self.binary_dict['&'](
                str(first_operand), str(second_operand)))
            stack.append(value)
        return stack

    def _parse_term(self, term_tuple: TermTuple) -> Union[bool, str]:
        field, operator, value = term_tuple

        function = self.comparison_dict.get(operator)

        result = function(field, value)

        return result
