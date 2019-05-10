

""" This is a demo module... """

__author__ = 'Tom'

import sys


def _fn_private():
    print('This is a private function...')


def fn_test():
    """ This is a test function """
    print(sys.argv)
    _fn_private()


if __name__ == '__main__':
    fn_test()

# print('demo.py', __name__)
