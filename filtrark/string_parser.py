from typing import NewType, List, Tuple, Union
from filtrark.operator_group import OperatorGroup

TermTuple = NewType('TermTuple', Tuple[str, str, Union[str, float]])


class StringParser:
    def __init__(self, operator_group: OperatorGroup) -> None:
        self.operator_group = operator_group

    def parse(self, domain: List[Union[str, TermTuple]]) -> str:
        stack = []  # type: List[str]
        for item in list(reversed(domain)):
            if item in self.operator_group.binary_operators():
                first_operand = stack.pop()
                second_operand = stack.pop()
                string_term = str(
                    self.operator_group.binary_operators()[str(item)](
                        first_operand, second_operand))
                stack.append(string_term)
            elif item in self.operator_group.unary_operators():
                operand = stack.pop()
                stack.append(
                    str(self.operator_group.unary_operators()[str(item)](
                        operand)))

            stack = self._default_join(stack)

            if isinstance(item, tuple):
                result = str(self._parse_term(item))
                stack.append(result)

        result = str(self._default_join(stack)[0])
        return result

    def expression(self):
        pass

    def _default_join(self, stack: List[str]
                      ) -> List[str]:
        if len(stack) == 2:
            first_operand = stack.pop()
            second_operand = stack.pop()
            value = str(self.operator_group.binary_operators()['&'](
                str(first_operand), str(second_operand)))
            stack.append(value)
        return stack

    def _parse_term(self, term_tuple: TermTuple) -> Union[bool, str]:
        field, operator, value = term_tuple
        function = self.operator_group.comparison_operators().get(operator)
        result = function(field, value)
        return result
