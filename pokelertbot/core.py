import requests
import time
import alert_factory
from slackclient import SlackClient

class PokelertBot(object):

    def __init__(self, config):
        self.config = config
        self.token = config.get('SLACK_TOKEN')
        self.channels = config.get('CHANNELS')
        self.sc = SlackClient(self.token)
        self.pokemon_cache = []

    def start(self):
        self.sc.rtm_connect()
        self.user_id = self.sc.api_call('auth.test', token=self.token)['user_id']
        self.username = u'<@' + self.user_id + '>'

        print('[-] Pokelert Bot initialized')
        while True:
            for message in self.sc.rtm_read():
                self.input(message)
            self.alert_slack()
            time.sleep(.1)

    def send_message(self, message, channel=None):
        if channel is None:
            for channel in self.channels:
                self.sc.api_call('chat.postMessage', channel=channel, text=message['text'], as_user=True, attachments=message['attachments'], mrk_dwn=True)
        else:
            self.sc.api_call('chat.postMessage', channel=channel, text=message['text'], as_user=True, attachments=message['attachments'])

    def input(self, message):
        if 'message' != message['type']:
            return

        if not self.username in message['text']:
            return

        if 'nearby' in message['text']:
            self.send_message(self.retrieve_pokemon()[0]['pokemon_name'], channel=message['channel'])

    def cache_pokemon(self, items):
        self.pokemon_cache += items

    def new_pokemon(self):
        new_list = [p for p in self.retrieve_pokemon() if not p in self.pokemon_cache]
        self.cache_pokemon(new_list)
        return new_list

    def alert_slack(self):
        for poke in self.new_pokemon():
            alert = alert_factory.generate_alert('nearby', poke)
            self.send_message(alert)

    def retrieve_pokemon(self):
        URL = self.config.get('ENDPOINT_URL') + '/raw_data?gyms=false&pokestops=false&scanned=false'
        r = requests.get(URL)
        return r.json()['pokemons']

    def retrieve_gyms(self):
        URL = self.config.get('ENDPOINT_URL') + '/raw_data?pokemons=false&gyms=true&pokestops=false&scanned=false'
        r = requests.get(URL)
        return r.json()['gyms']

    def retrieve_pokestops(self):
        URL = self.config.get('ENDPOINT_URL') + '/raw_data?pokemons=false&gyms=false&pokestops=true&scanned=false'
        r = requests.get(URL)
        return r.json()['pokestops']
