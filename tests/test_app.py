import os
import sys

# Добавляем корень проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import add


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -2) == -3
