from urllib.request import urlopen

class Request:
    def get(self, url):
        content = urlopen(url).read()
        return content

