import json
from slackclient import SlackClient
from geopy.geocoders import Nominatim
from datetime import datetime

slack_client = None
wanted_pokemon = None

# Initialize object
def init():
    global slack_client, wanted_pokemon
    # load pushbullet key
    with open('config.json') as data_file:
        data = json.load(data_file)
        # get list of pokemon to send notifications for
        wanted_pokemon = _str( data["notify"] ) . split(",")
        # transform to lowercase
        wanted_pokemon = [a.lower() for a in wanted_pokemon]
        # get api key
        api_key = _str( data["slack_api_token"] )
        if api_key:
            slack_client = SlackClient(api_key)


# Safely parse incoming strings to unicode
def _str(s):
  return s.encode('utf-8').strip()

# Notify user for discovered Pokemon
def pokemon_found(pokemon):
    # get name
    pokename = _str(pokemon["name"]).lower()
    # check array
    if not slack_client or not pokename in wanted_pokemon: return
    # notify
    print "[+] Notifier found pokemon:", pokename
    gMaps = "http://maps.google.com/maps?q=" + str(pokemon["lat"]) + "," + str(pokemon["lng"]) + "&24z"
    disappear_time = str(datetime.fromtimestamp(pokemon["disappear_time"]).strftime("%I:%M%p").lstrip('0'))
    notification_text = 'A wild {0} was found nearby and will disappear at {1}! {2}'.format(pokemon["name"], disappear_time, gMaps)
    slack_client.rtm_connect()
    slack_client.rtm_send_message("#pokedev", notification_text)


init()
