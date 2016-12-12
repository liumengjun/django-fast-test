import uuid
import string
import random


_chars = string.ascii_letters + string.digits

def random_chars(num):
    return ''.join(random.sample(_chars, num))

def random_name():
    return random_chars(9) + '_' + str(uuid.uuid1())[:23].replace('-','')

def random_string(num=30):
    return ''.join(random.choice(_chars) for i in range(num))
