
import os
import time
import psycopg2

class ChannelCopy:

  async def copychannel(self, interaction):
    time.sleep(1)
    #channel = client.get_channel(123456789101112131)
    messages = await interaction.channel.history(limit=50, oldest_first=True).flatten()

    count = 0
    tuples = []
    for message in messages:
      if message.content:
        count = count +1
        #key = "{}-{:05d}".format(channel.id, count)
        #print("{} => {}".format(key, message.content))
        #db[key] = message.content
        tuples.append((channel.id, message.content))

      for attachment in message.attachments:
        if attachment.url :
          count = count +1
          #key = "{}-{:05d}".format(channel.id, count)
          #db[key] = attachment.url
          #print("{} => {}".format(key, attachment.url))
          tuples.append((channel.id, attachment.url))

    if tuples:
        DATABASE_URL = os.environ['DATABASE_URL']
        try:
            conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = conn.cursor()
            cur.executemany("INSERT INTO messages (channel_id, content) VALUES(%s,%s)", tuples)
            cur.close()

            conn.commit()

            #TODO tester un truc genre
            #args_str = ','.join(cur.mogrify("(%s,%s)", x) for x in tuples)
            #cur.execute("INSERT INTO messages VALUES " + args_str)
            await interaction.response.send_message(f"Vous avez enregistré {count} messages du salon {channel.id}. Pour les coller quelque part, utilisez la commande :\n!collersalon {channel.id}", ephemeral=True)

        except (Exception, psycopg2.DatabaseError) as error:
            await interaction.response.send_message(f"Problème lors de la copie du salon : {error}", ephemeral=True)
        finally:
            if conn is not None:
                conn.close()
    time.sleep(1)

  async def pastechannel(self, interaction, recordId):
    DATABASE_URL = os.environ['DATABASE_URL']
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute("SELECT content FROM messages WHERE channel_id = %s order by id", (recordId,))
        records = cur.fetchall()
        for message in records:
            if message:
                time.sleep(1)
                await interaction.channel.send(message[0])

        cur.execute("DELETE FROM messages WHERE channel_id = %s", (recordId,))
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        await interaction.response.send_message(f"Problème lors de la récupération des messages : {error}", ephemeral=True)
    finally:
        if conn is not None:
            conn.close()

