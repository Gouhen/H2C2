import sys
import os
import shlex
import re
import time

import discord
from discord.ext import commands
from dotenv import load_dotenv


from bracketcompute import BracketCompute

load_dotenv()

token = os.getenv("token")

#client = discord.Client()
#
#@client.event
#async def on_ready():
## Print this when the bot starts up for the first time.
#    print(f'{client.user} has connected to Discord!')
#
#@client.event
#async def on_message(message):
## Ignore messages from the bot itself so that there's no conflict.
#    if message.author == client.user:
#        return
## Respond to hello.
#    if message.content == 'coucou':
#        await message.channel.send("Wesh gros!")
#
bot = commands.Bot(command_prefix='!', help_command=None)


#----------------------------------------------------------------------------
#
#   CALCUL DU BRACKET
#
#----------------------------------------------------------------------------


@bot.command(name="bracket")
async def bracket(ctx, *, args):
  print(f"{ctx.author.display_name} : bracket")

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


@bot.command(name="ensemble")
async def ensemble(ctx, *, args):
  print(f"{ctx.author.display_name} : ensemble")
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



@bot.command(name="aide")
async def aide(ctx):
  print(f"{ctx.author.display_name} : aide")
  e = discord.Embed(title="Aide")
  
  e.add_field(name="Calcul de bracket", value="Calcule votre bracket en fonction du niveau de vos combattants et de votre salle de formation. Exemple de commande:\n**!bracket 100, 90, 81, 81, 81 sdf 9**", inline=False) 

  e.add_field(name="Pourcentage sur forge d'ensemble", value="Calcule le pourcentage de bonus sur un ensemble en fonction des valeurs minimum, maximum et réelle d'un attribut. Exemple :\n**!ensemble 100 10000 5000**", inline=False)

  await ctx.channel.send(embed=e)

#----------------------------------------------------------------------------
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
#----------------------------------------------------------------------------
@ensemble.error
async def ensemble_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    message = "Vous, ou moi, (le bot), n'avons pas les droits pour exécuter cette commande."
  elif isinstance(error, commands.MissingRequiredArgument):
    message = "Il me faut des paramètres. Exemple d'utilisation :\n!ensemble <min> <max> <tirage>\nExemple concret : !ensemble 12123 19198 14051"
  else:
    message = "Arrg! Quelque chose a foiré"

  await ctx.author.send(message)


bot.run(token)
#client.run(token)