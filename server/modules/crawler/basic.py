import requests
from DrissionPage import ChromiumOptions, ChromiumPage
from models.basic_crawer import BasicCrawer


class Crawer(BasicCrawer):
    def __init__(self, url: str):
        self.url = url

    def use_request(self) -> bool:
        req = requests.get(self.url)
        if not req.ok:
            return False
        self.html = req.text
        return True

    def use_chromium(self) -> bool:
        options = ChromiumOptions()
        options.headless(True)
        options.set_address("--no-sandbox")
        page = ChromiumPage(options)
        page.get(self.url)
        self.html = page.html
        page.quit()
        return True

    def get(self):
        if not self.use_request():
            if not self.use_chromium():
                raise Exception("get html failed")
        data = self.getinfo()
        returndata = {
            "Content": data.text,
            "Meta": {
                "Title": data.title,
                "Authors": " ".join(data.authors),
                "Publish_Time": str(data.publish_date),
                "Keywords": " ".join(data.keywords),
            },
        }
        return returndata
