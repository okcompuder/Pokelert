# Pokelert - Pokémon Go Slackbot 

## Overview

This slackbot uses the popular [PokemonGo-Map](https://github.com/AHAAAAAAA/PokemonGo-Map) as an API to notify slack channels about nearby Pokémon. The project will focus on creating a conversational bot UI utilizing online PoGo Tools to help your Slack team be the very best, that no one ever was.

## Config
* Install Python 2.7  
* Install Python pip  
* Install Dependencies
```sh
pip install -r requirements.txt
```
* Install & Run [PokemonGo-Map](https://github.com/AHAAAAAAA/PokemonGo-Map)
* Add config.yaml
```sh
ENDPOINT_URL: http://localhost:5000
SLACK_TOKEN: 
CHANNELS: ['pogo']
```

## Use
Run *main.py* to activate bot in channel
