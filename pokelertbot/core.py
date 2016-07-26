import requests
import time
from slackclient import SlackClient

class PokelertBot(object):
    def __init__(self, config):
        """
        Params:
            SLACK_TOKEN: auth token generated from Slack
            CHANNELS: list of channels (i.e, ['general', 'random']) to alert on
            DEBUG: (optional: defaults to False)
        """
        self.config = config
        self.token = config.get('SLACK_TOKEN')
        self.channels = config.get('CHANNELS')
        self.sc = SlackClient(self.token)

    def start(self):
        self.sc.rtm_connect()
        self.user_id = self.sc.api_call('auth.test', token=self.token)['user_id']
        self.username = u'<@' + self.user_id + '>'

        print('[-] Pokelert Bot initialized')
        while True:
            for message in self.sc.rtm_read():
                self.input(message)
            time.sleep(.1)

    def send_message(self, message, attachment=None, channel=None):
        if channel is None:
            for channel in self.channels:
                print channel
                self.sc.api_call('chat.postMessage', channel=channel, text=message, as_user=True, attachment=attachment)

        self.sc.api_call('chat.postMessage', channel=channel, text=message, as_user=True, attachment=attachment)

    def input(self, message):
        if 'message' != message['type']:
            return

        if not self.username in message['text']:
            return

        if 'nearby' in message['text']:
            print('Nearby requested')
            print self.retrieve_pokemon()[0]['pokemon_name'], message['channel']
            self.send_message(self.retrieve_pokemon()[0]['pokemon_name'], channel=message['channel'])

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
