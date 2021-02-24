# import library
from op_snk import op_bash

print(
"""
OP Loverz Downloader

COMMAND MENU
snk  - menampilkan menu anime Shingeki No Kyujin S4
op   - menampilkan menu anime One Piece
all  - mendownload eposide terbaru dari SNK dan OP
exit - untuk mengakhiri program"""
)

while True:
    print()

    cmd = input("Command: ")

    if cmd == "snk":
        bot = op_bash(cmd)
        bot.run_menu(cmd)

    elif cmd == "op":
        bot = op_bash(cmd)
        bot.run_menu(cmd)

    elif cmd == "all":
        for an in ["snk","op"]:
            bot = op_bash(an)
            bot.latest_update(an)
            bot.download(bot.ep_link)

    elif cmd == "exit":
        break
    
    else:
        print(f"Perintah {cmd} tidak ditemukan.")
        print()