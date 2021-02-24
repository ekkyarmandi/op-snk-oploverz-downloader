import re, requests
from bs4 import BeautifulSoup

class ZippyBot():

    def __init__(self):
        
        pass

    def page_renderer(self, url):

        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

        self.headers = headers

        page = requests.get(url, headers=headers)
        soups = BeautifulSoup(page.content, 'html.parser')

        return soups

    def get_extension(self, title):

        ext = re.findall(r"\b\w{3}\b", title)[-1]

        self.ext = ext

    def completor(self, zippy_link, script):
        
        # get the zippy main link
        delimiter = "/"
        zippy_url = zippy_link.split("/")[:3]
        zippy_url = delimiter.join(zippy_url)

        # extract javascript download link
        link = script.contents[0].strip().split(";")[0][43:]
        mid = eval(re.findall(r'\((.*?)\)', link)[0])
        rest = re.findall('\"(.*?)\"', link)
        link = "".join([rest[0],str(mid),rest[1]])
        link = zippy_url+link

        return link

    def get_zippy_link(self, url):

        soups = self.page_renderer(url)
        sortlist = soups.findAll("div", class_="sorattl title-download")

        for item in sortlist:

            if all([(cat in item.text.lower()) for cat in ["1080", "mp4"]]):
                self.get_extension(item.text)
                zippy_link = item.findNext("a", text="Zippyshare")['href']
                break

            elif all([(cat in item.text.lower()) for cat in ["1080", "mkv"]]):
                self.get_extension(item.text)
                zippy_link = item.findNext("a", text="Zippyshare")['href']
                break

            elif all([(cat in item.text.lower()) for cat in ["720", "mp4"]]):
                self.get_extension(item.text)
                zippy_link = item.findNext("a", text="Zippyshare")['href']
                break

        return zippy_link

    def get_zippy_download(self, zippy_url):

        soups = self.page_renderer(zippy_url)
        scripts = soups.findAll('script', {"type":"text/javascript"})

        for script in scripts:
            if self.ext in str(script.contents):
                dl_link = self.completor(zippy_url, script)
                break

        return dl_link