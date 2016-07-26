import yaml
from pokelertbot import PokelertBot


if __name__ == '__main__':
    config = yaml.load(open('config.yaml', 'r'))
    plbot = PokelertBot(config)
    try:
        print plbot.retrieve_pokemon()
    except KeyboardInterrupt:
        sys.exit()
