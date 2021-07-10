# Hyena API Wrapper

## ❓| Hyena API

_The Hyena API is an API made by Donut#4427 for stuff like:_

- Chatbot
- NSFW

_To use the Hyena API you can visit [this page](https://www.hyenabot.xyz/api). And to get more info on it you can visit the [Docs!](https://docs.hyenabot.xyz/)_

_And to see how the hyena-bot works and test it out visit the official [Discord server](https://discord.gg/QePftyb2kN)!_

## Installing

### **Python 3.8 or higher is required**

To install the library use the following commands:

```
pip install hyena-api.py
# or
pip install hyena-api.py==version
```

To install from the master branch do this:

```
$ git clone https://github.com/AHiddenDonut/hyena-api.py.py hyena-api
$ cd hyena-api
$ python3 -m pip install -U .
```

## Examples

_Some quick examples to show how you can use the api_

### Sync:
```python
import hyena.Sync

hyena = hyena.Sync.Client("MY SUPER SECRET API KEY")

# Chatbot response
resp = hyena.chatbot("Hello!", name="My bot's name", owner="My name")
print(resp)
```

```python
import hyena.Sync

hyena = hyena.Sync.Client("MY SUPER SECRET API KEY")

# NSFW images
resp = hyena.nsfw("endpoint", format="json") # format will be a class by default
print(resp)

"""
How to use the response class [Default]

resp.title : Title of response
resp.description : Description of response
resp.image_url : Image URL of response
resp.url : url of the original post
"""
```

### Async:
```py
import hyena.Async, asyncio

async def main():
    async with hyena.Async.Client("KGgGT#FnFE_z2BdcERAqeZvYmU6D0Q") as client:
        async with (await client.nsfw("random", format="image")) as resp:
            pass # stuff
```

```py
import hyena.Async, asyncio

async def main():
    async with hyena.Async.Client("KGgGT#FnFE_z2BdcERAqeZvYmU6D0Q") as client:
        async with (await client.chatbot("hello world")) as resp:
            pass # stuff
```

```py
# with discord.py:
import hyena.Async

hyena = hyena.Async.Client("MY SUPER SECRET API KEY")

@client.command()
async def chatbot(ctx, *, message):
    my_reply = await hyena.chatbot(message, language="en", owner="myname", name="my bot's name")
    await ctx.reply(my_reply)


## Links

- [Documentation](https://docs.hyenabot.xyz/)
- [Official Server](https://discord.gg/QePftyb2kN)
- [API Link](https://www.hyenabot.xyz/api)