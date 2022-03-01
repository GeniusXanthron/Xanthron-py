import lightbulb
import os
import subprocess

bot = lightbulb.BotApp(
    token="OTQ1NDg3MTUyMTE0OTgyOTUy.YhQ3hw.0YDX9zIZnmXqphqHrqWxTeowgfA",
    default_enabled_guilds=(856435723241652225)
    )

@bot.command
@lightbulb.command('start', 'Starts the Minecraft server')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Opened!')
    await subprocess.call(['C:\Program Files\Mozilla Firefox\\firefox.exe'])

bot.run()