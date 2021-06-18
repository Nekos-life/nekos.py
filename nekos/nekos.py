from urllib.parse import quote

from .http import http
from .errors import EmptyArgument, InvalidArgument


def cat() -> str:
    return http.get("/img/meow")["url"]


def eightball() -> dict:
    response = http.get("/8ball")
    return {"text": response["response"], "image": response["url"]}


def fact() -> str:
    return http.get("/fact")["fact"]


def img(tag: str) -> str:
    possible = [
        "feet",
        "yuri",
        "trap",
        "futanari",
        "hololewd",
        "lewdkemo",
        "solog",
        "feetg",
        "cum",
        "erokemo",
        "les",
        "wallpaper",
        "lewdk",
        "ngif",
        "tickle",
        "lewd",
        "feed",
        "gecg",
        "eroyuri",
        "eron",
        "cum_jpg",
        "bj",
        "nsfw_neko_gif",
        "solo",
        "kemonomimi",
        "nsfw_avatar",
        "gasm",
        "poke",
        "anal",
        "slap",
        "hentai",
        "avatar",
        "erofeet",
        "holo",
        "keta",
        "blowjob",
        "pussy",
        "tits",
        "holoero",
        "lizard",
        "pussy_jpg",
        "pwankg",
        "classic",
        "kuni",
        "waifu",
        "pat",
        "8ball",
        "kiss",
        "femdom",
        "neko",
        "spank",
        "cuddle",
        "erok",
        "fox_girl",
        "boobs",
        "Random_hentai_gif",
        "smallboobs",
        "hug",
        "ero",
        "smug",
        "goose",
        "baka",
        "woof",
    ]

    if tag not in possible:
        raise InvalidArgument(
            f"The tag provided does not exist, \npossible tags: {possible}"
        )
    return http.get(f"/img/{tag}")["url"]


def owoify(text: str) -> str:
    return http.get(f"/owoify?text={quote(text)}")["owo"]


def textcat() -> str:
    return http.get("/cat")["cat"]


def why() -> str:
    return http.get("/why")["why"]
