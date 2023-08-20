from random import SystemRandom
from random import choice

character_set = {
    "lower":['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'],
    "upper":['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'],
    "digits":['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    "special":['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<'],
}
super_set = ["lower", "upper", "digits", "special"]

def generate(alpha, special, upper, complexity, max_len=10):
    print(alpha)
    print(special)
    print(upper)
    print(complexity)

    MAX_RETRY = 5 + max_len
    type_set = super_set.copy()
    password = ""
    if not alpha:
        type_set.clear()
        type_set = ["digits"]
    else:
        if not special:
            type_set.remove("special")
        if not upper:
            type_set.remove("upper")
        if complexity:
            password_set = set()
            while(len(password_set)!=max_len):
                type = choice(type_set)
                temp = choice(character_set[type])
                password_set.add(temp)
                # terminate possibility of infinite loop
                if not MAX_RETRY:
                    break
                else:
                    MAX_RETRY-=1
            for char in password_set:
                password+=char
            return password
        # no check for repetition in password

    for i in range(max_len):
        type = choice(type_set)
        password += choice(character_set[type])
    return password

