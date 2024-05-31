class Answers:
    def __init__(self, kanji, phonetic, kana, name, vocab_phonetic=None, vocab=None):
        self.kanji = kanji
        self.phonetic = phonetic
        self.kana = kana
        self.name = name
        self.vocab = vocab
        self.vocab_phonetic = vocab_phonetic


kanji_objects = [
    # numbers
    Answers("一", "ichi", "いち", ["one", "1"], "ichi", "いち"),
    Answers("二", "ni", "に", ["two", "ni", "2"], "に"),
    Answers("三", "san", "さん", ["three", "3"], "san", "さん"),
    Answers("五", "-", "-", ["five", "5"], "-", "-"),
    Answers("六", "roku", "ろく", ["six", "6"], "-", "-"),
    Answers("七", "shichi", "しち", ["seven", "7"], "nana", "なな"),
    Answers("八", "hachi", "はち", ["eight", "8"], "hachi", "はち"),
    Answers("九", "ku/kyuu", "く/きゅう", ["nine", "9"], "ku/kyuu", "く/きゅう"),
    Answers("十", "jyuu", "いち", ["ten", "10"], "jyuu", "いち"),
    Answers("千", "-", "-", ["one thousand", "thousand", "a thousand", "1000"], "-", "-"),

    # general LEVEL 1
    Answers("工", "kou/ku", "こう/く", "construction"),
    Answers("人", "nin, jin", "にん, じん ", "person", "hito", "ひと", ),
    Answers("山", "san", "さん", "mountain", "yama", "やま"),
    Answers("口", "ku", "く", "mouth", "kuchi", "くち"),
    Answers("上", "jyou", "じょう", "above", "うえ", "ue"),
    Answers("下", "ka", "か", "below", "shita", "した"),
    Answers("入", "nyuu", "にゅう", "enter"),
    Answers("女", "jo", "じょ", "woman", "onna", "おんな"),
    Answers("川", "kawa", "かわ", "river", "kawa", "かわ"),
    Answers("力", "ryoku", "りょく", "power", "chikara", "ちから"),
    Answers("大", "tai", "たい", "big"),

    # vocab LEVEL 1
    Answers("人口", "-", "-", "population", "jinkou", "じんこう", ),
    Answers("一人", "-", "-", ["alone", "one person", "hitori gotoh"], "hitori", "ひとり", ),
    Answers("人工", "-", "-", ["artificial", "man made"], "jinkou", "じんこう", ),
    Answers("上げる", "-", "-", ["to lift something", "to raise something"], "ageru", "あげる", ),
    Answers("ふじ山", "-", "-", ["fuji", "mt fuji", "mountain fuji", "mount fuji"], "fujisan", "ふじさん"),

    # general LEVEL 2
    Answers("水", "-", "-", "water"),
    Answers("土", "-", "-", "dirt"),
    Answers("刀", "-", "-", "sword"),
    Answers("ナ", "-", "-", "narwhal"),
    Answers("丁", "-", "-", "street"),
    Answers("儿", "-", "-", "legs"),
    Answers("冂", "-", "-", "head"),
    Answers("メ", "-", "-", "treasure"),
    Answers("夕", "-", "-", "evening"),
    Answers("子", "-", "-", "child"),
    Answers("小", "-", "-", "small"),
    Answers("弓", "-", "-", "bow"),
    Answers("尸", "-", "-", "flag"),
    Answers("彡", "-", "-", "hair"),
    Answers("天", "-", "-", "heaven"),
    Answers("手", "-", "-", "hand"),
    # kanji LEVEL 2
    Answers("丸", "maru", "まる", "circle"),
    Answers("才", "sai", "さい", "talent"),
    Answers("日", "nicha, jitsu", "にち、じつ", ["sun", "day"]),

    # vocab LEVEL 2
    Answers("入る", "-", "-", ["to enter", "to go in"], "hairu", "はいる"),
    Answers("下げる", "-", "-", "to lower something", "sageru", "さげる"),
    Answers("下さい", "-", "-", "please give me", "kudasai", "ください"),
    Answers("入り口", "-", "-", "entrance", "iriguchi", "いりぐち"),

    # counts
    Answers("一つ", "-", "-", "one thing", "hitotsu", "ひとつ"),
    Answers("二つ", "-", "-", "two things", "futatsu", "ふたつ"),
    Answers("二人", "-", "-", ["pair", "couple", "two people"], "futari", "ふたり"),
    Answers("三つ", "-", "-", "three things", "mittsu", "みっつ"),
    Answers("三人", "-", "-", "three people", "sannin", "さんにん"),
    Answers("七つ", "-", "-", "seven things", "nanatsu", "ななつ"),
    Answers("八つ", "-", "-", "eight things", "yottsu", "やっつ"),
    Answers("九つ", "-", "-", "nine things", "kokonotsu", "ここのつ"),
]
