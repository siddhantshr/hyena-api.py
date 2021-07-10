class NsfwResponse:
    """
    Response provided when the get_nsfw method of Client is called,
    ---------------------------------------------------------------

    Parameters
    ----------
    title : Title of response
    description : Description of response
    image_url : Image URL of response
    URL : URL of the original post
    
    Version
    --------
    Added : 1.0.0
    """
    def __init__(self, title, description, image_url, url):
        self.title = title
        self.description = description
        self.desc = description
        self.image_url = image_url
        self.image = image_url
        self.url = url
        self.post = url

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
