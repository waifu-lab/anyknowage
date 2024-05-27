from models.basic_crawer import BasicCrawer
import re
import requests


class twitter(BasicCrawer):
    def __init__(self, url: str):
        self.url = url
        self.API_URL = "https://api.vxtwitter.com/"

    def get(self):
        redata = re.match(
            r"https:\/\/(twitter.com|x.com)?/([a-zA-Z0-9._]{1,20})(/(status)?/([0-9]{1,}))?",
            self.url,
        )
        if redata[4] == "status":
            res = requests.get(self.API_URL + redata[5])
            if not res.ok:
                raise Exception("get twitter failed")
            data = res.json()
            returndata = {
                "Content": data["text"],
                "Meta": {
                    "Username": {data["user_name"]},
                    "User_ID": {data["user_screen_name"]},
                    "Tweet_Url": {data["tweetURL"]},
                    "Date": {data["date"]},
                },
            }
            return returndata
        else:
            return None
