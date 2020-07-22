# How to delete a random dictionary item?
import random

d = {"A": 4, "O": 6, "P": 10,
     "M": 7, "B": 3}
print(d)

keys = list(d.keys())
what_del = random.choice(keys)
del d[what_del]
print(d)

"""   RUN  DEMO
{'A': 4, 'O': 6, 'P': 10, 'M': 7, 'B': 3}
{'A': 4, 'O': 6, 'M': 7, 'B': 3}
"""
