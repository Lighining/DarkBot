import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio 
import random

bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():   
    print ("Bot is Ready = True")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    print ("-------------------------------------------------------")
    print ("Please run &ping to make sure the bot started properly!")
    await bot.change_status(game=discord.Game(name="Do &commands for help!", url="twitch.tv/streamer", type=1))

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong! :tada:")
    print ("User has pinged")

@bot.command(pass_context=True)
async def dev(ctx):
    await bot.say("Developer: xRedFlame_PvPx#2680 | Owner: Yqllow#4403")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Info:")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context = True)
async def clear(ctx, number):
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await bot.delete_message(x)
            counter += 1
            await asyncio.sleep(1.2) #1.2 second timer so the deleting process can be even
            await bot.say("Cleared :thumbsup:!")

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say(":boot: OUT OF MY WAY, {}. Ya loser!".format(user.name))
    await bot.kick(user)

@bot.command(pass_contexct=True)
async def invite(ctx):
    await bot.say("Here invite me via https://discordapp.com/api/oauth2/authorize?client_id=428321056831438849&permissions=8&scope=bot".ctx(parm))
    print ("User wanted DarkBot!")

@bot.command(pass_contexct=True)
async def shutdown(ctx):
    await bot.say("Bot shutting down... :zzz: ")

@bot.command()
async def echo(message: str):
    await bot.say(message)

@bot.command(pass_context=True)
async def members(ctx):
    amount = len(ctx.message.server.members)
    await bot.say('There are ' + str(amount) + ' members.')

@bot.event
async def on_message(message):
    if message.content.startswith('&commands'):
        embed = discord.Embed(title="Read This:", description="Here are all my commands", color=0x00ff00)
        embed.add_field(name="ping:", value="ping, pings the bot to make sure it's online!", inline=False)
        embed.add_field(name="dev:", value="Shows the Developer and Owner!", inline=False)
        embed.add_field(name="members:", value="Shows how many members your discord has!", inline=False)
        embed.add_field(name="ban:", value="Ban a member from your discord", inline=False)
        embed.add_field(name="kick:", value="Kick a member from your discord", inline=False)
        embed.add_field(name="echo:", value="Echo, the bot repeats the word you say", inline=False)
        embed.add_field(name="clear:", value="Clears/puges messages!", inline=False)
        embed.add_field(name="serverinfo", value="Serverinfo tells you info about your server", inline=False)
        embed.add_field(name="info:", value="Info, tells you your user info! (Not Password if your stupid)", inline=False)
        await bot.send_message(message.channel, embed=embed)

bot.run("NDI4MzIxMDU2ODMxNDM4ODQ5.DZxYlw.eKKasYYVRM_rbdnihjLVErziHNk")
