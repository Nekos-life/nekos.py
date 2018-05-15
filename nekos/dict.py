class JsonDict:
    def __init__(self, my_dict: dict):
        self._dict = my_dict

    def __getattr__(self, key):
        return self._dict.get(key, None)
