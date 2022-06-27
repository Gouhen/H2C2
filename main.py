import sys
import os
import shlex
import re
import time

import discord
from discord.ext import commands
from dotenv import load_dotenv
import psycopg2


from bracketcompute import BracketCompute
from rale import Rale, Content, Fouet, Boude, Rencard, Flower

load_dotenv()

token = os.getenv("token")
disabled_guilds = os.getenv("disabled")

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
#   Initialisation de la BDD
#
#----------------------------------------------------------------------------
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()
cur.execute(
"""
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    channel_id VARCHAR(255) NOT NULL,
    content VARCHAR(3000) NOT NULL
)
"""
)
cur.close()
conn.commit()
conn.close()
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


@bot.command(name="rencard")
async def rencard(ctx):
  if disabled_guilds == str(ctx.message.guild.id):
    return
  await ctx.message.delete()
  r=Rencard()
  #await ctx.channel.send()
  embed = discord.Embed(title=r.donot(), color=0xFF5733)
  embed.set_author(name=ctx.author.display_name+" a son premier rencard depuis un moment", icon_url=ctx.author.avatar_url)

  await ctx.channel.send(embed=embed)


@bot.command(name="bouquet")
async def bouquet(ctx):
  if disabled_guilds == str(ctx.message.guild.id):
    return
  await ctx.message.delete()
  f=Flower()
  #await ctx.channel.send()
  embed = discord.Embed(title=f.potDeFlower(), color=0xFF0000)
  embed.set_author(name=ctx.author.display_name+" t'offre une joli fleur", icon_url=ctx.author.avatar_url)

  await ctx.channel.send(embed=embed)


#----------------------------------------------------------------------------
#
#   LA GESTION DES SALONS
#
#----------------------------------------------------------------------------

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

@bot.command(name="aide")
async def aide(ctx):
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