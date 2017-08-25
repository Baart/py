import discord
from discord.ext import commands
import datetime


output = "\n New log session " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print output

class Mycog:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def log(self):

        session_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = "\nNew log session " + session_date

        with open('/home/bam/Red-DiscordBot/nohup.out', 'r') as f:
            content = f.read().split('\n')
            lastlines = content[-15:]
            output += '\n'.join(lastlines)

        output += "End of session " + session_date

        await self.bot.say(output)


def setup(bot):
    bot.add_cog(Mycog(bot))


