import os
# os.system("cd ..")

import sys

sys.path.append(r'./Hello World')
from app import home
def test_index():
    assert home()=='Hello World'