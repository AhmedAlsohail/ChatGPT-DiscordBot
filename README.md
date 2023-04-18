# About The bot
This bot can help to use OpenAI ChatGPT inside Discord rooms, by mentioning it with the question.

![randomQuestion](https://user-images.githubusercontent.com/62726823/232658611-da6197e7-6db5-40d1-869a-6407484d2f95.png)

# Setup the bot
You must set up your own bot and OpenAI Account by adding **Discord Token & ChatGPT API** inside the .env file

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

This will help to not lose the questions & can help the bot to remember the previous questions when restarted (not yet implemented).
