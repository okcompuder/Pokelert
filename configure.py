import argparse
import json

DEFAULT_ARGS = {
    'ampm_clock': False,
    'auth_service': 'ptc',
    'auto_refresh': None,
    'china': False,
    'debug': False,
    'display_gym': False,
    'display_pokestop': False,
    'host': '127.0.0.1',
    'ignore': None,
    'locale': 'en',
    'only': None,
    'onlylure': False,
    'port': 5000,
    'step_limit': 3
}

def get_args():
    args = DEFAULT_ARGS.copy()
    with open('config.json') as data_file:
        data = json.load(data_file)
        for key in data:
            args[key] = data[key]

        namespace = argparse.Namespace()
        for key in args:
            vars(namespace)[key] = args[key]
        return namespace

if __name__ == '__main__':
    print(get_args())
