# You can set the data type early on
age: int
age = 12

# This says the user_age parameter must be an integer and the return is a boolean
# These are called type hints
def police_check(user_age: int) -> bool:

    if user_age > 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive





#  But if we forgot what this function does... maybe we give it the wrong input. So instead we
if police_check(19):
    print("You are good")
else:
    print("Pay fine")

