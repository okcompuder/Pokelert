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

    def _start(self):
        print('Hello from PokelertBot!')
