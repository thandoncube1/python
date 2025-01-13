# Example file for Advanced Python by Joe Marini
# Programming challenge for working with Exceptions

# Implement the InvalidTempError exception class here


class DigitalOven:
    def __init__(self):
        self.temp = 0

    def set_temp(self, temp):
        self.temp = temp

    def get_temp(self):
        return self.temp

def test_oven(test_temp):
    global oven
    try:
        oven.set_temp(test_temp)
    finally:
        print(f"Current temp setting is {oven.get_temp()}")

# An "InvalidTempError" Exception should be raised if the temperature
# is set below 100 degrees or above 500 degrees
oven = DigitalOven()
test_oven(250)
test_oven(50)
test_oven(0)
test_oven(600)
