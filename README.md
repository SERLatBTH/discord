# Discord Repository
This repository contains everything related to the SERL Discord Server at BTH.  At the time there is some oracles for intended channel structure and role permissions, as well as a development on a discord bot. 

## Oracles
- [ ] Add Channel Structure Oracle
- [ ] Add Role Permissions Oracle

## discord-bot
A simple bot to manage our SERL discord server

## Build and Run

The easiest way to run the Discord bot is to use Docker.
First, set the environment variable `DISCORD_TOKEN` in the `compose.yml` file with your token.
Then you can use the following command to build and run the bot:

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

