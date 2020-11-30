import discord

client = discord.Client()

# TODO Functionalities
@client.event
async def on_ready():
    playground_channel = client.get_channel(783020045915783179)
    await playground_channel.send("I am online.")
    userList = client.users
    await playground_channel.send("List of online users:")
    for name in userList:
        await playground_channel.send(name)


@client.event
async def on_disconnect():
    playground_channel = client.get_channel(783020045915783179)
    await playground_channel.send("I am offline.")

@client.event
async def on_message(message):
    if message.content == "version":
        playground_channel = client.get_channel(783020045915783179)
        embed = discord.Embed(title="Bot version", description="Version 1.0.0",color=0x00ff00)
        embed.add_field(name="Latest update date:", value="30.11.2020", inline=False)
        embed.set_footer(text="Made by Wasted")
        await playground_channel.send(embed=embed)




client.run("NzgzMDE3MTQwMjk4NTc5OTk5.X8Unig.nGr9fbe-2CBHSY5Tbic92O7DLIc")

