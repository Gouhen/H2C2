import random

class Rale:
  shoutsOfRage = [ "Greumblblblblbl <:madchibiwasabi:905761925613359135> !!"
                 , "<:madchibiwasabi:905761925613359135> Greumblblblblbl!!"
                 , "Fuuuuuuuuuuuuu <:furiouschibiwasabi:905761899147325441>  !!!"
                 ]

  def shout(self):
    return random.choice(self.shoutsOfRage)

class Content:
  happyThoughts = [ ":smiling_face_with_3_hearts: Le soleil brille, les oiseaux chantent!"
                  , "Youpi, youpi!! :zany_face:"
                  , "Yipikaïïï!! "
                  , "Le soleil chante, les oiseaux brillent! :zany_face:"
                  , "Chuis hyper conteeeent(e) :face_vomiting: !!"
                  ]

  def happy(self):
    return random.choice(self.happyThoughts)

