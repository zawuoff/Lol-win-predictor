from html5lib.treewalkers import pprint
import requests, pprint

riot_url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
response = requests.get(riot_url, verify=False)
response_json = response.json()

active_summoner_name = response_json["activePlayer"]["summonerName"]

print(active_summoner_name)

def get_summoner_champion(summoner_name):
    champion_name = ""
    for players in response_json["allPlayers"]:
        if players["summonerName"] == summoner_name:
            champion_name = players["championName"]
    return champion_name
        

print(get_summoner_champion(active_summoner_name))
# try: 
#     response = requests.get(riot_url, verify=False)
#     response_json = response.json()
#     pprint.pprint(response_json["allPlayers"])
    
# except:
#     print("No Active League Data")


# print(response.status_code)