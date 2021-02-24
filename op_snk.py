from zippyshare import ZippyBot
from pathlib import Path
import re, wget

class op_bash(ZippyBot):

    def __init__(self, kind):

        super().__init__()

        if kind != all:
            print("Options: latest update, download latest, save dir, update save dir, exit")

        self.ep_link = None

        if kind == "snk":
            self.url = "https://www.oploverz.in/series/shingeki-no-kyojin-season-4/"
            self.save_dir = "C://Users/Lenovo/Downloads/Video/Shingeki No Kyujin Season 4/"
        
        elif kind == "op":
            self.url = "https://www.oploverz.in/series/one-piece-sub-indo/"
            self.save_dir = "C://Users/Lenovo/Downloads/Video/OP/"

    def run_menu(self, kind):

        while True:
            print()
            option = input(f"{kind.upper()} Command: ")

            if option == "latest update":
                self.latest_update(kind)
                print(self.ep_title)

            elif option == "update save dir":
                answer = input("Apakah Anda ingin mengganti lokasi penyimpanan? (y/n): ")
                if answer.lower() == "y": self.save_dir = input("dir: ")

            elif option == "save dir":
                print(self.save_dir)

            elif option == "download latest":
                self.latest_update(kind)
                print(self.ep_title)

                self.download(self.ep_link)

            elif option == "exit" or option == "back":
                break

    def latest_update(self, kind):

        def title(ep_url, kind):
            if kind == "snk":
                ep = re.search(r"(episode\-\d{2})",ep_url)[0]
            elif kind == "op":
                ep = re.search(r"(episode\-\d{3})",ep_url)[0]

            ep = ep.replace("-"," ").title()
            return ep

        soups = self.page_renderer(self.url)
        episodes = soups.find("div", class_="episodelist").find("ul")

        link = episodes.find("span", {'class':'lefttitle'}).find("a")['href']
        episode = title(link, kind)

        last_update = episodes.find("span", {'class':'rightoff'}).text.strip()
        last_episode = episodes.find("span", {'class':'lefttitle'}).find("a").text.strip()

        ep_title = f"{episode}: {last_episode} [{last_update}]"

        self.ep_link = link
        self.ep_title = ep_title

    def download(self, url):

        def file_title(filename):
            filename = filename.replace("%20", " ")
            filename = filename.replace("%5d", "]")
            filename = filename.replace("%5b", "[")
            return filename
        
        zippy_link = self.get_zippy_link(url)
        dl_link = self.get_zippy_download(zippy_link)

        filename = wget.detect_filename(dl_link)
        filename = file_title(filename)
        print(filename)
        
        wget.download(dl_link,str(Path(self.save_dir,filename)))