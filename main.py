from html5lib.treewalkers import pprint
import requests, pprint, json, os

riot_url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
response = requests.get(riot_url, verify=False)
response_json = response.json()
active_summoner_name = response_json["activePlayer"]["summonerName"]
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "builds.json")
print(file_path)
print(active_summoner_name)

def get_summoner_champion(summoner_name):
    champion_name = ""
    for players in response_json["allPlayers"]:
        if players["summonerName"] == summoner_name:
            champion_name = players["championName"]
    return champion_name

champion_name = get_summoner_champion(active_summoner_name)

with open(file_path, 'r') as builds:
    build_data = json.load(builds)
    if champion_name in build_data:
        print(build_data[champion_name]["core_build"])
