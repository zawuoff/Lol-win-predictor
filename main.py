import requests
from functions import get_summoner_champion, load_core_build
import webview
from screeninfo import get_monitors
import json

riot_url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
response = requests.get(riot_url, verify=False)
response_json = response.json()
active_summoner_name = response_json["activePlayer"]["summonerName"]


champion_name = get_summoner_champion(response_json, active_summoner_name)

build_data = load_core_build()

monitor = get_monitors()[1]
screen_width = monitor.width

window_width = 300
window_height = 100

pos_x = screen_width - window_width - 10
pos_y = 55

if champion_name in build_data:
    print(build_data[champion_name]["core_build"])
    core_build = build_data[champion_name]["core_build"]
    core_build_string = ",".join(core_build)
    print(core_build_string)
    window = webview.create_window(
        'LoL Overlay', 
        'ui/overlay.html',  # file name for html
        transparent=True, 
        on_top=True, 
        frameless=True,
        width= 350, 
        height= 150,
        resizable = False,
        easy_drag = False,
        x=pos_x,
        y=pos_y
    )

    def update_ui():
        import time
        time.sleep(1) 
        js_champ = json.dumps(champion_name)
        js_build = json.dumps(core_build_string)
        window.evaluate_js(f"displayBuild({js_champ}, {js_build})")
    webview.start(update_ui)


