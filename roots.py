"""
    Using the coefficients of a quadratic equation, returns information regarding the roots of the equation.
    Author: Brennan Tomlinson
"""


import math


print('The format of a quadratic equation is ax', chr(0x00B2), '+bx+c', sep='')


a = int(input('Enter a '))
b = int(input('Enter b '))
c = int(input('Enter c '))


def get_equation(coeff1, coeff2, coeff3):
    """
    Recreates the quadratic equation and returns it.
    :param coeff1:
    :param coeff2:
    :param coeff3:
    :return:
    """
    print(coeff1, 'x', chr(0x00B2), '+', coeff2, 'x+', coeff3, sep='')


def get_number_of_roots(coeff1, coeff2, coeff3):
    """
    This function returns the number of roots.
    :param coeff1:
    :param coeff2:
    :param coeff3:
    :return:
    """
    num_of_roots_equation = coeff1 ** 2 - 4 * coeff2 * coeff3

    if num_of_roots_equation < 0:
        raw_number_of_roots = 0

    if num_of_roots_equation == 0:
        raw_number_of_roots = 1

    if num_of_roots_equation > 0:
        raw_number_of_roots = 2

    return raw_number_of_roots


def get_roots( coeff1, coeff2, coeff3, number_of_roots):
    """

    :param coeff1:
    :param coeff2:
    :param coeff3:
    :return:
    """


def main():
    """
    hold
    :return:
    """
    get_equation(a, b, c)

    number_of_roots = get_number_of_roots(a, b, c)

    if number_of_roots == 0:
        print('No roots.')

    if number_of_roots == 1:
        print('One root.')

    if number_of_roots == 2:
        print('Two roots.')


main()
