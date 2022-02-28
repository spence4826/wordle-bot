import discord
from discord import Embed, Colour
from discord.ext import commands
from discord.ext.commands import Bot

from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.presences = True

# Loads env file
load_dotenv()

# Sets variables from env file
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

botDescription = 'Best bot that does nothing special.'
helpCommand = commands.DefaultHelpCommand(no_category='Commands', LeaderboardCog='Commands')

# Sets prefix for bot
client = Bot(command_prefix=BOT_PREFIX, intents=intents, help_command=helpCommand, description=botDescription)


# When client comes online
@client.event
async def on_ready():
    # Prints to console that its online
    print(f'{client.user.name} is online!')

    # Sets bot status
    game = discord.Game('wordle')
    await client.change_presence(status=discord.Status.online, activity=game)

    for guild in client.guilds:
        message = guild.name
        for channel in guild.text_channels:
            message += ' - ' + channel.name
        print(message)

        if guild.me.guild_permissions.administrator:
            continue
        if not guild.me.guild_permissions.manage_messages:
            print('I need to be able to manage messages in ' + guild.name + ' - ' + str(guild.id))
        if not guild.me.guild_permissions.add_reactions:
            print('I need to be able to add reactions in ' + guild.name + ' - ' + str(guild.id))
        if not guild.me.guild_permissions.read_message_history:
            print('I need to be able to read message history in ' + guild.name + ' - ' + str(guild.id))

    print('done: started')

