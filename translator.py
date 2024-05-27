import random


def translate(text_input, app, random_start=False):

    if random_start is False:
        kanji_name = text_input.get()
        answerObject = correctName(kanji_name)
    else:
        answerObject = text_input
    # if it doesn't return false, proceed (it returns false if the name does not match)
    if answerObject is not False:
        app.kanji_answer.set(answerObject.kanji)
        app.phonetic_answer.set(answerObject.phonetic)
        app.kana_answer.set(answerObject.kana)
    else:
        app.kanji_answer.set("Unknown! Typo?")
        app.phonetic_answer.set("-")
        app.kana_answer.set("-")


class Answers:
    def __init__(self, kanji, phonetic, kana, name):
        self.kanji = kanji
        self.phonetic = phonetic
        self.kana = kana
        self.name = name


# all the kanji objects
kanjis = [
    # numbers
    Answers("一", "ichi", "いち", "one"),
    Answers("二", "ni", "に", "two"),
    Answers("三", "san", "さん ", "three"),
    Answers("七", "shichi", "しち", "seven"),
    Answers("八", "hachi", "はち", "eight"),
    Answers("九", "ku", "く", "nine"),
    Answers("一", "jyuu", "いち", "ten"),

    # other
    Answers("工", "kou/ku", "こう/く", "construction"),
    Answers("人", "hito", "ひと", "person"),
    Answers("山", "san", "さん", "mountain"),
    Answers("口", "kuchi", "くち", "mouth"),
    Answers("上", "jyou", "じょう", "above"),
    Answers("下", "ka", "か", "below"),
    Answers("入", "nyuu", "にゅう", "enter"),
    Answers("女", "jo", "じょ", "woman"),
    Answers("川", "kawa", "かわ", "river"),
    Answers("力", "ryoku", "りょく", "power"),
    Answers("大", "tai", "たい", "big"),

    # vocab
    Answers("人口", "jinkou", "じんこう", "population"),
    Answers("一人", "hitori", "ひとり", "alone"),
    Answers("人工", "jinkou", "じんこう", "artificial"),
    # counts
    Answers("一つ", "hitotsu", "ひとつ", "one thing"),
    Answers("三つ", "mittsu", "みっつ", "three things"),
    Answers("三人", "sannin", "さんにん", "three people"),
    Answers("八つ", "yottsu", "やっつ", "eight things"),
    Answers("七つ", "nanatsu", "ななつ", "seven things"),]

# all the names of the kanji
kanji_names = []
for x in kanjis:
    kanji_names.append(x.name)


# check if name is a real name
def correctName(k_name):
    # loop through all the kanji's names to confirm if the name provided is actually a real name, then return the kanji object if true
    for x in kanjis:
        if x.name == k_name:
            return x
    return False


def pick_random(app, start_random):
    if start_random:
        translate(random.choice(kanjis), app, True)