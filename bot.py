import discord
from discord.ext import commands
from bot_config import token

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("-------------------------------------")

# ping command
@client.command(pass_context = True)
async def ping(ctx):
    await client.say("Hello!")
    # tts version:
    #await client.send_message(ctx.message.channel, "Hello!", tts=True)

client.run(token)
