import os
import time
import datetime
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
def load_discord_token():
    try:
        return os.environ["DISCORD_TOKEN"]
    except KeyError:
        raise NameError("DISCORD_TOKEN env does not exist. Unable to proceed.")

MY_GUILD = discord.Object(id=os.environ["GUILD_ID"])
# +++++++++++ Client Setup +++++++++++ #
class Bot(discord.Client):
    def __init__(self, *, intents: discord.Intents, guild: discord.Guild = None):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.guild = guild

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=self.guild)
        #self.tree.clear_commands(guild=None)
        #self.tree.clear_commands(guild=self.guild) # clears guild commands
        await self.tree.sync(guild=self.guild)
    


intents = discord.Intents.default()
# intents.members = True
intents.message_content = True
bot = Bot(intents=intents, guild=MY_GUILD)
# +++++++++++ Client Setup +++++++++++ #

@bot.tree.command(description='Shows you what commands you can use.')
async def help(interaction: discord.Interaction):
    rnd_hex = 0x00ff00
    embed = discord.Embed(title='Commands  |  Help\n-=-=-=-=-=-=-=-=-=-=-=-=-=-', colour=rnd_hex, timestamp=datetime.datetime.now(datetime.timezone.utc))
    # embed.set_thumbnail(url=bot_logo)
    embed.add_field(name='\u200B\n/judgement help', value="Shows you a help message for judgement commands.", inline=False)
    embed.add_field(name='\u200B\n/ticket <title> <message>', value="Creates a support ticket", inline=False)
    embed.add_field(name='\u200B\n/report <userId> <message_Id> <channel_Id> (screenshot link)', value="Reports a user to staff.", inline=False)
    embed.add_field(name='\u200B\n/orb', value="Ask a question, get an answer.", inline=True)
    embed.add_field(name='\u200B\n/flip', value="Flips a coin for 'Heads' or 'Tails'.", inline=True)
    embed.add_field(name='\u200B\n/rmbg <image>', value="Remove the background from images.", inline=True)
    embed.add_field(name='\u200B\n/glcvrt <message> (option)', value="Will convert your message to and from the galactic alphabet.", inline=False)
    # embed.set_footer(text=__authors__, icon_url=author_logo)
    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.tree.command(description='Shows you what commands you can use.')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"⏱️ Pong! ⏱️\nConnection speed is {round(bot.latency * 1000)}ms", ephemeral=True)

if __name__ == '__main__':
    token = load_discord_token()
    bot.run(token, reconnect=True)
    print('Bot exited on ' + time.strftime('%Y-%m-%d %H:%M:%S'))