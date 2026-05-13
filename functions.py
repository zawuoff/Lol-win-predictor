import os, json
def get_summoner_champion(response_json, summoner_name):
    champion_name = ""
    for players in response_json["allPlayers"]:
        if players["summonerName"] == summoner_name:
            champion_name = players["championName"]
    return champion_name

def load_core_build():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "builds.json")
    with open(file_path, 'r') as builds:
        return json.load(builds)