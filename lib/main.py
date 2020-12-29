# Load modules
try:
    import os
    import sys
    import yaml
    import discord

except:
    print("Couldn't load all the libaries. Please install the libaries listed in <root>/requirements.txt.")
    sys.exit(0)

# Set token
# try:
token = os.environ.get("scdtoken")
print(token)

# except:
print("Please type in a valid bot token. The token can be found at the Discord Developer Portal at 'applications/<application id>/bot'.")
print("Type in a bot token or press enter to skip.")
set_token = input()
if set_token != "":
    os.environ["scdtoken"] = set_token
    print("Updated the 'scdtoken' to '" + os.environ["scdtoken"] + "'.")
    sys.exit(0)

cwd = os.getcwd()

# Load config
with open(cwd + '\\config\\main.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

try:
    client.run(token)

except:
    print("ERROR: Unable to run the client. Did you input a invalid token?")