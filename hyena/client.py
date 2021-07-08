import requests
from .exceptions import *

class NsfwResponse:
    def __init__(self, title, description, image_url, url):
        self.title = title
        self.description = description
        self.desc = description
        self.image_url = image_url
        self.image = image_url
        self.url = url
        self.post = url

class Client:
    def __init__(
        self,
        api_key: str,
        **kwargs
    ):
        self.api_key = api_key
        self.headers = {"api-key" : self.api_key}
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.depreciated = []
        self.version = str(kwargs.get("version")) if kwargs.get("langauge") != None else "1"
        if self.version not in ["1"]:
            raise InvalidVersionError("The version given [{}] is not a valid version, choose from \"1\"".format(self.version))
        if self.version in self.depreciated:
            raise DepreciationError("The version given [{}] is Depreciation, latest versions are: \"1\"".format(self.version))
        self.return_json = True if kwargs.get("return_json") == True else False
        self.base_url = f"https://hyenabot.xyz/api/v{self.version}/"

    def chatbot(self, message, **kwargs):
        language = str(kwargs.get("language")) if kwargs.get("language") != None else "en"
        bot_owner = str(kwargs.get("owner")) if kwargs.get("owner") != None else "Donut"
        bot_name = str(kwargs.get("name")) if kwargs.get("name") != None else "Hyena"

        payload = {
            "message" : message,
            "language" : language,
            "bot_owner" : bot_owner,
            "bot_name" : bot_name
        }
        resp = self.session.get(self.base_url + "chatbot", params=payload)
        if resp.status_code == 200:
            if self.return_json == True:
                return resp.json()
            return resp.json()['reply']
        elif resp.status_code == 401:
            raise UnauthorizedError("No API key was provided") # it should never happen :?
        elif resp.status_code == 403:
            raise InvalidApiKeyError("The API key provided [{}] is invalid".format(self.api_key))
        elif resp.status_code == 422:
            raise InvalidParametersError(resp.json()['err'])
    
    ai_response = ai = ai_chatbot = chatbot

    def get_nsfw(self, nsfw_type, **kwargs): 
        return_type = str(kwargs.get("format")).lower() if str(kwargs.get("format")).lower() in ['class', 'json', 'image'] else 'class' 
        nsfw_type = nsfw_type.lower().replace("/", "").strip()
        resp = self.session.get(self.base_url + "nsfw/" + nsfw_type)
        if resp.status_code == 200:
            if self.return_json == True or return_type == 'json':
                return resp.json()
            elif return_type == 'image':
                return resp.json()['image_url']
            elif return_type == 'class':
                _dict = resp.json()
                return NsfwResponse(_dict['title'], _dict['description'], _dict['image_url'], _dict['url'])
        if resp.status_code == 404:
            raise InvalidEndpointError("The endpoint given [{}] is not a valid endpoint, refer to \
https://docs.hyenabot.xyz/version-1/nsfw/endpoints for list of endpoints")
        elif resp.status_code == 401:
            raise UnauthorizedError("No API key was provided") # it should never happen :?
        elif resp.status_code == 403:
            raise InvalidApiKeyError("The API key provided [{}] is invalid".format(self.api_key))

    nsfw = smirk = get_nsfw

    def close(self):
        self.session.close()
