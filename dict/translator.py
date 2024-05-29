import dict.hiragana_dict as hiragana_dict

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


"""
get the input, and immediately run it through the name checker, "correctName"
if is the correct name, immediately set the text to the object
if it's not, set default, but
check if the input is two or three characters long, aka length of a kana
check if the name matches a kana, then set answer or default accordingly 
"""


def translate(text_input, app):
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
        if len(text_input.get()) < 4:
            kanji_name = text_input.get()
            kana = correctName(kanji_name, True)
            if kana is not False:
                # SET KANA
                app.kanji_answer.set(kana)
                setDefault(app)
            else:
                # UNKNOWN KANA
                app.kanji_answer.set("Unknown Kana! Typo?")
                setDefault(app)


"""
just the class of the answers
no helper functions needed
"""


class Answers:
    def __init__(self, kanji, phonetic, kana, name, vocab_phonetic=None, vocab=None):
        self.kanji = kanji
        self.phonetic = phonetic
        self.kana = kana
        self.name = name
        self.vocab = vocab
        self.vocab_phonetic = vocab_phonetic


"""
this list is every single answer 
eventually i may move it over to another file
answers are formatted like this:
Answers(Kanji, Phonetic Kanji, Kanji Kana, Name, Vocab Phonetic, Vocab Kana
the name is smack dab in the middle because i forgot about vocab initially and i do not want to change it
in the list they are also sorted by numbers, general, and vocab
some are sorted a bit more in those certain subsections but not important enough to be listed here
"""
kanji_objects = [
    # numbers
    Answers("一", "ichi", "いち", ["one", "1"], "ichi", "いち"),
    Answers("二", "ni", "に", ["two", "ni", "2"], "に"),
    Answers("三", "san", "さん ", ["three", "3"], "san", "さん "),
    Answers("七", "shichi", "しち", ["seven", "7"], "nana", "なな"),
    Answers("八", "hachi", "はち", ["eight", "8"], "hachi", "はち"),
    Answers("九", "ku/kyuu", "く/きゅう", ["nine", "9"], "ku/kyuu", "く/きゅう"),
    Answers("一", "jyuu", "いち", ["ten", "10"], "jyuu", "いち"),

    # general
    Answers("工", "kou/ku", "こう/く", "construction"),
    Answers("人", "nin, jin", "にん, じん ", "person", "hito", "ひと", ),
    Answers("山", "san", "さん", "mountain", "yama", "やま"),
    Answers("口", "ku", "く", "mouth", "kuchi", "くち"),
    Answers("上", "jyou", "じょう", "above", "うえ", "ue"),
    Answers("下", "ka", "か", "below", "shita", "した"),
    Answers("入", "nyuu", "にゅう", "enter"),
    Answers("女", "jo", "じょ", "woman", "onna", "おんな"),
    Answers("川", "kawa", "かわ", "river", "kawa", "かわ"),
    Answers("力", "ryoku", "りょく", "power", "shikara", "ちから"),
    Answers("大", "tai", "たい", "big"),

    # vocab
    Answers("人口", "-", "-", "population", "jinkou", "じんこう", ),
    Answers("一人", "-", "-", ["alone", "one person", "hitori gotoh"], "hitori", "ひとり", ),
    Answers("人工", "-", "-", ["artificial", "man made"], "jinkou", "じんこう", ),
    Answers("上げる", "-", "-", ["to lift something", "to raise something"], "ageru", "あげる", ),
    Answers("上げる", "-", "-", ["fuji", "mt fuji", "mountain fuji", "mount fuji"], "fujisan", "ふじさん"),
    # counts
    Answers("一つ", "-", "-", "one thing", "hitotsu", "ひとつ"),
    Answers("二つ", "-", "-", "two things", "futotsu", "ふたつ"),
    Answers("二人", "-", "-", ["pair", "couple", "two people"], "futari", "ふたり"),
    Answers("三つ", "-", "-", "three things", "mittsu", "みっつ"),
    Answers("三人", "-", "-", "three people", "sannin", "さんにん"),
    Answers("七つ", "-", "-", "seven things", "nanatsu", "ななつ"),
    Answers("八つ", "-", "-", "eight things", "yottsu", "やっつ"),
]

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
    for x in kanji_objects:
        if type(x.name) == list:
            for y in x.name:
                if y == k_name:
                    return x
        else:
            if x.name == k_name:
                return x

    return False
