import os
# os.system("cd ..")

import sys

sys.path.append(r'C:\Users\ACER\Downloads\Day04-Docker-20221009T052040Z-001\Day04-Docker\Hello World\Hello World')
from app import home
def test_index():
    assert home()=='Hello World'