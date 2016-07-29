from datetime import datetime

def generate_alert(alert_type, pokemon):
    alert = nearby_alert(pokemon)
    return alert

def nearby_alert(pokemon):
    text = u'Wild *{}* appeared!'.format(pokemon['pokemon_name'])
    attachments = nearby_attachments(pokemon)
    return { 'text': text, 'attachments': attachments}

def nearby_attachments(pokemon):
    id = str(pokemon['pokemon_id']).zfill(3)
    url = 'https://fevgames.net/pokedex/{}-{}/'.format(id, pokemon['pokemon_name'])
    attachments = \
    [{
        'fallback':'Error',
        'color':'#439FE0',
        'author_name': 'Scan',
        'author_link': url,
        'fields': nearby_fields(pokemon),
        'thumb_url':'http://pogo.ethanhoneycutt.com/static/larger-icons/{}.png'.format(pokemon['pokemon_id']),
        'footer':'<{}|Github>'.format('https://github.com/okcompuder/Pokelert'),
        'footer_icon':'http://androidforum.cz/images/icons/hw/ext/pokemon_go.png'
    }]
    return attachments

def nearby_fields(pokemon):
    gmaps = 'http://maps.google.com/maps?q={},{}&24z'.format(pokemon['latitude'], pokemon['longitude'])
    location = "<{}|Map>".format(gmaps)
    time = format_time(pokemon['disappear_time'])

    fields = [{ 'title':'Location', 'value':location, 'short':'true' },
              { 'title':'Time Remaining', 'value':time, 'short':'true' },
              { 'title':'Type', 'value':'Kanto', 'short':'true' },
              { 'title':'Attack/Defense/Stamina', 'value':'94/90/80', 'short':'true' }
             ]
    return fields

def format_time(timestamp):
    seconds = (datetime.fromtimestamp(timestamp / 1e3) - datetime.now()).total_seconds()
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    time = "%i Minutes %i Seconds" % (minutes, seconds)
    return time
