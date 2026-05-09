# hyena-api.py

> A lightweight Python wrapper for the [Hyena API](https://www.hyenabot.xyz/api) — supporting both synchronous and asynchronous usage.

[![PyPI version](https://img.shields.io/pypi/v/hyena-api.py)](https://pypi.org/project/hyena-api.py/)
[![Python](https://img.shields.io/pypi/pyversions/hyena-api.py)](https://pypi.org/project/hyena-api.py/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

---

## 📖 About

**hyena-api.py** is a Python client library that wraps the [Hyena API](https://www.hyenabot.xyz/api), originally built by Donut#4427. It provides a clean, Pythonic interface to:

- 🤖 **Chatbot** — Get AI-generated replies to messages, with optional language, bot name, and owner customisation.
- 🖼️ **NSFW image fetching** — Retrieve images from Reddit-based endpoints, returning results as a structured class, raw JSON, or a direct image URL.

The library ships with both a **synchronous** client (backed by `requests`) and an **asynchronous** client (backed by `aiohttp`), making it easy to integrate into scripts, bots, or async applications like those built with `discord.py`.

---

## 🔗 Links

| Resource | URL |
|---|---|
| PyPI | https://pypi.org/project/hyena-api.py/ |
| API Documentation | https://docs.hyenabot.xyz/ |
| API Key Registration | https://www.hyenabot.xyz/api |
| Official Discord Server | https://discord.gg/QePftyb2kN |
| Source Code | https://github.com/AHiddenDonut/hyena-api.py |

---

## ⚙️ Requirements

- Python **3.6** or higher
- `requests >= 2.25.1`
- `aiohttp >= 3.7.4`

---

## 📦 Installation

Install the latest stable release from PyPI:

```bash
pip install hyena-api.py
```

Install a specific version:

```bash
pip install hyena-api.py==1.1.0
```

Install the latest development version directly from GitHub:

```bash
git clone https://github.com/AHiddenDonut/hyena-api.py hyena-api
cd hyena-api
pip install -U .
```

---

## 🚀 Quick Start

### Synchronous client

```python
from hyena.Sync import Client

client = Client("YOUR_API_KEY")

# Chatbot
reply = client.chatbot("Hello!", name="MyBot", owner="MyName", language="en")
print(reply)  # prints the bot's text reply

# NSFW — returns a NsfwResponse object by default
resp = client.nsfw("random")
print(resp.title)
print(resp.image_url)
print(resp.url)

# NSFW — return raw image URL
url = client.nsfw("random", format="image")
print(url)

client.close()
```

### Asynchronous client

```python
import asyncio
from hyena.Async import Client

async def main():
    async with Client("YOUR_API_KEY") as client:
        # Chatbot
        reply = await client.chatbot("Hello!", language="en", name="MyBot", owner="MyName")
        print(reply)

        # NSFW — returns a NsfwResponse object by default
        resp = await client.nsfw("random")
        print(resp.title)
        print(resp.image_url)

asyncio.run(main())
```

### With discord.py

```python
import discord
from discord.ext import commands
from hyena.Async import Client as HyenaClient

bot = commands.Bot(command_prefix="!")
hyena = HyenaClient("YOUR_API_KEY")

@bot.command()
async def chat(ctx, *, message):
    reply = await hyena.chatbot(message, language="en", name="MyBot", owner="MyName")
    await ctx.reply(reply)

bot.run("YOUR_BOT_TOKEN")
```

---

## 📚 API Reference

### `Client(api_key, *, version="1", return_json=False)`

Both `hyena.Sync.Client` and `hyena.Async.Client` accept the same constructor parameters.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `api_key` | `str` | ✅ | — | Your Hyena API key. |
| `version` | `str` | ❌ | `"1"` | API version to use. |
| `return_json` | `bool` | ❌ | `False` | If `True`, all methods return raw JSON dicts instead of processed values. |

---

### `chatbot(message, *, language="en", name="Hyena", owner="Donut")`

Get an AI chatbot response.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `message` | `str` | ✅ | — | The message to send to the chatbot. |
| `language` | `str` | ❌ | `"en"` | Language code for the conversation. |
| `name` | `str` | ❌ | `"Hyena"` | Display name of the bot. |
| `owner` | `str` | ❌ | `"Donut"` | Name of the bot's owner. |

**Returns:** `str` — the bot's reply (or `dict` if `return_json=True`).

**Aliases:** `ai`, `ai_response`, `ai_chatbot`

---

### `get_nsfw(nsfw_type, *, format="class")`

Fetch an NSFW image from a subreddit endpoint.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `nsfw_type` | `str` | ✅ | — | The endpoint name. See the [full list](https://docs.hyenabot.xyz/version-1/nsfw/endpoints). |
| `format` | `str` | ❌ | `"class"` | Return format: `"class"`, `"json"`, or `"image"`. |

**Returns:**
- `"class"` → `NsfwResponse` with `.title`, `.description`, `.image_url`, `.url`
- `"json"` → raw `dict`
- `"image"` → `str` (direct image URL)

**Aliases:** `nsfw`, `smirk`

---

### `NsfwResponse`

| Attribute | Alias | Description |
|---|---|---|
| `.title` | — | Title of the post |
| `.description` | `.desc` | Description of the post |
| `.image_url` | `.image` | Direct URL to the image |
| `.url` | `.post` | URL of the original Reddit post |

---

## ⚠️ Exceptions

| Exception | When raised |
|---|---|
| `InvalidApiKeyError` | The API key provided is invalid (HTTP 403) |
| `UnauthorizedError` | No API key was provided (HTTP 401) |
| `InvalidParametersError` | A required parameter is missing or malformed (HTTP 422) |
| `InvalidEndpointError` | The requested endpoint does not exist (HTTP 404) |
| `InvalidVersionError` | The version specified is not supported |
| `DepreciationError` | The version specified has been deprecated |

All exceptions are importable from `hyena.exceptions`.

---

## 📋 Changelog

See [CHANGELOG.md](CHANGELOG.md) for the full release history.

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0**. See [LICENSE](LICENSE) for details.