from discord.ext import commands
from discord_slash import SlashCommand
import discord
#from replit import db
import os
#repl.it specific
#from keep_alive import keep_alive
import statistics
import re

from bracketcompute import BracketCompute
from channelcopy import ChannelCopy
from rale import Rale, Content, Fouet, Boude

#repl.it specific
my_secret = os.environ['DA_TOKEN']
disabled_guilds = os.environ['disabled']


#result = ""



bot = commands.Bot(command_prefix='!', help_command=None)
slash = SlashCommand(bot, sync_commands=True)

@bot.command(name="bracket")
async def bracket(ctx, *, args):

  #await ctx.channel.send("debug en cours")
  sdfre = re.compile("\s*sdf\s*=*")
  if not sdfre.search(args) :
    await ctx.channel.send("Ne trouve pas 'sdf'\nExemple d'utilisation :\n!bracket 100, 90, 81, 81, 81 sdf 9")
    return
  
  #await ctx.channel.send("1")

  arguments = sdfre.split(args)

  if len(arguments) != 2:
    await ctx.channel.send("Ne trouve pas 'sdf'\nExemple d'utilisation :\n!bracket 100, 90, 81, 81, 81 sdf 9")
    return

  #await ctx.channel.send("2")
  spacere = re.compile("\s*,\s*|\s+")
  fl = spacere.split(arguments[0])
  #await ctx.channel.send(fl)
  if not fl:
    await ctx.channel.send("Ne trouve pas la liste des niveaux de combattants\nExemple d'utilisation :\n!bracket 100, 90, 81, 81, 81 sdf 9")
    return
    
  fightersList = []
  for i in range(len(fl)):
    if fl[i].isdigit():
      fightersList.append(int(fl[i]))

  trainingRoomLevel = int(arguments[1])

  b = BracketCompute()# TODO (fightersList, trainingRoomLevel)

  
  numberOfFighters = len(fightersList)

  validFightersList = b.validFighters(fightersList, trainingRoomLevel)


  if len(validFightersList) > 0:
    
    levelSet = sorted(b.span3rule(validFightersList, ctx))
    
    #plus haut niveau
    maxLevel = list(b.levels.keys())[list(b.levels.values()).index(max(levelSet))]

    #nombre de combattants dans le plus haut niveau et nombre autorisé
    nbFightersAtMaxLevel = b.countFightersAtMaxLevel(validFightersList, maxLevel)
    nbMaxAuthorized = round(numberOfFighters/2)
    
    #plus fort combattant
    maxf = max(validFightersList)
  else:
    levelSet = []
    nbFightersAtMaxLevel = 0
    nbMaxAuthorized = 0
    maxf=max(fightersList)

  embed = discord.Embed(title="Calcul du bracket", color=0xFF5733)

  embed.add_field(name="Caserne", value="{} combattants".format(numberOfFighters), inline=False)
  embed.add_field(name="Salle de Formation", value="niveau {}".format(trainingRoomLevel), inline=False)

  #await ctx.channel.send("Caserne "+str(numberOfFighters)+" combattants, Salle de Formation niveau "+str(trainingRoomLevel))
  
  if len(validFightersList):
    embed.add_field(name="Combattants pris en compte", value=",".join(str(n) for n in validFightersList), inline=False)
  else:
    embed.add_field(name="Combattants pris en compte", value="Aucuns :scream:", inline=False)

    
  #si il y a plus que 3 dans le set
  if len(levelSet) >=3:
    embed.add_field(name="Règle des 3 niveaux", value="Combattants dans plus de 3 niveaux :scream:\n({})".format(', '.join(levelSet)), inline=False)
    embed.add_field(name="Plus haut combattant", value="{}".format(maxf), inline=False)
    embed.add_field(name="BRACKET", value="**{}x{}**".format(numberOfFighters, b.bracketFromAverage(maxf)), inline=False)
    
  elif len(levelSet) == 0 :
    embed.add_field(name="Plus haut combattant", value="{}".format(maxf), inline=False)
    embed.add_field(name="BRACKET", value="**{}x{}**".format(numberOfFighters, b.bracketFromAverage(maxf)), inline=False)
    
  elif nbFightersAtMaxLevel > nbMaxAuthorized :
    embed.add_field(name="Combattants dans le niveau supérieur", value=":scream: : {} sur {} max\n_**note :** actuellement, ce calcul n'est pas correct. Demandez conseil à votre clan_".format(nbFightersAtMaxLevel, nbMaxAuthorized), inline=False)
    embed.add_field(name="BRACKET", value="**{}x{}**".format(numberOfFighters, b.bracketFromAverage(maxf)), inline=False)
    
  else:
    embed.add_field(name="Règle des 3 niveaux", value=":thumbsup: : {}".format(', '.join(levelSet)), inline=True)
    
    meanf = statistics.mean(validFightersList)
    embed.add_field(name="Moyenne", value="{}".format(meanf), inline=False)
    embed.add_field(name="BRACKET", value="**{}x{}**".format(numberOfFighters, b.bracketFromAverage(meanf)), inline=False)


  await ctx.channel.send(embed=embed)



  

@bot.command(name="ensemble")
async def ensemble(ctx, *, args):
  arguments = args.split()

  if len(arguments) != 3:
    await ctx.channel.send("Utilisation : !ensemble <min> <max> <tirage>\nExemple : !ensemble 12123 19198 14051")
    return
  #(valeur-min) * 100 / (max - min)
  arguments = list(map(float, arguments))
  min, max, value = arguments
  percentage = (value-min)*100.0 / (max-min)
  if percentage < 30:
      await ctx.channel.send("**{}%**.   :scream:".format(round(percentage, 2)))
  elif percentage < 60:
      await ctx.channel.send("**{}%**.   :slight_smile:".format(round(percentage, 2)))
  elif percentage < 80:
      await ctx.channel.send("**{}%**.   :grinning:".format(round(percentage, 2)))  
  else:
      await ctx.channel.send("**{}%**.   :star_struck:".format(round(percentage, 2)))
  #await ctx.channel.send("**{}%**".format(round(percentage, 2)))



@slash.slash(name="ping", description="Le plus beau jeu du monde")
async def ping(ctx):
  if disabled_guilds == str(ctx.message.guild.id):
    return
  #await ctx.message.delete()
  await ctx.channel.send("pong")




@bot.command(name="rale")
async def rale(ctx):
  if disabled_guilds == str(ctx.message.guild.id):
    return
  await ctx.message.delete()
  r=Rale()
  #await ctx.channel.send()
  embed = discord.Embed(title=r.shout(), color=0xFF5733)
  embed.set_author(name=ctx.author.display_name+" en a gros", icon_url=ctx.author.avatar_url)

  await ctx.channel.send(embed=embed)




@bot.command(name="content")
async def content(ctx):
  if disabled_guilds == str(ctx.message.guild.id):
    return
  await ctx.message.delete()
  c=Content()
  embed = discord.Embed(title=c.happy(), color=0x33CC00)
  embed.set_author(name=ctx.author.display_name+" est content", icon_url=ctx.author.avatar_url)

  await ctx.channel.send(embed=embed)

@bot.command(name="contente")
async def contente(ctx):
  if disabled_guilds == str(ctx.message.guild.id):
    return
  await ctx.message.delete()
  c=Content()

  embed = discord.Embed(title=c.happy(), color=0x33CC00)
  embed.set_author(name=ctx.author.display_name+" est contente", icon_url=ctx.author.avatar_url)

  await ctx.channel.send(embed=embed)


@bot.command(name="fouet")
async def fouet(ctx):
  if disabled_guilds == str(ctx.message.guild.id):
    return
  await ctx.message.delete()
  f=Fouet()
  embed = discord.Embed(title="", color=0xFFCC00)
  embed.set_author(name=ctx.author.display_name+" te fouette", icon_url=ctx.author.avatar_url)
  embed.set_image(url=f.fouette())

  await ctx.channel.send(embed=embed)



@bot.command(name="boude")
async def boude(ctx):
  if disabled_guilds == str(ctx.message.guild.id):
    return
  await ctx.message.delete()
  f=Boude()
  img_url = f.boudeuh()
  print(img_url)
  #await ctx.channel.send(f.boudeuh())
  embed = discord.Embed(title="", color=0xFFCC00)
  embed.set_author(name=ctx.author.display_name+" boude", icon_url=ctx.author.avatar_url)
  embed.set_image(url=img_url)

  await ctx.channel.send(embed=embed)





@bot.command(name="copiersalon")
async def copiersalon(ctx):
  await ctx.message.delete()
  c = ChannelCopy()
  await c.copychannel(ctx.channel, ctx.author)

@bot.command(name="collersalon")
async def collersalon(ctx, *, arg):
  await ctx.message.delete()
  c = ChannelCopy()
  await c.pastechannel(ctx.channel, "Gouhen", arg)
  




@bot.command(name="help")
async def help(ctx):
  e = discord.Embed(title="Aide")
  e.add_field(name="Calcul de bracket", value="Calcule votre bracket en fonction du niveau de vos combattants et de votre salle de formation. Exemple de commande:\n**!bracket 100, 90, 81, 81, 81 sdf 9**", inline=False) 
  
  e.add_field(name="Pourcentage sur forge d'ensemble", value="Calcule le pourcentage de bonus sur un ensemble en fonction des valeurs minimum, maximum et réelle d'un attribut. Exemple :\n**!ensemble 100 10000 5000**", inline=False)
  
  if disabled_guilds != str(ctx.message.guild.id):
    e.add_field(name="Ping-Pong", value="Joue au ping-pong. Commande **!ping**", inline=False)
    e.add_field(name="Fouet", value="Fouette. Commande **!fouet**", inline=False)
    e.add_field(name="Râle", value="Exprime son mécontentement. Commande **!rale**", inline=False)
    e.add_field(name="Boude", value="Exprime son mécontentement d'une manière plus silencieuse. Commande **!boude**", inline=False)
    e.add_field(name="Content", value="Exprime un immense plaisir. Commande **!content** ou **!contente**", inline=False)
  
  await ctx.channel.send(embed=e)

#@bracket.error
#async def bracket_error(ctx, error):
#  await ctx.channel.send("Je ne comprends pas votre demande.\nExemple d'utilisation:\n!bracket 100, 90, 81, 81, 81 sdf 9")



@ensemble.error
async def ensemble_error(ctx, error):
  await ctx.channel.send("Utilisation : !ensemble <min> <max> <tirage>\nExemple : !ensemble 12123 19198 14051")



#repl.it specific
#keep_alive()
bot.run(my_secret)