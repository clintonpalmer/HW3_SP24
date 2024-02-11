
def simp_rule(f, a, b, n = 1000):
    """
    This function uses the Simpsons 1/3 rule of numerical integration.
    :param f:  the callback function. The function of x to integrate
    :param a: left limit of integration
    :param b: right limit of integration
    :param n:  number of points in integration
    :return: the value of the integral of f(x) between a, b
    Chatgpt and Dr. Jim Smay's video assisted in the development of this function
    video titled hw3b_SP24   https://youtu.be/mhMG3mFU18M?si=4fF89xy_cyos9pm3
    """
    xL = min(a,b)
    xR = max(a,b)
    if xL == xR:
        return 0
    h = (b - a) / n # calculate panel width
    x = [a + i * h for i in range(n + 1)]
    integral = f(a) + f(b)
    for i in range(1, n, 2):
        integral += 4 * f(x[i])
    for i in range(2, n - 1, 2):
        integral += 2 * f(x[i])
    integral *= h / 3
    return integral # return the value for the interval.
