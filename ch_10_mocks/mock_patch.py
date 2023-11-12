from unittest.mock import patch
from calendar import isleap


with patch('__main__.isleap'):
    print(isleap(1995))
