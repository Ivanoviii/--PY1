import random
import string

def get_random_password() -> str:
    numm_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    n = random.randrange(8, len(numm_), 1)
    password = "".join(random.sample(numm_, n))
    return password


print(get_random_password())
