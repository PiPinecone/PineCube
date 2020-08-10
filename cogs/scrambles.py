from discord.ext import commands
import random


def convert(lizt):
    return ' '.join(lizt)


def scram(small, large):
    moves = (('U', 'D'), ('F', 'B'), ('R', 'L'))
    directions = ('', "'", '2')
    scramble_length = random.randint(small, large)

    def group_find(move):
        temp = moves[0]
        if move[0] in temp:
            return moves[0]
        else:
            temp = moves[1]
            if move[0] in temp:
                return moves[1]
            else:
                return moves[2]

    scramble = []
    for i in range(scramble_length):
        if i == 0:
            scramble.append(random.choice(random.choice(moves)) + random.choice(directions))
        else:
            while True:
                move = random.choice(moves)
                if move != group_find(scramble[i - 1]):
                    scramble.append(random.choice(move) + random.choice(directions))
                    break

    s3 = "**" + convert(scramble) + "**"
    return s3


class Scrambles(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
        name="3x3",
        aliases=['3', '3X3', '3x', '3X', 'Three', 'three', 'THREE']
    )
    @commands.guild_only()
    async def scram3x3(self, ctx: commands.Context):
        await ctx.send(scram(17, 25))

    @commands.command(
        name="2x2",
        aliases=['2', '2X2', '2x', '2X', 'Two', 'two', 'TWO']
    )
    @commands.guild_only()
    async def scram2x2(self, ctx: commands.Context):
        await ctx.send(scram(9, 10))

    @commands.command(
        name="1x1",
        aliases=['1', '1X1', '1x', '1X', 'One', 'one', 'ONE']
    )
    @commands.guild_only()
    async def scr1(self, ctx: commands.Context):
        await ctx.send("No. That's stupid.")


def setup(client: commands.Bot):
    client.add_cog(Scrambles(client))
