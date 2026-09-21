# MULTIPLE INHERITANCE

class Vehicle:
    def __init__(self, speed):
        self.speed = speed


class SportsItem:
    def __init__(self, weight):
        self.weight = weight


class Bicycle(Vehicle, SportsItem):
    def __init__(self, speed, weight, gears):
        Vehicle.__init__(self, speed)
        SportsItem.__init__(self, weight)
        self.gears = gears


details = []

for d in range(2):
    a = int(input("Input speed: "))
    b = int(input("Input weight: "))
    c = int(input("Input gears: "))

    details.append(Bicycle(a, b, c))


for detail in details:
    print(f"Speed: {detail.speed}")
    print(f"Weight: {detail.weight}")
    print(f"Gears: {detail.gears}")