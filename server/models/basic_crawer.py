from abc import ABC, abstractmethod
from newspaper import Article


class BasicCrawer(ABC):
    url: str
    context: str
    html: str
    article: Article

    @abstractmethod
    def get(self):
        return NotImplemented

    def getinfo(self):
        self.article = Article(self.url)
        self.article.download(input_html=self.html)
        self.article.parse()
        return self.article
