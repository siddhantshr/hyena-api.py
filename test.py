import hyena.Async, asyncio, discord
from discord.ext import commands

# client = hyena.Async.Client("KGgGT#FnFE_z2BdcERAqeZvYmU6D0Q")
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print('ready')
    async with hyena.Async.Client("KGgGT#FnFE_z2BdcERAqeZvYmU6D0Q") as client:
        async with (await client.nsfw("ass", format="image")) as resp:
            print(str(resp))

bot.run("ODM0NDMzODI2MTU5NDYwNDEy.YIA1Dw.C-y_WYB5slrNgoooVvN9FL8p-a4")