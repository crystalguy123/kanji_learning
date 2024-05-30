import dict.hiragana_dict as hiragana_dict
import dict.translator as translator
import random


kanji_list = translator.kanji_objects


def getAnswers():
    if random.randint(1, 2) == 1:
        # kanji, object
        # pick random object
        random_kanji_object = random.choice(kanji_list)
        # set

        # kanji
        question = random_kanji_object.kanji
        # list of names
        answer = random_kanji_object.name
        return question, answer
    else:
        # kana, dictionary
        answer, question = random.choice(list(hiragana_dict.kana_dict.items()))
        return question, answer


def checkAnswer(response, answer, app):
    if "," in answer.get():
        answer = answer.get().replace("(", "").replace(")", "").replace("'", "").split(",")
        print(answer)
        for x in answer:
            x.lstrip(" ")
            if x[0] == " ":
                x = x[1:]
                if response.get() == x:
                    app.updateVariables()
    else:
        if response.get() == answer.get():
            app.updateVariables()
