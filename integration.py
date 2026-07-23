import numpy as np


def trapezoidal_rule(f, a, b, n):
    """
    Numerical Integration using Trapezoidal Rule
    """
    h = (b - a) / n

    x = np.linspace(a, b, n + 1)
    y = f(x)

    result = h * (
        (y[0] + y[-1]) / 2 +
        np.sum(y[1:-1])
    )

    return result


def simpson_one_third_rule(f, a, b, n):
    """
    Numerical Integration using Simpson's 1/3 Rule
    n must be even.
    """
    if n % 2 != 0:
        raise ValueError(
            "Simpson 1/3 Rule requires an even number of intervals."
        )

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)
    y = f(x)

    result = (
        h / 3
    ) * (
        y[0]
        + y[-1]
        + 4 * np.sum(y[1:-1:2])
        + 2 * np.sum(y[2:-2:2])
    )

    return result


def simpson_three_eighth_rule(f, a, b, n):
    """
    Numerical Integration using Simpson's 3/8 Rule
    n must be divisible by 3.
    """
    if n % 3 != 0:
        raise ValueError(
            "Simpson 3/8 Rule requires the number of intervals to be divisible by 3."
        )

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)
    y = f(x)

    total = y[0] + y[-1]

    for i in range(1, n):

        if i % 3 == 0:
            total += 2 * y[i]
        else:
            total += 3 * y[i]

    result = (3 * h / 8) * total

    return result


def weddle_rule(f, a, b, n):
    """
    Numerical Integration using Weddle's Rule
    n must be divisible by 6.
    """
    if n % 6 != 0:
        raise ValueError(
            "Weddle Rule requires the number of intervals to be divisible by 6."
        )

    h = (b - a) / n

    result = 0

    for i in range(0, n, 6):

        x = np.array([
            a + (i + 0) * h,
            a + (i + 1) * h,
            a + (i + 2) * h,
            a + (i + 3) * h,
            a + (i + 4) * h,
            a + (i + 5) * h,
            a + (i + 6) * h
        ])

        y = f(x)

        result += (
            (3 * h) / 10
        ) * (
            y[0]
            + 5 * y[1]
            + y[2]
            + 6 * y[3]
            + y[4]
            + 5 * y[5]
            + y[6]
        )

    return result


def calculate_integral(method, f, a, b, n):
    """
    Select Numerical Integration Method
    """

    if method == "Trapezoidal Rule":
        return trapezoidal_rule(f, a, b, n)

    elif method == "Simpson 1/3 Rule":
        return simpson_one_third_rule(f, a, b, n)

    elif method == "Simpson 3/8 Rule":
        return simpson_three_eighth_rule(f, a, b, n)

    elif method == "Weddle Rule":
        return weddle_rule(f, a, b, n)

    else:
        raise ValueError("Invalid Numerical Integration Method.")