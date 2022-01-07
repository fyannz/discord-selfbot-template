# DISCORD SELFBOT TEMPLATE BY fyann#5319
# For 'discord.ext commands' docs, here: https://discordpy.readthedocs.io/en/stable/ext/commands/index.html

# Default prefix: !

# import module
import discord
from discord.ext import commands


token = "your_token_here"         # use your account token, not bot.
client = commands.Bot(command_prefix="!", self_bot=True, help_command=None) # you can edit prefix after 'command_prefix'

# Print message on Console if the bot online
@client.event
async def on_ready():
    print("Online!")
    print("by fyann")

# Ping Command (!ping)
@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

# embedSay Command (!embedsay)
@client.command(case_insensitive=True)
async def embedsay (ctx, saymsg=None):
    if saymsg==None:
        return await ctx.send("add some text lol")
        
    sayEmbed = discord.Embed(color = discord.Color.blue(), description=f"{saymsg}")
    await ctx.send(embed = sayEmbed)
   
client.run(token, bot=False)        # this function will activate the selfbot.