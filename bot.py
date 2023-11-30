import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        print(f'message from {message.author}; {message.content}')
        channel = message.channel
        await channel.send ('hello bro')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTE3OTU3NDkzNTIxMjAxOTc2Mw.GCQNQx.0_MqVlZFTWyl73keCiTTrFykb8ZYzM1o858eIc')

#id: 1179574935212019763
#key: 0365f0a03d18b849ee86f4a5e38eaca5b09a080166813117a62d3dfd4a12f053
