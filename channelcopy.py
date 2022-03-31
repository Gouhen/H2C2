from replit import db

class ChannelCopy:
  async def copychannel(self, channel, author):
    #channel = client.get_channel(123456789101112131)
    messages = await channel.history(limit=50, oldest_first=True).flatten()

    count = 0
    for message in messages:
      if message.content:
        count = count +1
        key = "{}-{:05d}".format(channel.id, count)
        #print("{} => {}".format(key, message.content))
        db[key] = message.content
        
      for attachment in message.attachments:
        if attachment.url :
          count = count +1
          key = "{}-{:05d}".format(channel.id, count)
          db[key] = attachment.url
          print("{} => {}".format(key, attachment.url))

    await author.send("Vous avez enregistré {} messages du salon {}. Pour les coller quelque part, utilisez la commande :\n!collersalon {}".format(count, channel.id, channel.id))

  async def pastechannel(self, channel, author, recordId):
    matches = db.prefix(recordId)
    #print(f"liste: %s" % (matches,))
    for key in sorted(matches):
      message = db[key]
      #print("{} => {}".format(key, message))
      if message:
        await channel.send(message)

    for key in matches:
      del db[key]
