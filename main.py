import yaml
import sys
from pokelertbot import PokelertBot
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-d', '--debug', help="Debug mode", action='store_true')
    parser.add_argument('-c', '--config', help="Path to config file", metavar='path')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    config = yaml.load(open(args.config or 'config.yaml', 'r'))
    pokedex = yaml.load(open('pokelertbot/pokedex.yaml', 'r'))
    plbot = PokelertBot(config, pokedex)
    try:
        plbot.start()
    except KeyboardInterrupt:
        sys.exit()
