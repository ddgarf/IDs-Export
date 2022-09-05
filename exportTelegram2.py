from telethon.sync import TelegramClient
from git import Repo
import utils as u
import re
from exportTelegraph import *
import asyncio
from telethon import TelegramClient
from telethon.tl.types import PeerChannel

def cleanse_message(message_content):
    cleansed_content = ""
    rows = [row for row in message_content.split("\n") if len(row.strip()) > 0] 
    channel_id_regex = r'[a-zA-Z0-9]{40}'
    if re.search(channel_id_regex, message_content):
        for i, row in enumerate(rows):
            if re.search(channel_id_regex, row):
                if i > 0:
                  cleansed_content += rows[i-1] + "\n" + row + "\n"
                else:
                  cleansed_content += "UNTITLED CHANNEL" + "\n" + row + "\n"
    return cleansed_content


def update_channel_dict(message_content, channel_dict):
    rows = message_content.split("\n")
    for i, row in enumerate(rows):
        if i % 2 == 1:
            channel_id = row
            channel_name = rows[i-1]
            channel_dict[channel_id] = channel_name
    return channel_dict


def export_channels(channel_dict, export_file):

    channel_list = []

    for channel_id, channel_name in channel_dict.items():
        group_title = u.extract_group_title(channel_name)
        tvg_id = u.extract_tvg_id(channel_name)
        logo = u.get_logo(tvg_id)
        channel_info = {"group_title": group_title,
                        "tvg_id": tvg_id,
                        "logo": logo,
                        "channel_id": channel_id,
                        "channel_name": channel_name}
        channel_list.append(channel_info)

    all_channels = ""
    all_channels += '#EXTM3U url-tvg="https://raw.githubusercontent.com/dracohe/CARLOS/master/guide_IPTV.xml"\n'
    channel_pattern = '#EXTINF:-1 group-title="GROUPTITLE" tvg-id="TVGID" tvg-logo="LOGO" ,CHANNELTITLE\nhttp://127.0.0.1:6878/ace/getstream?id=CHANNELID\n'


    for group_title in u.group_title_order:
        for channel_info in channel_list:
            if channel_info["group_title"] == group_title:
                all_channels += channel_pattern.replace("GROUPTITLE", channel_info["group_title"]) \
                                               .replace("TVGID", channel_info["tvg_id"]) \
                                               .replace("LOGO", channel_info["logo"]) \
                                               .replace("CHANNELID", channel_info["channel_id"]) \
                                               .replace("CHANNELTITLE", channel_info["channel_name"])


    with open(export_file, "w") as f:
        f.write(all_channels)

api_id = 
api_hash = ''

peer_channel_id =  # replace with channel peer 

async def export_messages(export_file="RUTA AQUI"):

    async with TelegramClient('NOMBRE DE USUARIO DE TELEGRAM AQUI', api_id, api_hash) as client:
        channel_name = await client.get_entity(PeerChannel(peer_channel_id))
        channel_dict = dict()  # {channel_id: channel_name}

        try:
            contenido_telegraph = exportTelegraph()
            cleansed_content = cleanse_message(contenido_telegraph) #!!!!!!!!!!!!!
            async for message in client.iter_messages(channel_name, limit=10):
                message_content = message.message
                if message_content is not None:
                    cleansed_content += cleanse_message(message_content)
                    if cleansed_content:
                        channel_dict = update_channel_dict(cleansed_content, channel_dict)
        except Exception as e:
            print("export_messages : ERROR :", e)

        print("export_messages : INFO : messages retrieved from Telegram")



        export_channels(channel_dict, export_file)

        print("export_messages : INFO : messages exported")

def main():
    asyncio.run(export_messages())

def gitUpdate():
    gitRepo = r'RUTA AQUI'
    commitMessage = 'channels updated'

    try:
        repo = Repo(gitRepo)
        repo.git.add(update=True)
        repo.index.commit(commitMessage)
        origin = repo.remote(name='origin')
        origin.push()

        print("updating_github : INFO : channels updated to github")
    except:
        print("updating_github : ERROR : some error occured while pushing the code")

if __name__ == "__main__":
    main()
    gitUpdate()
