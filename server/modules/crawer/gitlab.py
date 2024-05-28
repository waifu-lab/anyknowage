import requests
import re
import sys

from util.readme_unmark import unmark
from models.basic_crawer import BasicCrawer


class Gitlab(BasicCrawer):
    def __init__(self, url: str):
        self.url = url
        self.API_URL = "https://gitlab.com/api/v4/projects/"
        self.RAW_URL = "https://gitlab.com/"

    def get(self):
        match = re.match(
            "https:\/\/gitlab.com/([a-zA-Z0-9._-]{1,30}/[a-zA-Z0-9._-]{1,30})", self.url
        )
        if match:
            res = requests.get(self.API_URL + match[1].replace("/", "%2F"))
            if not res.ok:
                raise Exception("get gitlab failed")
            data = res.json()
            readme = requests.get(
                self.RAW_URL + match[1] + f"/-/raw/{data['default_branch']}/README.md"
            )
            if not readme.ok:
                readme = requests.get(
                    self.RAW_URL
                    + match[1]
                    + f"/-/raw/{data['default_branch']}/readme.md"
                )
                if not readme.ok:
                    readme.text = ""
            readme = unmark(readme.text)
            returndata = {
                "Content": data["description"] + "\n" + readme,
                "Meta": {
                    "Username": {data["namespace"]["name"]},
                    "Repo_Name": {data["name"]},
                    "Repo_Url": {data["web_url"]},
                    "Date": {data["created_at"]},
                },
            }
            return returndata
        else:
            return None
