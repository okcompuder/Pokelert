# Pokémon Go Slackbot 

## Status - Down
Due to the [impact on Niantic's servers](https://www.nianticlabs.com/blog/update-080416/) several services utilizing their API have been shut down, including [PokemonGo-Map](https://github.com/AHAAAAAAA/PokemonGo-Map) used for this slackbot. Playing with the Pokémon data was a blast, but the strain placed on Niantic's server was an understandably fatal issue.

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

## Screenshot
![Screenshot](/pokelert.png?raw=true "Slack Alerts")

*Location links to Google Maps 

*Location distance text and Attack/Defense/Stamina are placeholders

