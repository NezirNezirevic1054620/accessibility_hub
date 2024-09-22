# import random
import secrets
import string


def username_generator(full_name):
    if len(full_name) > 1:
        first_letter = full_name[0][0]
        three_letters_surname = full_name[-1][:3].rjust(3, "x")
        number = "{:03d}".format(secrets.randbelow(999) + 1)
        return "{}{}{}".format(first_letter, three_letters_surname, number)

    else:
        print("Error. Please enter first name and surname")
        # try again...


def password_generator():
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for i in range(15))  # for a 15-character password


if __name__ == "__main__":
    username = username_generator("test person")
    password = password_generator()
    print(username, password)
