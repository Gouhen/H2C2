class BracketCompute:
  levels = {1:"1-20", 21:"21-30", 31:"31-40", 41:"41-47", 48:"48-55", 56:"56-62", 63:"63-70", 71:"71-77", 78:"78-85", 86:"86-94", 95:"95-100"}
  trainingRoomToLevels = {4:0, 5:26, 6:36, 7:51, 8:66, 9:81}
  brackets = [0,20,30,39,42,47,54,55,62,69,70,77,84,85,94,100]
  authorizedFightersAbove = {40:1, 69:2, 94:3, 100:8}
  
  def span3rule(self, fightersList, ctx):
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