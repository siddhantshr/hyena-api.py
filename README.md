# Hyena API Wrapper

## ❓| Hyena API

*The Hyena API is an API made by Donut#4427 for stuff like:*

* Chatbot
* NSFW

*To use the Hyena API you can visit [this page](https://www.hyenabot.xyz/api). And to get more info on it you can visit the [Docs!](https://docs.hyenabot.xyz/)*

*And to see how the hyena-bot works and test it out visit the official [Discord server](https://discord.gg/QePftyb2kN)!*

## Installing
### **Python 3.8 or higher is required**

To install the library use the following commands:

```
To be filled
```

To install from the master branch do this:
```
$ git clone https://github.com/AHiddenDonut/hyena-api.py.py hyena-api
$ cd hyena-api
$ python3 -m pip install -U .
```

## Examples

*Some quick examples to show how you can use the api*

```python
import hyena

hyena = hyena.Client("MY SUPER SECRET API KEY")

# Chatbot response
resp = hyena.chatbot("Hello!", name="My bot's name", owner="My name")
print(resp)
```

```python
import hyena

hyena = hyena.Client("MY SUPER SECRET API KEY")

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

## Links

* [Documentation](https://docs.hyenabot.xyz/)
* [Official Server](https://discord.gg/QePftyb2kN)
* [API Link](https://www.hyenabot.xyz/api)