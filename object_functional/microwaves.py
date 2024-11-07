class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on.")
        else:
            self.turned_on = True
            print(f"Microwave ({self.brand}) is now turned on")

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave ({self.brand}) is now turned off.")
        else:
            print(f"Microwave ({self.brand}) is already turned on")

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f"Running ({self.brand}) for {seconds} seconds")
        else:
            print("Turn the microwave on to use the features.")

    def __str__(self):
        return f"{self.brand} Rating: {self.power_rating}"

    def __repr__(self) -> None:
        return f'''Microwave(brand="{self.brand}",\
 power_rating="{self.power_rating}")'''


smeg: Microwave = Microwave('Smeg', 'B')
print(smeg)
print(smeg.brand)
print(smeg.power_rating)
smeg.turn_on()
smeg.run(30)
smeg.turn_off

bosch: Microwave = Microwave('Bosch', 'C')
print(bosch.brand)
print(bosch.power_rating)
bosch.run(10)
bosch.turn_on()

print(smeg)
print(bosch)
print(repr(smeg))
print(repr(bosch))



numslist = [3, 1, 2, 7, 4, 2, 1, 1, 5]

def find_length(nums: list[int], k: int) -> int:
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        # This is a regular method to find length
        while curr > k:
            curr -= nums[left]
            left += 1

        ans = max(ans, right - left + 1)
    return ans

print(find_length(numslist, 8))