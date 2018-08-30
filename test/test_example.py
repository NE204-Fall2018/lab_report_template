# Tests for the trivial example code in code/example.py
from __future__ import absolute_import
import sys
import os
# Temporarily add the repo path to the PYTHONPATH so that code can be imported
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from code.example import add

from nose.tools import assert_raises

def test_add_works():
    assert add(2, 2) == 4

def test_add_commutative():
    assert add(1, 3) == add(3, 1)

def test_add_bad_inputs():
    a = 1
    b = "I'm a string"
    assert_raises(TypeError, add, a, b)
