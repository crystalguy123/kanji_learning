import dict.hiragana_dict as hiragana_dict
import dict.kanjis as kanjis

"""
set all the text values in the app to default, aka '-'
"""


def setDefault(app):
    app.phonetic_kana_answer.set("-")
    app.kana_answer.set("-")
    app.vocab_answer.set("-")
    app.phonetic_vocab_answer.set("-")


"""
set all the text values in the app to the values given by the answer object
"""


def setAll(app, answerObject):
    app.kanji_answer.set(answerObject.kanji)
    app.phonetic_kana_answer.set(answerObject.phonetic)
    app.kana_answer.set(answerObject.kana)
    app.vocab_answer.set(answerObject.vocab)
    app.phonetic_vocab_answer.set(answerObject.vocab_phonetic)
    if type(answerObject.name) == list:
        app.actual_name.set(answerObject.name[0])
    else:
        app.actual_name.set(answerObject.name)


"""
get the input, and immediately run it through the name checker, "correctName"
if is the correct name, immediately set the text to the object
if it's not, set default, but
check if the input is two or three characters long, aka length of a kana
check if the name matches a kana, then set answer or default accordingly 
"""


def translate(text_input, app):
    if type(text_input) == str:
        kanji_name = text_input
    else:
        kanji_name = text_input.get()

    answerObject = correctName(kanji_name, False)
    # CHECK IF KANJI WITH NAME EXISTS
    if answerObject is not False:
        setAll(app, answerObject)
    # THROW "ERROR" IF NOT
    else:
        app.kanji_answer.set("Unknown Kanji! Typo?")
        setDefault(app)
        # CHECK IF KANA, IF NOT KANJI (IN THIS ORDER SO KANJI LIKE "TEN" DON'T GET COUNTED AS KANA
        if type(text_input) == str:
            kanji_name = text_input
        else:
            kanji_name = text_input.get()
        if len(kanji_name) < 4:
            kana = correctName(kanji_name, True)
            if kana is not False:
                # SET KANA
                app.kanji_answer.set(kana)
                app.actual_name.set(kanji_name)

                setDefault(app)
            else:
                # UNKNOWN KANA
                app.kanji_answer.set("Unknown Kana! Typo?")
                app.kanji_answer.set("-")
                setDefault(app)


"""
if this gets called, it means the input is a kana, and thus more than three characters long
attempt to return a kana from the hiragana dictionary with k_name key
if it doesn't work, aka there is no kana, return false
"""


def correctName(k_name, isKana):
    if isKana:
        try:
            return hiragana_dict.kana_dict[k_name]
        except KeyError:

            return False

    """
    figure out if its a list
    if it's a list, check in that list for names
    if not a list, just look for if the name itself matches
    if either match, return the answer object
    """
    for x in kanjis.kanji_objects:
        if type(x.name) == list:
            for y in x.name:
                if y == k_name:
                    return x
        else:
            if x.name == k_name:
                return x

    return False
