from sense_hat import SenseHat
import time

sense = SenseHat ()

w = (255, 255, 255) # White
g = (0, 102, 0) # Green
b = (0, 0, 255) # Blue
r = (255, 0, 0) # Red
t = (153, 76, 0) # Brown
e = (0, 0, 0) # Empty

pet1 = [
    e, e, e, w, g, e, e, e,
    e, e, g, g, g, r, e, e,
    e, g, g, b, g, g, g, e,
    e, g, g, g, g, g, g, e,
    g, g, b, g, w, g, r, g,
    r, g, g, g, g, g, g, g,
    e, e, g, w, g, g, e, e,
    e, e, e, t, t, e, e, e,
    ]

pet2 = [
    e, e, e, r, g, e, e, e,
    e, e, g, g, g, b, e, e,
    e, g, g, w, g, g, g, e,
    e, g, g, g, g, g, g, e,
    g, g, w, g, r, g, b, g,
    b, g, g, g, g, g, g, g,
    e, e, g, r, g, g, e, e,
    e, e, e, t, t, e, e, e,
    ]

pet3 = [
    e, e, e, b, g, e, e, e,
    e, e, g, g, g, w, e, e,
    e, g, g, r, g, g, g, e,
    e, g, g, g, g, g, g, e,
    g, g, b, g, w, g, b, g,
    w, g, g, g, g, g, g, g,
    e, e, g, b, g, g, e, e,
    e, e, e, t, t, e, e, e,
    ]
    
def twinkling ():
    for i in range(10):
        sense.set_pixels (pet1)
        time.sleep(0.4)
        sense.set_pixels (pet2)
        time.sleep (0.4)
        sense.set_pixels (pet3)
        time.sleep (0.4)

sense.clear()

x, y, z, = sense.get_accelerometer_raw().values()

while x<2 and y<2 and z<2:
    x, y, z, = sense.get_accelerometer_raw().values()

twinkling()
sense.clear()

    
