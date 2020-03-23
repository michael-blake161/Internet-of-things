from sense_hat import SenseHat
from time import sleep

class AnimatedEmoji:
   
      blue = (0, 0, 255)
      green = (0, 255, 0)
      purple = (160, 32, 240)
      black = (0, 0, 0)

      sense = SenseHat()

      while True:
   
         c = purple
         b = black

         smiley = [
         c, c, c, c, c, c, c, c,
         c, c, c, c, c, c, c, c,
         c, b, b, c, c, b, b, c,
         c, b, b, c, c, b, b, c,
         c, c, c, c, c, c, c, c,
         c, b, b, c, c, b, b, c,
         c, c, c, b, b, c, c, c,
         c, c, c, c, c, c, c, c
         ]
         sense.set_pixels(smiley)
         sleep(3)


         c = blue
         
         smiley = [
         c, c, c, c, c, c, c, c,
         c, c, c, c, c, c, c, c,
         c, b, b, c, c, b, b, c,
         c, b, b, c, c, b, b, c,
         c, c, c, c, c, c, c, c,
         c, b, b, c, c, b, b, c,
         c, c, c, b, b, c, c, c,
         c, c, c, c, c, c, c, c
         ]
         sense.set_pixels(smiley)
         sleep(3)

         c = green
         smiley = [
         c, c, c, c, c, c, c, c,
         c, c, c, c, c, c, c, c,
         c, b, b, c, c, b, b, c,
         c, b, b, c, c, b, b, c,
         c, c, c, c, c, c, c, c,
         c, b, b, c, c, b, b, c,
         c, c, c, b, b, c, c, c,
         c, c, c, c, c, c, c, c
         ]
         sense.set_pixels(smiley)
         sleep(3)


