
import discord
from discord.ext import commands
from discord.utils import get

import traceback
import sys
#from replit import db
import os
#from keep_alive import keep_alive
import re

#from bracketcompute import BracketCompute
#from channelcopy import ChannelCopy
#from rale import Rale, Content, Fouet, Boude

my_secret = os.environ['DA_TOKEN']
#disabled_guilds = os.environ['disabled']

#result = ""

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)
#slash = SlashCommand(bot, sync_commands=True)




#----------------------------------------------------------------------------
#
#   CALCUL DU BRACKET
#
#----------------------------------------------------------------------------

'''
@bot.command(name="bracket")
async def bracket(ctx, *, args):

  #await ctx.channel.send("debug en cours")
  sdfre = re.compile("\s*sdf\s*=*")
  if not sdfre.search(args) :
    await ctx.channel.send("Ne trouve pas 'sdf'\nExemple d'utilisation :\n!bracket 100, 90, 81, 81, 81 sdf 9")
    return
    
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

  b = BracketCompute()# TODO ()
  embed = b.compute(fightersList, trainingRoomLevel)

  
  await ctx.channel.send(embed=embed)

  
#----------------------------------------------------------------------------
#
#   CALCUL DU % D'ENSEMBLE
#
#----------------------------------------------------------------------------
  
'''
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

'''
    
#----------------------------------------------------------------------------
#
#   LE TEST
#
#----------------------------------------------------------------------------


@slash.slash(name="ping", description="Le plus beau jeu du monde")
async def ping(ctx):
  if disabled_guilds == str(ctx.message.guild.id):
    return
  #await ctx.message.delete()
  await ctx.channel.send("pong")


#----------------------------------------------------------------------------
#
#   LES BETISES
#
#----------------------------------------------------------------------------


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




#----------------------------------------------------------------------------
#
#   LA GESTION DES SALONS
#
#----------------------------------------------------------------------------

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
  

@bot.command(name="dupliquercategorie")
async def dupliquercategorie(ctx, *, args):
  
  await ctx.message.delete()
  
  arguments = args.split()

  if len(arguments) != 2:
    await ctx.channel.send("Utilisation : !dupliquercategorie <nom ancienne catégorie> <nom nouvelle catégorie>\nExemple : !dupliquercategorie ancienne nouvelle")
    return
  category = get(ctx.guild.categories, name=arguments[0])

  await category.clone(name=arguments[1], reason="duplicate category")
  await ctx.author.send("Vous avez dupliqué une catégorie")
  


#----------------------------------------------------------------------------
#
#   L'AIDE
#
#----------------------------------------------------------------------------

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




#----------------------------------------------------------------------------
#
#   LA GESTION D'ERREUR
#
#----------------------------------------------------------------------------
  
#@bracket.error
#async def bracket_error(ctx, error):
#  await ctx.channel.send("Je ne comprends pas votre demande.\nExemple d'utilisation:\n!bracket 100, 90, 81, 81, 81 sdf 9")


@bracket.error
async def bracket_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    message = "Vous, ou moi, (le bot), n'avons pas les droits pour exécuter cette commande."
  elif isinstance(error, commands.MissingRequiredArgument):
    message = "Il me faut des paramètres. Exemple d'utilisation :\n!bracket 100, 90, 81, 81, 81 sdf 9"
  else:
    message = "Arrg! Quelque chose a foiré"
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

  await ctx.author.send(message)

@ensemble.error
async def ensemble_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    message = "Vous, ou moi, (le bot), n'avons pas les droits pour exécuter cette commande."
  elif isinstance(error, commands.MissingRequiredArgument):
    message = "Il me faut des paramètres. Exemple d'utilisation :\n!ensemble <min> <max> <tirage>\nExemple concret : !ensemble 12123 19198 14051"
  else:
    message = "Arrg! Quelque chose a foiré"

  await ctx.author.send(message)

@collersalon.error
async def collersalon_error(ctx, error):
  await ctx.channel.send("Il me faut des paramètres")
  
@dupliquercategorie.error
async def dupliquercategorie_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    message = "Vous, ou moi, (le bot), n'avons pas les droits pour exécuter cette commande."
  elif isinstance(error, commands.MissingRequiredArgument):
    message = "Il me faut des paramètres. Exemple d'utilisation :\n!dupliquercategorie categorie-old categorie-new"
  else:
    message = "Arrg! Quelque chose a foiré"

  await ctx.author.send(message)

keep_alive()

'''

bot.run(my_secret)
