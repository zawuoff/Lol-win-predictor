from html5lib.treewalkers import pprint
import requests, pprint

riot_url = "https://127.0.0.1:2999/liveclientdata/allgamedata"




try: 
    response = requests.get(riot_url, verify=False)
    response_json = response.json()
    # print(response_json.keys()) 
    # print(response_json["allPlayers"])
    # print("connected to live league api")
    pprint.pprint(response_json["allPlayers"][0])
    """
    for players in response_json["allPlayers"]:
        if players["team"] == "ORDER":
            players["team"] = "BLUE"
        if players["team"] == "CHAOS":
            players["team"] = "RED"
        print(f"{players["championName"]} - {players["team"]}")
    """
except:
    print("No Active League Data")


# print(response.status_code)