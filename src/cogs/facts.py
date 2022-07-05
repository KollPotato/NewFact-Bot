from discord.ext.commands import Cog, Bot, command
from discord import Embed
import random


class Facts(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.fact_count = 3090

    def get_facts(self):
        with open("src/facts.txt", "r") as f:
            return f.read().split("\n")

    def get_fact(self, position: int):
        return self.get_facts()[position]

    def get_random_fact(self):
        random_number = random.randint(1, self.fact_count)
        return self.get_fact(random_number)

    @command("fact")
    async def fact(self, ctx, amount: int = 1):

        embed = Embed()
        embed.title = "Did you know that?"
        embed.description = self.get_random_fact()
        embed.color = 0x615cff

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Facts(bot))