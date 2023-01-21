
__all__ = ["Nets"]
class SpiderError(Exception):
    pass

import requests, base64

class Nets:
    def __init__(self) -> None:
        self.ShortUrl_BackEnd = ["https://suo.yt/short"]
    
    def ShortUrl(self, URL:str, User_Agent:str="TechnologySpider", BackEnd:int=0) -> str:
        Form = {
            "longUrl": base64.b64encode(URL.encode("utf-8")).decode("utf-8"),
            "User_Agent": User_Agent
        }
        _Date = requests.post(self.ShortUrl_BackEnd[BackEnd], data=Form)
        if _Date.status_code != 200:
            return
        else:
            _Date = _Date.json()
            return _Date["ShortUrl"]

if __name__ == "__main__":
    pass