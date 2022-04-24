import re
import urllib
import urllib.request
import numpy as np


class Bing:
    def __init__(self, query, limit=10, adult="on", timeout=60, filters="", page_counter=0):
        self.query = query
        self.adult = adult
        self.filters = filters
        self.limit = limit
        self.timeout = timeout
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
        self.page_counter = page_counter

    def run(self):
        request_url = (
            "https://www.bing.com/images/async?q="
            + urllib.parse.quote_plus(self.query)
            + "&first="
            + str(self.page_counter)
            + "&count="
            + str(self.limit)
            + "&adlt="
            + self.adult
            + "&qft="
            + self.filters
        )
        request = urllib.request.Request(request_url, None, headers=self.headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf8")
        links = re.findall("murl&quot;:&quot;(.*?)&quot;", html)

        return links[np.random.randint(0, self.limit)]


def download(query):
    return Bing(query).run()

