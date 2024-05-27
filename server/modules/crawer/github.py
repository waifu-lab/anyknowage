from models.basic_crawer import BasicCrawer
import requests
import re
from util.readme_unmark import unmark


class Github(BasicCrawer):
    def __init__(self, url: str):
        self.url = url
        self.API_URL = "https://api.github.com/repos/"
        self.RAW_URL = "https://raw.githubusercontent.com"

    def get(self):
        match = re.match(
            "https:\/\/github.com/([a-zA-Z0-9._]{1,30}/[a-zA-Z0-9._-]{1,30})", self.url
        )
        if match:
            res = requests.get(self.API_URL + match[1])
            if not res.ok:
                raise Exception("get github failed")
            data = res.json()
            readme = requests.get(
                self.RAW_URL + match[1] + f"/{data["default_branch"]}/README.md"
            )
            if not readme.ok:
                readme = requests.get(
                    self.RAW_URL + match[1] + f"/{data["default_branch"]}/readme.md"
                )
                if not readme.ok:
                    readme.text = ""
            readme = unmark(readme.text)
            returndata = {
                "Content": data["description"] + "\n" + readme,
                "Meta": {
                    "Username": {data["owner"]["login"]},
                    "Repo_Name": {data["name"]},
                    "Repo_Url": {data["html_url"]},
                    "Date": {data["created_at"]},
                },
            }
            return returndata
        else:
            return None
