#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Vincent Newsom"

import sys


def is_nested(line):
    left_bracket = ['[', '{', '(', '<', '(*']
    right_bracket = [']', '}', ')', '>']
    bracket_stack = []
    index_error = 0
    for char in line:
        if char in left_bracket:
            bracket_stack.append(char)
            index_error += 1
        elif char == '*' and bracket_stack and bracket_stack[- 1] == '(':
            bracket_stack[-1] = '(*'
        elif bracket_stack and bracket_stack[-1] == '*' and char == ')':
            bracket_stack.pop()
            if bracket_stack and bracket_stack[-1] == '(*':
                bracket_stack.pop()
            else:
                with open('output.txt', 'a') as f:
                    f.write(f'N0 {index_error}\n')
                print('N0', index_error)
                return
        elif bracket_stack and bracket_stack[-1] == '(*' and char == ')':
            index_error += 1
            with open('output.txt', 'a') as f:
                f.write(f'N0 {index_error}\n')
            print('N0', index_error)
            return
        elif char in right_bracket and len(bracket_stack) >= 1\
                and left_bracket.index(bracket_stack[len(bracket_stack)-1]) ==\
                right_bracket.index(char):
            bracket_stack.pop()
            index_error += 1
        elif (char in right_bracket and not bracket_stack) or\
            (char in right_bracket and
             left_bracket.index(bracket_stack[len(bracket_stack)-1]) !=
                right_bracket.index(char)):
            index_error += 1
            with open('output.txt', 'a') as f:
                f.write(f'N0 {index_error}\n')
            print('N0', index_error)
            return
        elif bracket_stack and bracket_stack[-1] == '*' and char == '*':
            index_error += 1
        elif char == '*':
            bracket_stack.append(char)
            index_error += 1
        else:
            index_error += 1

    left_bracket_remainder = [
        x for x in bracket_stack if left_bracket.count(x)]
    # total_right_bracket = [x for x in list(line) if right_bracket.count(x)]
    # check condition below
    # if not total_right_bracket and len(left_bracket_remainder) and list(line)[-1] == '\n':
    #     with open('output.txt', 'a') as f:
    #         f.write(f'N0 {index_error}\n')
    #     print('NO', index_error)
    if len(left_bracket_remainder):
        with open('output.txt', 'a') as f:
            f.write(f'N0 {index_error}\n')
        print('NO', index_error)
    else:
        with open('output.txt', 'a') as f:
            f.write('YES\n')
        print('YES')
    return
    pass


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    with open(args[0]) as f:
        for line in f:
            is_nested(line)
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
