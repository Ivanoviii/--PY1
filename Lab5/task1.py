keys = ['bin', 'dec', 'hex', 'oct']
dict = [{"bin": bin(i), "dec": (i), "hex": hex(i), "oct": oct(i)} for i in range(16)]
from pprint import pprint
pprint(dict)