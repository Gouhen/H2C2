import random

class Fouet:
  whipslashes = [ "https://c.tenor.com/NIhYtIbVihUAAAAC/shin-jimin-jimin.gif"
                , "https://c.tenor.com/kUv0ib9CgY4AAAAC/whip-fire-whip.gif"
                , "https://c.tenor.com/1XcK_sxXvYEAAAAC/hotdog-hotdogs.gif"
                , "https://c.tenor.com/0LRXMWsCSwgAAAAC/simpsons-whip.gif"
                ]

  def fouette(self):
    return random.choice(self.whipslashes)
