#!/usr/bin/python3
'''Export python grammar to C grammar files

Author: Jeroen van der Heijden (Transceptor Technology)
Date: 2016-10-10
'''
import os
import sys
sys.path.insert(0, '../../pyleri/')
from grammar import siri_grammar


if __name__ == '__main__':
    c_file, h_file = siri_grammar.export_c(target='siri/grammar/grammar')

    EXPORT_PATH = 'cgrammar'

    try:
        os.makedirs(EXPORT_PATH)
    except FileExistsError:
        pass

    with open(os.path.join(EXPORT_PATH, 'grammar.c'),
              'w',
              encoding='utf-8') as f:
        f.write(c_file)
    with open(os.path.join(EXPORT_PATH, 'grammar.h'),
              'w',
              encoding='utf-8') as f:
        f.write(h_file)

    print('\nFinished creating new c-grammar files...\n')

    js_file = siri_grammar.export_js()

    EXPORT_PATH = 'jsgrammar'

    try:
        os.makedirs(EXPORT_PATH)
    except FileExistsError:
        pass

    with open(os.path.join(EXPORT_PATH, 'grammar.js'),
              'w',
              encoding='utf-8') as f:
        f.write(js_file)

    print('\nFinished creating new js-grammar file...\n')

    py_file = siri_grammar.export_py()

    EXPORT_PATH = 'pygrammar'

    try:
        os.makedirs(EXPORT_PATH)
    except FileExistsError:
        pass

    with open(os.path.join(EXPORT_PATH, 'grammar.py'),
              'w',
              encoding='utf-8') as f:
        f.write(py_file)

    print('\nFinished creating new py-grammar file...\n')

    go_file = siri_grammar.export_go()

    EXPORT_PATH = 'gogrammar'

    try:
        os.makedirs(EXPORT_PATH)
    except FileExistsError:
        pass

    with open(os.path.join(EXPORT_PATH, 'grammar.go'),
              'w',
              encoding='utf-8') as f:
        f.write(go_file)

    print('\nFinished creating new go-grammar file...\n')

    java_file = siri_grammar.export_java()

    EXPORT_PATH = 'javagrammar'

    try:
        os.makedirs(EXPORT_PATH)
    except FileExistsError:
        pass

    with open(os.path.join(EXPORT_PATH, 'SiriGrammar.java'),
              'w',
              encoding='utf-8') as f:
        f.write(java_file)

    print('\nFinished creating new java-grammar file...\n')
