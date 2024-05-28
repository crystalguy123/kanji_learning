import random
import hiragana_dict


def setDefault(app):
    app.phonetic_kana_answer.set("-")
    app.kana_answer.set("-")
    app.vocab_answer.set("-")
    app.phonetic_vocab_answer.set("-")


def setAll(app, answerObject):
    app.kanji_answer.set(answerObject[0].kanji)
    app.phonetic_kana_answer.set(answerObject[0].phonetic)
    app.kana_answer.set(answerObject[0].kana)
    app.vocab_answer.set(answerObject[0].vocab)
    app.phonetic_vocab_answer.set(answerObject[0].vocab_phonetic)


def translate(text_input, app, random_start=False):
    # SET RANDOM
    if random_start is False:
        # DEFAULT
        kanji_name = text_input.get()
        answerObject = correctName(kanji_name, False)
    elif random_start is None:
        # SET NO VALUE
        setDefault(app)
        answerObject = False
    else:
        # IS RANDOM
        answerObject = text_input
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


class Answers:
    def __init__(self, kanji, phonetic, kana, name, vocab_phonetic=None, vocab=None):
        self.kanji = kanji
        self.phonetic = phonetic
        self.kana = kana
        self.name = name
        self.vocab = vocab
        self.vocab_phonetic = vocab_phonetic


# all the kanji objects
kanji_objects = [
    # kanji, phonetic, kana, kanji name, vocab
    # numbers
    Answers("一", "ichi", "いち", "one", "ichi", "いち"),
    Answers("二", "ni", "に", "two", "ni", "に"),
    Answers("三", "san", "さん ", "three", "san", "さん "),
    Answers("七", "shichi", "しち", "seven", "nana", "なな"),
    Answers("八", "hachi", "はち", "eight", "hachi", "はち"),
    Answers("九", "ku/kyuu", "く/きゅう", "nine", "ku/kyuu", "く/きゅう"),
    Answers("一", "jyuu", "いち", "ten", "jyuu", "いち"),

    # other
    Answers("工", "kou/ku", "こう/く", "construction"),
    Answers("人", "hito", "ひと", "person"),
    Answers("山", "san", "さん", "mountain"),
    Answers("口", "ku", "く", "mouth", "kuchi", "くち"),
    Answers("上", "jyou", "じょう", "above", "うえ", "ue"),
    Answers("下", "ka", "か", "below"),
    Answers("入", "nyuu", "にゅう", "enter"),
    Answers("女", "jo", "じょ", "woman", "onna", "おんな"),
    Answers("川", "kawa", "かわ", "river", "kawa", "かわ"),
    Answers("力", "ryoku", "りょく", "power"),
    Answers("大", "tai", "たい", "big"),

    # vocab
    Answers("人口", "-", "-", "population", "jinkou", "じんこう",),
    Answers("一人", "-", "-", "alone", "hitori", "ひとり",),
    Answers("人工", "-", "-", "artificial", "jinkou", "じんこう",),
    Answers("上げる", "-", "-", "to lift something", "ageru", "あげる",),
    # counts
    Answers("一つ", "-", "-", "one thing", "hitotsu", "ひとつ"),
    Answers("三つ", "-", "-", "three things", "mittsu", "みっつ"),
    Answers("三人", "-", "-", "three people", "sannin", "さんにん"),
    Answers("八つ", "-", "-", "eight things", "yottsu", "やっつ"),
    Answers("七つ", "-", "-", "seven things", "nanatsu", "ななつ")]


# check if name is a real name
def correctName(k_name, isKana):
    if isKana:  # the object is one or two characters long, so check if matches in kana list
        try:
            return hiragana_dict.kana_dict[k_name]
        except KeyError:

            return False
    # loop through all the kanji's names to confirm if the name provided is actually a real name, then return the kanji object if true
    for x in kanji_objects:
        if x.name == k_name:
            return x, True

    return False


def pick_random(app, start_random):
    if start_random:
        translate(random.choice(kanji_objects), app, True)
