import sys

print("Hello world")
USER = "Robin"
print("This is running in this namespace:", __name__)


def print_name():
    print(USER)

a = "Hello "
b = "Hello "
print(id(a), id(b))