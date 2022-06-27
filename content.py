import random

class Content:
  happyThoughts = [ ":smiling_face_with_3_hearts: Le soleil brille, les oiseaux chantent!"
                  , "Youpi, youpi!! :zany_face:"
                  , "Yipikaïïï!! "
                  , "Le soleil chante, les oiseaux brillent! :zany_face:"
                  , "Chuis hyper conteeeent(e) :face_vomiting: !!"
                  ]

  def happy(self):
    return random.choice(self.happyThoughts)
