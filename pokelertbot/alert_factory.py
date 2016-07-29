from datetime import datetime

class AlertFactory(object):

    def __init__(self, config):
        self.config = config

    def generate_alert(self, alert_type, pokemon):
        alert = self.nearby_alert(pokemon)
        return alert

    def nearby_alert(self, pokemon):
        text = ''
        attachments = self.nearby_attachments(pokemon)
        return { 'text': text, 'attachments': attachments}

    def nearby_attachments(self, pokemon):
        id = str(pokemon['pokemon_id']).zfill(3)
        url = 'https://fevgames.net/pokedex/{}-{}/'.format(id, pokemon['pokemon_name'])
        author_name = u'Wild {} appeared!'.format(pokemon['pokemon_name'])
        color = self.format_color(pokemon)
        
        attachments = \
        [{
            'fallback':'Error',
            'color': color,
            'title': author_name,
            'author_link': url,
            'fields': self.nearby_fields(pokemon),
            'thumb_url':'http://pogo.ethanhoneycutt.com/static/larger-icons/{}.png'.format(pokemon['pokemon_id']),
            'footer':'<{}|Github>'.format('https://github.com/okcompuder/Pokelert'),
            'footer_icon':'http://androidforum.cz/images/icons/hw/ext/pokemon_go.png',
            'mrkdwn_in': ['title']
        }]
        return attachments

    def nearby_fields(self, pokemon):
        gmaps = 'http://maps.google.com/maps?q={},{}&24z'.format(pokemon['latitude'], pokemon['longitude'])
        distance = self.format_distance(self.config['LATITUDE'], self.config['LOGITUDE'])
        location = '<{}|{}>'.format(gmaps, distance)
        time = self.format_time(pokemon['disappear_time'])
        types = ' '.join(pokemon['pokedex_info']['Types'])

        fields = [\
                  { 'title':'Location', 'value':location, 'short':'true' },
                  { 'title':'Time Remaining', 'value':time, 'short':'true' },
                  { 'title':'Type', 'value':types, 'short':'true' },
                  { 'title':'Attack/Defense/Stamina', 'value':'94/90/80', 'short':'true' }
                 ]
        return fields

    def format_color(self, pokemon):
        first_type = pokemon['pokedex_info']['Types'][0]
        return self.color_map(first_type)   
        
    def color_map(self, type):
        colors = {
            'Normal': '#000000',
            'Grass': '#228B22',
            'Bug': '#00FF00',
            'Water': '#1E90FF'
        }
        return colors.get(type, '#FFFFFF')
        
    def format_distance(self, lat, long):
        return '400 Feet NW'

    def format_time(self, timestamp):
        seconds = (datetime.fromtimestamp(timestamp / 1e3) - datetime.now()).total_seconds()
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        time = "%i Minutes %i Seconds" % (minutes, seconds)
        return time
