# Pokémon Go Slack Bot

This is a Python application used to notify a Slack channel about nearby desired Pokémon.
The project is based on [configurable notifying PokemonGo-Finder](https://github.com/jxmorris12/PokemonGo-Finder), a fork of [the popular PokemonGo-Map repository](https://github.com/AHAAAAAAA/PokemonGo-Map).

## Config File
All arguments are read from a `config.json` file. In addition to all of the options laid out [here](https://github.com/AHAAAAAAA/PokemonGo-Map/wiki/Usage), I've introduced two required fields: `slack_api_token`, your Slack API key, and `notify`, a comma-separated list of the Pokemon that you'd like to receive Pushbullet notifications for.

Here's a sample `config.json`:

```
{
  "auth_service": "google",
  "username": "myemailuser",
  "password": "pikachu123",
  "step_limit": 5,
  "location": "742 Evergreen Terrace, Arlington, VA",
  "notify": "dratini,magnemite,electabuzz,hitmonchan,hitmonlee,chansey,lapras,snorlax,porygon,mew,mewtwo,moltres,zapdos,articuno,ditto,seel,gyarados,cubone",
  "slack_api_token": "o.XyDeiVeYuM5eSv2ssy7AlFGLDl4ajEXj"
}
```

## Install

Install the necessary dependencies (including the Slack client) by running `pip install --upgrade -r requirements.txt`. Create a config file and then run the main script using `python main.py`.

*Using this software is against the ToS and can get you banned. Use at your own risk.*

## Screenshots

<p align="center">
<img src="https://raw.githubusercontent.com/AHAAAAAAA/PokemonGo-Map/master/static/cover.png">
</p>
