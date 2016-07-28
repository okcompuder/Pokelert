import requests
import time
from datetime import datetime
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

    def send_message(self, message, attachments=None, channel=None):
        if channel is None:
            for channel in self.channels:
                self.sc.api_call('chat.postMessage', channel=channel, text=message, as_user=True, attachments=attachments, mrk_dwn=True)
        else:
            self.sc.api_call('chat.postMessage', channel=channel, text=message, as_user=True, attachments=attachments)

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
        for p in self.new_pokemon():
            message_dict = self.generate_message(p)
            self.send_message(message_dict['text'], attachments=message_dict['attachments'])

    def generate_message(self, pokemon):
        name = pokemon['pokemon_name']
        id = str(pokemon['pokemon_id']).zfill(3)
        url = 'https://fevgames.net/pokedex/{}-{}/'.format(id, name)
        
        text = u'Wild *<{}|{}>* appeared!'.format(url, name) 
        attachments = self.generate_attachments(pokemon)
        return { 'text': text, 'attachments': attachments}
        
    def generate_attachments(self, pokemon):
        attachments = \
        [{
            'fallback':'Error',
            'color':'#439FE0',            
            'fields':self.generate_fields(pokemon),
            'thumb_url':'http://pogo.ethanhoneycutt.com/static/larger-icons/{}.png'.format(pokemon['pokemon_id']),
            'footer':'<{}|Github>'.format('https://github.com/okcompuder/Pokelert'),
            'footer_icon':'http://androidforum.cz/images/icons/hw/ext/pokemon_go.png'
        }]
        return attachments
        
    def generate_fields(self, pokemon):
        gmaps = 'http://maps.google.com/maps?q={},{}&24z'.format(pokemon['latitude'], pokemon['longitude'])
        location = "<{}|Map>".format(gmaps)        
        time = self.format_time(pokemon['disappear_time'])
               
        fields = [{ 'title':'Location', 'value':location, 'short':'true' }, 
                  { 'title':'Time Remaining', 'value':time, 'short':'true' },
                  { 'title':'Type', 'value':'Kanto', 'short':'true' },
                  { 'title':'Attack/Defense/Stamina', 'value':'94/90/80', 'short':'true' }
                  ]
        return fields
        
    def format_time(self, timestamp):
        seconds = (datetime.fromtimestamp(timestamp / 1e3) - datetime.now()).total_seconds()
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        time = "%i Minutes %i Seconds" % (minutes, seconds)
        return time

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
