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
    #await client.send_message(ctx.message.channel, "Suhhhh dude", tts=True)

#May move these to a different .py.  Create a function instead would be better.
#Trigger Dad/Robert Joke for "I'm Back"


# async def on_message(message):
#
# #Define normal person's correct grammar.  It's in incorrect case to save using .lower()
#     trigger = "i'm back"
# #Define degenerate speak
#     grammar_terrorist_trigger = "im back"
# #Get the message, convert it to str, change it to lowercase, and then overwrite the original message.
#     message.content=message.content.lower();
# #!!!!IMPORTANT!!!! Make sure to define the dad joke below!!! I added it there so it's only created if the if statement returns true
# #Can probably move here if it doesn't make a difference for the sake of readability
#
#
#
# #If the message contains @trigger or @grammer_terrorist_trigger, send the Dad Joke
#     if (trigger or grammar_terrorist_trigger in message.content):
# #Define dad joke.  Have not tested this concatenation or event what self returns.
#         dad_Joke= "Hi back, I'm" + client.user.name
# # Send the dad joke
#         await client.send_message(message.channel, dad_Joke)

client.run(token)

