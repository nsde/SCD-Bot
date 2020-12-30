# Load modules
try:
    import os
    import sys
    import yaml
    import discord

except:
    print("Couldn't load all the libaries. Please install the libaries listed in <root>/requirements.txt.")
    sys.exit(0)

# Some basic defenitions
client = discord.Client()
cwd = os.getcwd()

# Set token
def tokenError():
    print("Please type in a valid bot token.\n\nThe token can be found at config/token.txt. Remember to not give anyone access to this secret file!")
    set_token = input("Token: ")
    with open (cwd + "\\config\\token.txt", "w") as f:
        token = f.write(set_token)

try:
    with open (cwd + "\\config\\token.txt") as f:
        token = f.read()
    print(token)

    if token == "":
        tokenError()

except:
    tokenError()

# Load config
with open(cwd + '\\config\\main.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print("\n\nConfig:\n" + str(data) + "\n\n")

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
    sys.exit(0)