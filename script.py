import math
import sys
from os import rename

import requests

r = requests.get('https://www.youtube.com/watch?v=RMH6X5VKEuY&list=RDRMH6X5VKEuY&start_radio=1')
print(r.status_code)

