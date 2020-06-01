import os
import sys

"""
Если у вас без данного файла нет ошибки,
ModuleNotFoundError: No module named 'module name', то его можно удалить.
"""

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))