from typing import Dict, Any


class SafeEval:

    def __init__(self) -> None:
        self._prefix = '>>>'
        self._globals = {
            '__builtins__': None
        }
        self._forbidden = ['__', '**']

    def __call__(self, expression: str, locals: Dict[str, Any] = {}) -> Any:
        if not expression.startswith(self._prefix) or any(
                character in expression for character in self._forbidden):
            return expression

        expression = expression.replace(self._prefix, '').strip()

        return eval(expression, self._globals, locals)
