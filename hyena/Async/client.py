import aiohttp, asyncio
from ..exceptions import *
from ..nsfw_response import NsfwResponse

class DictResponse(dict):
    async def __aexit__(self,  exc_type, exc, tb):
        await self.session.close()
        return True
    
    async def __aenter__(self):
        return self

class StringResponse(str):
    async def __aexit__(self,  exc_type, exc, tb):
        await self.session.close()
        return True
    
    async def __aenter__(self):
        return self

class Client:
    """
    The client that connects to the API
    -----------------------------------

    Parameters
    ----------
    api_key : [Required] the API key that client should
              use to connect, get one here:
              https://api.hyenabot.xyz/ [String]

    version : [Optional] the version that the client 
              should use [String] [Default : Latest]

    return_json : [Optional] wether the client should
                  return raw json data. [Bool] 
                  [Default : False]

    Methods
    -------
    chatbot |coro| : Get a response from an AI Chatbot.

    get_nsfw |coro| : Get nsfw images from subreddits
               Endpoints: https://docs.hyenabot.xyz/version-1/nsfw/endpoints

    Version
    --------
    Added : 1.1.0
    """
    def __init__(self, api_key: str, **kwargs):
        self.api_key = api_key
        self.headers = {"api-key" : self.api_key}
        self.loop = asyncio.get_event_loop()
        self.session = aiohttp.ClientSession(headers=self.headers, loop=self.loop)
        self.depreciated = []
        self.version = str(kwargs.get("version")) if kwargs.get("version") != None else "1"
        if self.version not in ["1"]:
            raise InvalidVersionError("The version given [{}] is not a valid version, choose from \"1\"".format(self.version))
        if self.version in self.depreciated:
            raise DepreciationError("The version given [{}] is Depreciation, latest versions are: \"1\"".format(self.version))
        self.return_json = True if kwargs.get("return_json") == True else False
        self.base_url = f"https://hyenabot.xyz/api/v{self.version}/"

    async def chatbot(self, message, **kwargs):
        """
        |coro|
        Get a response from an AI Chatbot.
        ----------------------------------

        Parameters
        ----------

        message : [Required] the message that the bot should respond to
                  [String]

        language : [Optional] The language that the message is in and the bot should 
                   respond in. [String] [Default : en or english]. 

        bot_name : [Optional] Name of the bot [String] [Default : Hyena]

        bot_owner : [Optional] Name of the bot owner [String] [Default : Donut]

        Version
        --------
        Added : 1.1s.0

        Request Type
        ------------
        GET
        """
        language = str(kwargs.get("language")) if kwargs.get("language") != None else "en"
        bot_owner = str(kwargs.get("owner")) if kwargs.get("owner") != None else "Donut"
        bot_name = str(kwargs.get("name")) if kwargs.get("name") != None else "Hyena"

        payload = {
            "message" : message,
            "language" : language,
            "bot_owner" : bot_owner,
            "bot_name" : bot_name
        }
        #async 
        resp = await self.session.get(self.base_url + "chatbot", params=payload)
        _json = await resp.json()
        if resp.status == 200:
            if self.return_json == True:
                return DictResponse(_json)
            return StringResponse(_json['reply'])
        elif resp.status == 401:
            raise UnauthorizedError("No API key was provided") # it should never happen :?
        elif resp.status == 403:
            raise InvalidApiKeyError("The API key provided [{}] is invalid".format(self.api_key))
        elif resp.status == 422:
            raise InvalidParametersError(resp.json()['err'])
    
    ai_response = ai = ai_chatbot = chatbot

    async def get_nsfw(self, nsfw_type, **kwargs):
        """
        |coro|
        Get nsfw images from subreddits
        Endpoints: https://docs.hyenabot.xyz/version-1/nsfw/endpoints
        -------------------------------------------------------------

        Parameters
        ----------

        nsfw_type : [Required] the endpoint that will be used for the response
                    [String]

        return_type : [Optional] The type to be returned in response Choose from
                      <class | json | image> [String] [Default : class]. 
        Version
        --------
        Added : 1.1.0

        Request Type
        ------------
        GET
        """
        return_type = str(kwargs.get("format")).lower() if str(kwargs.get("format")).lower() in ['class', 'json', 'image'] else 'class' 
        nsfw_type = nsfw_type.lower().replace("/", "").strip()
        resp = await self.session.get(self.base_url + "nsfw/" + nsfw_type)
        if resp.status == 200:
            _json = await resp.json()
            if self.return_json == True or return_type == 'json':
                return DictResponse(_json)
            elif return_type == 'image':
                return StringResponse(_json['image_url'])
            elif return_type == 'class':
                return NsfwResponse(_json['title'], _json['description'], _json['image_url'], _json['url'])
        if resp.status == 404:
            raise InvalidEndpointError("The endpoint given [{}] is not a valid endpoint, refer to \
https://docs.hyenabot.xyz/version-1/nsfw/endpoints for list of endpoints".format(nsfw_type))
        elif resp.status == 401:
            raise UnauthorizedError("No API key was provided") # it should never happen :?
        elif resp.status == 403:
            raise InvalidApiKeyError("The API key provided [{}] is invalid".format(self.api_key))

    nsfw = smirk = get_nsfw

    async def ok(self):
        return "ok"

    async def __aexit__(self,  exc_type, exc, tb):
        """
        Async context manager

        Version
        --------
        Added : 1.1.0
        """
        await self.session.close()
        return True
    
    async def __aenter__(self):
        """
        Async context manager

        Version
        --------
        Added : 1.1.0
        """
        return self

    async def close(self):
        """
        Closes the connection

        Version
        --------
        Added : 1.1.0
        """
        await self.session.close()
        return True