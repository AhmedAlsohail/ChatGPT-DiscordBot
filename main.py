import os, datetime
import discord
import openai as gpt
from dotenv import load_dotenv

# Set Up discord
intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)
 
# Load Tokens
load_dotenv(".env")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
gpt.api_key = os.getenv("GPT_API")

# Client Events
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if client.user in message.mentions:
        await message.channel.typing() # Appear as typing while processing.

        # Save user message in the log
        chat_log = []
        chat_log.append({"role" : "user", "content" : message.content})

        # Get response
        response = gpt.ChatCompletion.create(
             model ="gpt-3.5-turbo",
             messages = chat_log
             )   
        gptResponse = response['choices'][0]['message']['content']

        # Save Response message in the log
        chat_log.append({"role" : "assistant", "content": gptResponse.strip("\n").strip()})

        # Send Response to discord room.
        await message.channel.send("``` {} ```".format(gptResponse))

        # Append to log file
        with open("log.txt", "a", encoding='utf-8') as file:
            now = datetime.datetime.now()
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
            file.write("\nUser:\n {}.\n".format(message.content))
            file.write("GPT:\n {}.\n\n".format(gptResponse))

# Run the client
client.run(DISCORD_TOKEN)