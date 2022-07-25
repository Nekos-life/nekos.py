import urllib

from . import http, dict, errors

noresponse = "Couldn't contact the API right now..."


def eightball():
    r = http.get("/8ball")
    return dict.JsonDict({"text": r["response"], "image": r["url"]})


def img(target: str):
    possible = [
        "wallpaper",
        "ngif",
        "tickle",
        # "lewd", Provides 1 image
        "feed",
        "gecg",
        "gasm",
        "slap",
        "avatar",
        "lizard",
        "waifu",
        "pat",
        "8ball",
        "kiss",
        "neko",
        "spank",
        "cuddle",
        "fox_girl",
        "hug",
        "smug",
        "goose",
        "woof",
    ]

    if target is None:
        raise errors.EmptyArgument(f"You have to at least define an argument in string format\nArguments: {possible}")


    if target.lower() not in possible:
        raise errors.InvalidArgument(f"You haven't added any valid arguments\nArguments: {possible}")


    try:
        if target.lower() == "random_hentai_gif":
            r = http.get("/img/Random_hentai_gif")
        else:
            r = http.get(f"/img/{target.lower()}")
    except Exception as e:
        raise errors.NothingFound(noresponse) from e

    return r["url"]


def owoify(text: str):
    if text is None:
        raise errors.EmptyArgument(
            "You have to enter a string you want to enter to API"
        )

    r = http.get(f"/owoify?text={urllib.parse.quote(text)}")
    return r["owo"]


def spoiler(text: str):
    if text is None:
        raise errors.EmptyArgument(
            "You have to enter a string you want to enter to API"
        )

    r = http.get(f"/spoiler?text={urllib.parse.quote(text)}")
    return r["owo"]


def cat():
    try:
        return http.get("/img/meow")["url"]
    except Exception as e:
        raise errors.NothingFound(noresponse) from e


def textcat():
    try:
        return http.get("/cat")["cat"]
    except Exception as e:
        raise errors.NothingFound(noresponse) from e


def why():
    try:
        return http.get("/why")["why"]
    except Exception as e:
        raise errors.NothingFound(noresponse) from e


def fact():
    try:
        return http.get("/fact")["fact"]
    except Exception as e:
        raise errors.NothingFound(noresponse) from e


def name():
    try:
        return http.get("/name")["name"]
    except Exception as e:
        raise errors.NothingFound(noresponse) from e
