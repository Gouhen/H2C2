import sys
import os
import shlex
import re
import time
from typing import Optional

import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
#import psycopg2

#from channelcopy import ChannelCopy

from bracketcompute import BracketCompute
from rale import Rale
from content import Content
from fouet import Fouet
from boude import Boude
from rencard import Rencard
from flower import Flower

load_dotenv()

token = os.getenv("token")
disabled_guilds = os.getenv("disabled")


class h2g2client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"{self.user} connecté")

client = h2g2client()
tree = app_commands.CommandTree(client)



#----------------------------------------------------------------------------
#
#   LES BETISES
#
#----------------------------------------------------------------------------

@tree.command(name = "content", description="Exprimer sa joie au masculin", )
async def self(interaction: discord.Interaction):

    c=Content()

    embed = discord.Embed(title=c.happy(), color=0x33CC00)
    embed.set_author(name=f"{interaction.user.display_name} est content!", icon_url=interaction.user.display_avatar)

    await interaction.response.send_message(embed=embed)


@tree.command(name = "contente", description="Exprimer sa joie au féminin", )
async def self(interaction: discord.Interaction):

    c=Content()

    embed = discord.Embed(title=c.happy(), color=0x33CC00)
    embed.set_author(name=f"{interaction.user.display_name} est contente!", icon_url=interaction.user.display_avatar)

    await interaction.response.send_message(embed=embed)


@tree.command(name = "fouet", description="Rendre la justice!", )
async def self(interaction: discord.Interaction, destinataire:Optional[discord.Member] = None):

    if destinataire:
        message = f"{interaction.user.display_name} fouette {destinataire.display_name}, parce que c'est mérité!"
    else:
        message = f"{interaction.user.display_name} te fouette!"

    f=Fouet()
    embed = discord.Embed(title="", color=0xFFCC00)
    embed.set_author(name=message, icon_url=interaction.user.display_avatar)
    embed.set_image(url=f.fouette())

    await interaction.response.send_message(embed=embed)


@tree.command(name = "boude", description="Exprimer son mécontentement silencieusement", )
async def self(interaction: discord.Interaction):

    f=Boude()
    img_url = f.boudeuh()

    embed = discord.Embed(title="", color=0xFFCC00)
    embed.set_author(name=f"{interaction.user.display_name} boude", icon_url=interaction.user.display_avatar)
    embed.set_image(url=img_url)

    await interaction.response.send_message(embed=embed)


@tree.command(name = "rencard", description="Mais que dire lors de ton prochain rencard?", )
async def self(interaction: discord.Interaction):

    r=Rencard()

    embed = discord.Embed(title=r.donot(), color=0xFF5733)
    embed.set_author(name=f"{interaction.user.display_name} a son premier rencard depuis un moment", icon_url=interaction.user.display_avatar)

    await interaction.response.send_message(embed=embed)


@tree.command(name = "bouquet", description="Offrir une belle fleur", )
async def self(interaction: discord.Interaction, destinataire:Optional[discord.Member] = None):

    if destinataire:
        message = f"Tiens {destinataire.display_name}, voilà une zouli fleur de la part de {interaction.user.display_name}!"
    else:
        message = f"{interaction.user.display_name} vous offre une zouli fleur!"

    f=Flower()

    embed = discord.Embed(title="", color=0xFF0000)
    embed.set_author(name=message, icon_url=interaction.user.display_avatar)
    embed.set_image(url=f.flowers())

    await interaction.response.send_message(embed=embed)


@tree.command(name = "rale", description="Exprimer son mécontentement", )
async def self(interaction: discord.Interaction):

    r=Rale()

    embed = discord.Embed(title=r.shout(), color=0xFF5733)
    embed.set_author(name=f"{interaction.user.display_name} en a gros", icon_url=interaction.user.display_avatar)

    await interaction.response.send_message(embed=embed)


#----------------------------------------------------------------------------
#
#   CALCUL DU BRACKET
#
#----------------------------------------------------------------------------

@tree.command(name = "bracket", description="calculer un bracket d'arène", )
@app_commands.rename(levels='niveaux', training_room='salle_de_formation')
@app_commands.describe(levels='Niveaux des combattants séparés par des espaces. Exemple : 100 90 81 81 81', training_room='Niveau de la salle de formation. Exemple : 9')
async def self(interaction: discord.Interaction, levels:str, training_room:int):

    spacere = re.compile("\s*,\s*|\s+")
    fl = spacere.split(levels)
    #await ctx.channel.send(fl)


    fightersList = []
    for i in range(len(fl)):
        if fl[i].isdigit():
            fightersList.append(int(fl[i]))

    if not fightersList:
        await interaction.response.send_message("Je ne trouve pas la liste des niveaux de combattants\nExemple d'utilisation :\n/bracket puis 100 90 81 81 81 dans niveaux, puis 9 dans salle de formation", ephemeral=True)
        return

    b = BracketCompute()# TODO ()
    embed = b.compute(fightersList, training_room)


    await interaction.response.send_message(embed=embed)


#----------------------------------------------------------------------------
#
#   CALCUL DU % D'ENSEMBLE
#
#----------------------------------------------------------------------------

@tree.command(name = "ensemble", description="calcul du pourcentage de bonus d'un ensemble", )
@app_commands.rename(min='minimum', max='maximum', value='valeur')
@app_commands.describe(min="minimum possible d'un attribut (dans l'écran de droite)", max="maximum possible d'un attribut (dans l'écran de droite)", value="valeur de l'attribut (dans l'écran de gauche)")
async def self(interaction: discord.Interaction, min:int, max:int, value:int):

    percentage = round((value-min)*100.0 / (max-min), 2)

    if percentage < 30:
        message = f"**{percentage}%**.   :scream:"
    elif percentage < 60:
        message = f"**{percentage}%**.   :slight_smile:"
    elif percentage < 80:
        message = f"**{percentage}%**.   :grinning:"
    else:
        message = f"**{percentage}%**.   :star_struck:"

    await interaction.response.send_message(message)



#----------------------------------------------------------------------------
#
#   LA GESTION DES SALONS
#
#----------------------------------------------------------------------------


# @tree.command(name = "copiersalon", description="Copier les 50 derniers messages du salon", )
# async def self(interaction: discord.Interaction):

    # if not interaction.user.guild_permissions.manage_channels:
        # await interaction.response.send_message("Vous n'avez pas les droits pour utiliser cette commande", ephemeral=True)
        # return

    # c = ChannelCopy()
    # await c.copychannel(interaction)


# @tree.command(name = "collersalon", description="Copier les 50 derniers messages du salon", )
# @app_commands.rename(room_id='identifiant')
# @app_commands.describe(room_id='identifiant du salon copié préalablement')
# async def self(interaction: discord.Interaction, room_id:int):


    # if not interaction.user.guild_permissions.manage_channels:
        # await interaction.response.send_message("Vous n'avez pas les droits pour utiliser cette commande", ephemeral=True)
        # return

    # c = ChannelCopy()
    # await c.pastechannel(interaction, room_id)



# @tree.command(name = "dupliquercategorie", description="Duplique une catégorie existante, avec les droits et tout", )
# async def self(interaction: discord.Interaction, categorie_existante:str, nom_nouvelle_categorie:str):

    # if not interaction.user.guild_permissions.manage_channels:
        # await interaction.response.send_message("Vous n'avez pas les droits pour utiliser cette commande", ephemeral=True)
        # return

    # category = get(interaction.guild.categories, name=categorie_existante)

    # await category.clone(name=nom_nouvelle_categorie, reason="duplicate category")
    # await interaction.response.send_message("Vous avez dupliqué une catégorie", ephemeral=True)




client.run(token)

#----------------------------------------------------------------------------
#
#   Initialisation de la BDD
#
#----------------------------------------------------------------------------
# DATABASE_URL = os.environ['DATABASE_URL']
# def create_tables():
    # sqls = (
        # """
        # CREATE TABLE IF NOT EXISTS messages (
            # id SERIAL PRIMARY KEY,
            # channel_id VARCHAR(255) NOT NULL,
            # content VARCHAR(3000) NOT NULL
        # )
        # """,
    # )

    # try:
        # conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        # cur = conn.cursor()

        # print('PostgreSQL database version:')
        # cur.execute('SELECT version()')
        # db_version = cur.fetchone()
        # print(db_version)

        create table one by one
        # for sql in sqls:
            # cur.execute(sql)
        close communication with the PostgreSQL database server
        # cur.close()
        commit the changes
        # conn.commit()
    # except (Exception, psycopg2.DatabaseError) as error:
        # print(error)
    # finally:
        # if conn is not None:
            # conn.close()




# create_tables()