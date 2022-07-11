import requests, urllib
from json import loads as json_parse
from json import dumps as json_stringify

APIURL = "https://nekos.life/api/v2"

# ENDPOINTS QUICKDOCS
# [0] - NAME
# [1] - URL
# [2] - JSON GET | {}.get()
ENDPOINTS = [
  ["tickle", "/img/tickle", "url"],
  ["slap", "/img/slap", "url"],
  ["poke", "/img/poke", "url"],
  ["pat", "/img/pat", "url"],
  ["neko", "/img/neko", "url"],
  ["meow", "/img/meow", "url"],
  ["lizard", "/img/lizard", "url"],
  ["kiss", "/img/kiss", "url"],
  ["hug", "/img/hug", "url"],
  ["fox_girl", "/img/fox_girl", "url"],
  ["feed", "/img/feed", "url"],
  ["cuddle", "/img/cuddle", "url"],
  ["why", "/why", "why"],
  ["cat", "/cat", "cat"],
  ["owoify", "/owoify?", "owo"],
  ["fact", "/fact", "fact"],
  ["ngif", "/img/ngif", "url"],
  ["smug", "/img/smug", "url"],
  ["baka", "/img/baka", "url"],
  ["woof", "/img/woof", "url"],
  ["spoiler", "/spoiler?", "owo"],
  ["wallpaper", "/img/wallpaper", "url"],
  ["goose", "/img/goose", "url"],
  ["gecg", "/img/gecg", "url"],
  ["avatar", "/img/avatar", "url"],
  ["waifu", "/img/waifu", "url"],
  ["8ball", "/8ball", "url"]
]

def get_neko(neko_type = str, query_text = str):
  typefound = False
  nekoindex = 0
  for t in ENDPOINTS:
    if neko_type == t[0]:
      typefound = True
      nekoindex = ENDPOINTS.index(t)
  
  if not typefound == True:
    return f"Type \"{neko_type}\" not found."
    exit()

  reqURL = APIURL + eval(f"ENDPOINTS[{nekoindex}][1]")

  if ENDPOINTS[nekoindex][1].endswith("?"):
    if query_text:
        reqURL = f"{reqURL}text={urllib.parse.quote(query_text)}"

  req = requests.get(reqURL).content.decode("ascii")
  resp = json_parse(req).get(eval(f"ENDPOINTS[{nekoindex}][2]"))
  return resp