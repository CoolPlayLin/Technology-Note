__all__ = ["Spiders"]
class SpiderError(Exception):
    pass

import requests, base64

class Spiders:
    def __init__(self) -> None:
        self.ShortUrl_BackEnd = ["https://suo.yt/short", "https://d1.mk/short"]
    
    def ShortUrl(self, URL:str, User_Agent:str="TechnologySpider", BackEnd:int=0) -> str:
        Form = {
            "longUrl": base64.b64encode(URL.encode("utf-8")).decode("utf-8"),
            "User_Agent": User_Agent
        }
        _Date = requests.post(self.ShortUrl_BackEnd[BackEnd], data=Form)
        _ErrorMessage = _Date.json()["Message"] if not bool(_Date.json()["ShortUrl"]) else "The status code error is {}".format(_Date.status_code) if _Date.status_code != 200 else None
        if bool(_ErrorMessage):
            raise SpiderError(_Date.json()["Message"])
        else:
            return _Date.json()["ShortUrl"]

if __name__ == "__main__":
    pass