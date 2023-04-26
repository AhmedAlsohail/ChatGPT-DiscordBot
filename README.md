# About The bot
This bot can help to use OpenAI ChatGPT inside Discord rooms, by mentioning it with the question.

![randomQuestion](https://user-images.githubusercontent.com/62726823/232658611-da6197e7-6db5-40d1-869a-6407484d2f95.png)

# Setup the bot
1) install all dependencies in requirements.txt

2) Create .env file:
You must set up your own Discord bot and OpenAI Account by adding **Discord Token & ChatGPT API** inside the .env file in the following format:
```
DISCORD_TOKEN=*YOUR TOKEN*
GPT_API=*YOUR API KEY*
```

3) Run main.py

# History Log
Any question asked will be saved in the following foramt, inside a local text file named **"log.txt"**:

```
2023-04-18 02:26:24
User:
 <@ID> give me 5 random vr games.
GPT:
1. Beat Saber
2. Superhot VR
3. Job Simulator
4. Moss
5. Arizona Sunshine.
```

The History Log can help in:
- Track & Not lose the questions asked through your bot.
- Can help the bot to remember the previous questions when restarted (not yet implemented).
