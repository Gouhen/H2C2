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

class Fouet:
  whipslashes = [ "https://c.tenor.com/NIhYtIbVihUAAAAC/shin-jimin-jimin.gif"
                , "https://c.tenor.com/kUv0ib9CgY4AAAAC/whip-fire-whip.gif"
                , "https://c.tenor.com/1XcK_sxXvYEAAAAC/hotdog-hotdogs.gif"
                , "https://c.tenor.com/0LRXMWsCSwgAAAAC/simpsons-whip.gif"
                ]

  def fouette(self):
    return random.choice(self.whipslashes)




class Boude:
  sulk = [ "https://c.tenor.com/7fea_o7VelYAAAAC/cartoon-kitten.gif"
         , "https://c.tenor.com/het_46e4PwUAAAAC/pout-pouting.gif"
         , "https://c.tenor.com/WSeKfIxf8D4AAAAC/pout-tinkerbell.gif"
         ]

  def boudeuh(self):
    return random.choice(self.sulk)
    
    
class Rencard:
  donotsay = [ "C’est fou ce que tu ressembles à ma mère."
             , "T’inquiète, j’ai ce qu’il faut dans ma poche #clindoeilsuperlourd"
             , "Je sors d’une histoire vraiment compliquée."
             , "Tu prends quoi toi, à manger?"
             , "Attends juste 30 secondes, je dois appeler mon agent de libération conditionnelle à 18h."
             , "Papa travaille dans une banque réputée."
             , "J’ai 35 ans et j’habite chez mes parents."
             , "Excuse-moi, je n’ai pas eu le temps de me changer, j’arrive direct du boulot."
             , "Mon métier? Sosie de Ryan Gosling."
             , "Je vais prendre une tranche de pain à l’ail et des spaghetti au pesto."
             , "Tu fais quelque chose dimanche? Viens chez mes parents, il y aura aussi ma tante Cécile!"
             , "Tu ne ressembles pas du tout à ta photo de profil Facebook!"
             , "Et toi, tu veux combien d’enfants?"
             , "En amour je n’ai vraiment pas de chance, je ne tombe que sur des filles chiantes."
             , "Le vin? Je te laisse choisir."
             , "Je te préviens, j’ai un sale caractère."
             , "Tu gagnes combien?"
             , "Viens, on va manger au MacDo!"
             , "On ne s’est pas vu déjà quelque part?"
             , "Je suis super indépendant."
             , "J’avais d’abord craqué sur ta sœur."
             , "Je fais du vélo-tennis-golf tous les dimanches matin avec papa."
             , "Sinon 'Cinquante nuances de Grey', ça t’excite?"
             , "Je te laisse deux minutes, j’ai un coup de fil à passer…"
             , "Je suis resté 5 ans avec elle, mais je n’étais pas amoureux."
             , "Je vis encore avec mon ex, mais plus pour très longtemps."
             , "On boit un dernier verre?"
             , "Tu ressembles à la fille de mes rêves."
             , "Tu ressembles beaucoup à mon ex."
             , "Désolé, je file: j’ai un after de prévu chez une copine."
             , "Je crois que je suis en train de tomber amoureux de toi."
             ]

  def donot(self):
    return random.choice(self.donotsay)
class Flower:
    potDeFlowers = [ "https://www.atozflowers.com/wp-content/uploads/2019/02/800px-Lycoris_radiata_-_Kinchakuda_2018_-_2.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2017/11/Magnolia_flower_Duke_campus-1024x640.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2018/07/5341134754_d2dd47806a_o-1024x686.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2017/11/800px-Purple_Flower__Pensamiento__Viola_%C3%97_wittrockiana.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2021/01/gloriosa-in-a-greenhouse-C47SHEF-Large-1024x683.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2017/12/Gfp-yellow-blooming-dandelion-1024x683.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2020/07/loewenmaeulchen-897902_1280-1024x682.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2020/09/datura-ordinary-3852817_1280-682x1024.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2017/11/Dahlia_Marys_Jomanda-1024x768.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2018/06/hearts-in-nature-G5CMHH4-Custom-1024x768.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2018/08/Protea_cynaroides_Flower-1024x768.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2018/07/Dracula_gigas_33800268116-1024x1024.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2018/10/Lily_of_the_valley_777-1024x708.jpg"
                   , "https://www.atozflowers.com/wp-content/uploads/2017/11/Small_Red_Rose-1024x768.jpg"
                   ]
    def flowers(self):
        return random.choice(self.potDeFlowers)
