# Discord Repository

This repository contains everything related to the SERL Discord Server at BTH.

## Oracle

[**The Oracle**](ORACLE.md) contains intended channel structure, role permissions and functionality of the discord bot. Includes comments with reasoning behind selected features.  
Acts as a backup if the Discord Server gets compromised or an authorized user changes unintended settings without documentation.

## discord-bot
A simple bot to manage our SERL discord server

## Build and Run

The easiest way to run the Discord bot is to use Docker.
First, rename `.env.sample` to `.env`.
Then set the environment variable `DISCORD_TOKEN` in the `.env` file with your token.
Finally, you can use the following command to build and run the bot:

```sh
docker compose up
```

### Development
The bot is based on the [discord.py python library](https://discordpy.readthedocs.io/en/stable/index.html#) to get started building our first Discord app. More resources to get started:

- [YouTube Tutorial by Indently](https://www.youtube.com/watch?v=UYJDKSah-Ww&t=1260s)
- [discord-py-interactions](https://pypi.org/project/discord-py-interactions/) which is needed to support Discord's command API (easier to write commands to the bot) [see below](#python-code-using-discords-command-api)

#### Python Code using Discord's command API
```python
bot = commands.Bot(command_prefix='$', intents=intents)
tree = bot.tree
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    await tree.sync()
@tree.command(name='test', description='Test command')
async def test(interaction: discord.Integration):
    await interaction.response.send_message('Test command works!')
```

### Hosting
The discord.py library already include a hosting solution. We don't know how secure this solution is, but it should be sufficent for our needs.

### Functionality
The intentions of the bot is to assist general information like the rules channel. It is to avoid dependency on another discord user who may leave the discord in the future. It will also make the discord server feel a bit more official and fun.

