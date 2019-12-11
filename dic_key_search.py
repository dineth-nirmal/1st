def get_meaning(word):
    meaning = []
    key_types = [word, word.title(), word.upper(), word.lower()]
    for type in key_types:
        try:
            if len(meaning) > 0:
                break
            meaning = data[type]
        except:
            pass
    return meaning
