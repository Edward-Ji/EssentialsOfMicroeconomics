from enum import Enum

from sympy import N, latex


class Approx(Enum):
    HIDE = "Hide"
    REPLACE = "Replace"
    APPEND = "Append"


def latex_approx(expr, perc: int = 15, approx: Approx = Approx.HIDE):
    if approx == Approx.HIDE:
        return latex(expr)
    evalf = N(expr, perc)
    if evalf == expr:
        return latex(expr)
    elif approx == Approx.REPLACE:
        return latex(evalf)
    elif approx == Approx.APPEND:
        return latex(expr) + r"\approx " + latex(evalf)
    else:
        assert False
