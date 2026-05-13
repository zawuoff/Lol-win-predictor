from html5lib.treewalkers import pprint
import requests, pprint, json
from functions import get_summoner_champion, load_core_build

riot_url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
response = requests.get(riot_url, verify=False)
response_json = response.json()
active_summoner_name = response_json["activePlayer"]["summonerName"]


champion_name = get_summoner_champion(response_json, active_summoner_name)

build_data = load_core_build()

if champion_name in build_data:
    print(build_data[champion_name]["core_build"])