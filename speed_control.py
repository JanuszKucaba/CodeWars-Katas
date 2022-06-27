"""
Given s and x the task is to return as an integer the *floor* of the maximum
average speed per hour obtained on the sections of x. If x length is less than
or equal to 1 return 0 since the car didn't move.
https://www.codewars.com/kata/56484848ba95170a8000004d
"""


def gps(s, x):
    """
    Input: s - speed [seconds], x - distances.

    Otput: maximum average speed per hour
    """
    if len(x) > 1:
        delta_x = [x[i+1] - x[i] for i in range(len(x)-1)]
        delta_distance = [(3600 * x) / s for x in delta_x]
        return max(delta_distance)
    else:
        return 0


if __name__ == '__main__':
    from math import fabs

    def testing(actual, expected, msg=""):
        """Test function."""
        r = fabs(actual - expected)
        inrange = r <= 1
        if (msg == "" and inrange == False):
            msg = "(actual - expected).abs must be <= 1 but was {:.2f}"
            msg = msg.format(r)
        return print(inrange, msg)

    x = [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61]
    s = 20
    u = 41
    testing(gps(s, x), u)
    x = [0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25]
    s = 12
    u = 219
    testing(gps(s, x), u)
    x = [0.0, 0.18, 0.36, 0.54, 0.72, 1.05, 1.26, 1.47, 1.92, 2.16, 2.4, 2.64, 2.88, 3.12, 3.36, 3.6, 3.84]
    s = 20
    u = 80
    testing(gps(s, x), u)
    x = [0.0, 0.01, 0.36, 0.6, 0.84, 1.05, 1.26, 1.47, 1.68, 1.89, 2.1, 2.31, 2.52, 2.73, 2.94, 3.15]
    s = 14
    u = 90
    testing(gps(s, x), u)
    x = [0.0, 0.02, 0.36, 0.54, 0.72, 0.9, 1.08, 1.26, 1.44, 1.62, 1.8]
    s = 17
    u = 72
    testing(gps(s, x), u)
    x = [0.0, 0.24, 0.48, 0.72, 0.96, 1.2, 1.44, 1.68, 1.92, 2.16, 2.4]
    s = 12
    u = 72
    testing(gps(s, x), u)
    x = [0.0, 0.02, 0.44, 0.66, 0.88, 1.1, 1.32, 1.54, 1.76]
    s = 17
    u = 88
    testing(gps(s, x), u)
    x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.32, 1.54, 1.76, 1.98, 2.2, 2.42, 2.76, 2.99, 3.22, 3.45]
    s = 16
    u = 76
    testing(gps(s, x), u)
    x = [0.0, 0.01, 0.36, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75]
    s = 17
    u = 82
    testing(gps(s, x), u)
    x = [0.0, 0.2, 0.4, 0.69, 0.92, 1.15, 1.38, 1.61, 1.92, 2.16, 2.4, 2.64, 2.88, 3.12, 3.36]
    s = 19
    u = 58
    testing(gps(s, x), u)
    x = []
    s = 19
    u = 0
    testing(gps(s, x), u)
    x = [0.0]
    s = 19
    u = 0
    testing(gps(s, x), u)
