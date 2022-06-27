import random

class Rale:
  shoutsOfRage = [ "Greumblblblblbl <:madchibiwasabi:905761925613359135> !!"
                 , "<:madchibiwasabi:905761925613359135> Greumblblblblbl!!"
                 , "Fuuuuuuuuuuuuu <:furiouschibiwasabi:905761899147325441>  !!!"
                 ]

  def shout(self):
    return random.choice(self.shoutsOfRage)

