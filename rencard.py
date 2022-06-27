import random

class Rencard:
    donotsay =  [ "C’est fou ce que tu ressembles à ma mère."
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
