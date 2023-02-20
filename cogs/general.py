from discord.ext import commands
import discord

class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

async def setup(bot):
    await bot.add_cog(general(bot))
