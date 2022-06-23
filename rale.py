import random

class Rale:
  shoutsOfRage = ["Greumblblblblbl <:madchibiwasabi:905761925613359135> !!", "<:madchibiwasabi:905761925613359135> Greumblblblblbl!!", "Fuuuuuuuuuuuuu <:furiouschibiwasabi:905761899147325441>  !!!"]

  def shout(self):
    return random.choice(self.shoutsOfRage)

class Content:
  happyThoughts = [":smiling_face_with_3_hearts: Le soleil brille, les oiseaux chantent!", "Youpi, youpi!! :zany_face:", "Yipikaïïï!! ", "Le soleil chante, les oiseaux brillent! :zany_face:", "Chuis hyper conteeeent(e) :face_vomiting: !!"]

  def happy(self):
    return random.choice(self.happyThoughts)

class Fouet:
  whipslashes = ["https://c.tenor.com/NIhYtIbVihUAAAAC/shin-jimin-jimin.gif", "https://c.tenor.com/kUv0ib9CgY4AAAAC/whip-fire-whip.gif", "https://c.tenor.com/1XcK_sxXvYEAAAAC/hotdog-hotdogs.gif", "https://c.tenor.com/0LRXMWsCSwgAAAAC/simpsons-whip.gif"]

  def fouette(self):
    return random.choice(self.whipslashes)




class Boude:
  sulk = ["https://c.tenor.com/7fea_o7VelYAAAAC/cartoon-kitten.gif", "https://c.tenor.com/het_46e4PwUAAAAC/pout-pouting.gif", "https://c.tenor.com/WSeKfIxf8D4AAAAC/pout-tinkerbell.gif"]

  def boudeuh(self):
    return random.choice(self.sulk)