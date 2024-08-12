import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Define the command prefix

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    await tree.sync()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

bot = commands.Bot(command_prefix='$', intents=intents)
tree = bot.tree
@tree.command(name='testa', description='Test command')
async def test(interaction: discord.Integration):
    await interaction.response.send_message('Test command works!')

# Run the bot
bot.run(TOKEN)
