import random

class Flower:
    potDeFlowers =  [ "https://www.atozflowers.com/wp-content/uploads/2019/02/800px-Lycoris_radiata_-_Kinchakuda_2018_-_2.jpg"
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
