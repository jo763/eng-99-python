# Define a car class

# Initialised with a top speed attribute, current speed (start at 0),
# methods: accelerate method (add x mph to speed)
# brake method, removes speed

# do the accelerate and the brake methods work as you would expect?

class Car():
    def __init__(self, top_speed):
        self.top_speed = top_speed
        self._speed = 0

    def accelerate(self, speed_amount):
        self._speed += speed_amount
        if self._speed > self.top_speed:
            self._speed = self.top_speed
    def brake(self, speed_amount):
        self._speed -= speed_amount
        if self._speed < 0:
            self._speed = 0
    def get_speed(self):
        return self._speed

toyota_aygo = Car(96)

toyota_aygo.accelerate(10)
print(toyota_aygo._speed)
