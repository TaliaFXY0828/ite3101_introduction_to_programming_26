def using_control_once() -> str:
    if 8 > 3:
        return "Success #1"


def using_control_again() -> str:
    if 7 == 7:
        return "Success #2"


print(using_control_once())
print(using_control_again())
