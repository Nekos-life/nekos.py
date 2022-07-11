# nekos.py
A Python module that uses Nekos API

## Requirements
- Python 3.6 and up - https://www.python.org/downloads/

# Install
```
pip install nekos.py
```

# Usage example
```py
import nekos

print(nekos.get_neko("meow"))
>>> 'https://cdn.nekos.life/meow/02D1A.jpg'

print(nekos.get_neko("owoify", "Nekos.life is really awesome!"))
>>> 'NYekos.wife is weawwy awesome UwU'
```

# Endpoints
NOTE: You must call them as function's parameter
- tickle
- slap
- poke
- pat
- neko
- meow
- lizard
- kiss
- fox_girl
- feed
- cuddle
- why
- cat
- owoify (Includes parameter `?text=`)
- fact
- ngif
- smug
- baka
- woof
- spoiler (Includes parameter `?text=`)
- wallpaper
- goose
- gecg
- avatar
- waifu
- 8ball
