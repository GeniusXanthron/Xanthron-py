import lightbulb
import os
import subprocess

bot = lightbulb.BotApp(
    token="code",
    default_enabled_guilds=(this)
    )

@bot.command
@lightbulb.command('start', 'Starts the Minecraft server')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Opened!')
    await subprocess.call(['C:\Program Files\Mozilla Firefox\\firefox.exe'])

bot.run()