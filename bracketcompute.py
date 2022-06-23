import discord
import statistics

class BracketCompute:
  levels = {1:"1-20", 21:"21-30", 31:"31-40", 41:"41-47", 48:"48-55", 56:"56-62", 63:"63-70", 71:"71-77", 78:"78-85", 86:"86-94", 95:"95-100"}
  trainingRoomToLevels = {4:0, 5:26, 6:36, 7:51, 8:66, 9:81}
  brackets = [0,20,30,39,42,47,54,55,62,69,70,77,84,85,94,100]
  authorizedFightersAbove = {40:1, 69:2, 94:3, 100:8}
  
  def span3rule(self, fightersList):
    levelSet = set()
    #pour chaque combattant
    for fighter in fightersList:
      for level in reversed(self.levels.keys()):
        #on regarde dans quel niveau il est
        if fighter >= level:
          #on ajoute le niveau à un set.
          levelSet.add(self.levels[level])
          break
    return levelSet
          
  def validFighters(self, fightersList, trainingRoomLevel):
    validFightersList = []
    #pour chaque combattant
    for fighter in fightersList:
      #on ne l'ajoute que si il est au dessus du niveau min de la trainingroom
      if( fighter >= self.trainingRoomToLevels[trainingRoomLevel] ):
        validFightersList.append(fighter)
            
    #result += ",".join(str(n) for n in validFightersList) + "\n"
    return validFightersList
          
  def bracketFromAverage(self, average):
    #pour chaque bracket
    #si la moyenne est supérieure à niveau bracket+1, va dans le bracket suivant.
    for i in range( len(self.brackets) - 1, -1, -1):
      if( average >= self.brackets[i] + 1 ):
        return self.brackets[i+1]
  
  def countFightersAtMaxLevel(self, validFightersList, maxLevel):
    nb = 0
    for fighter in validFightersList:
      #print("test {} sur {}", fighter, maxLevel)
      if( fighter >= maxLevel ):
        nb = nb + 1
    return nb

  def compute(self, fightersList, trainingRoomLevel):
    
    numberOfFighters = len(fightersList)
  
    validFightersList = self.validFighters(fightersList, trainingRoomLevel)
  
  
    if len(validFightersList) > 0:
      
      levelSet = sorted(self.span3rule(validFightersList))
      
      #plus haut niveau
      maxLevel = list(self.levels.keys())[list(self.levels.values()).index(max(levelSet))]
  
      #nombre de combattants dans le plus haut niveau et nombre autorisé
      nbFightersAtMaxLevel = self.countFightersAtMaxLevel(validFightersList, maxLevel)
      nbMaxAuthorized = round(numberOfFighters/2)
      
      #plus fort combattant
      maxf = max(validFightersList)
    else:
      levelSet = []
      nbFightersAtMaxLevel = 0
      nbMaxAuthorized = 0
      maxf=max(fightersList)
  
    embed = discord.Embed(title="Calcul du bracket", color=0xFF5733)
  
    embed.add_field(name="Caserne", value=f"{numberOfFighters} combattants", inline=False)
    embed.add_field(name="Salle de Formation", value="niveau {}".format(trainingRoomLevel), inline=False)
  
    
    if len(validFightersList):
      embed.add_field(name="Combattants pris en compte", value=",".join(str(n) for n in validFightersList), inline=False)
    else:
      embed.add_field(name="Combattants pris en compte", value="Aucuns :scream:", inline=False)
  
      
    #si il y a plus que 3 dans le set
    if len(levelSet) >=3:
      embed.add_field(name="Règle des 3 niveaux", value="Combattants dans plus de 3 niveaux :scream:\n({})".format(', '.join(levelSet)), inline=False)
      embed.add_field(name="Plus haut combattant", value="{}".format(maxf), inline=False)
      embed.add_field(name="BRACKET", value="**{}x{}**".format(numberOfFighters, self.bracketFromAverage(maxf)), inline=False)
      
    elif len(levelSet) == 0 :
      embed.add_field(name="Plus haut combattant", value="{}".format(maxf), inline=False)
      embed.add_field(name="BRACKET", value=f"**{numberOfFighters}x{self.bracketFromAverage(maxf)}**", inline=False)
      
    elif nbFightersAtMaxLevel > nbMaxAuthorized :
      embed.add_field(name="Combattants dans le niveau supérieur", value=":scream: : {} sur {} max\n_**note :** actuellement, ce calcul n'est pas 100% sûr. Demandez conseil à votre clan_".format(nbFightersAtMaxLevel, nbMaxAuthorized), inline=False)
      embed.add_field(name="BRACKET", value="**{}x{}**".format(numberOfFighters, self.bracketFromAverage(maxf)), inline=False)
      
    else:
      embed.add_field(name="Règle des 3 niveaux", value=":thumbsup: : {}".format(', '.join(levelSet)), inline=True)
      
      meanf = statistics.mean(validFightersList)
      embed.add_field(name="Moyenne", value="{}".format(meanf), inline=False)
      embed.add_field(name="BRACKET", value="**{}x{}**".format(numberOfFighters, self.bracketFromAverage(meanf)), inline=False)
  
    return embed