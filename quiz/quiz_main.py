import customtkinter as ctk

import settings
import dict.dictionary_page as dictionary_page
import quiz.quiz_list as quiz_list
import dict.translator as translator


class Quiz_Page(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)

        self.master = master
        self.frame = ctk.CTkFrame(self.master, fg_color=settings.BACKGROUND)
        self.app = app

        # data
        self.kanji_answer = ctk.StringVar()
        self.kanji_question = ctk.StringVar()
        self.response_answer = ctk.StringVar()
        self.updateVariables()

        # fonts
        kanji_font = ctk.CTkFont(settings.FONT, 60, weight="bold")

        # layout

        self.frame.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.frame.rowconfigure((0, 1), weight=1, uniform="a")

        # QUIZ BOX
        self.quiz_box = Quiz_Box(self.frame,
                                 kanji_font,
                                 self.kanji_question).grid(column=0, row=0, columnspan=3, padx=50, pady=20,
                                                           sticky="nsew")

        # SUBMIT ANSWER BUTTON
        self.submit = Submit(self.frame,
                             kanji_font,
                             self.response_answer,
                             self.kanji_answer,
                             self).grid(column=0, row=2, columnspan=3, padx=50, pady=20, sticky="nsew")

        # BACK BUTTON
        self.back = Back_Button(self.frame,
                                kanji_font,
                                self).grid(column=0, row=2, padx=50, pady=20, sticky="nsew")

        # DICT BUTTON

        self.back = Dict_Button(self.frame,
                                kanji_font,
                                self).grid(column=2, row=2, padx=50, pady=25, sticky="nsew")

        # REVEAL BUTTON
        self.reveal = Whats_Answer_Button(self.frame,
                                          kanji_font).grid(column=0, row=1, columnspan=3, padx=50, pady=20,
                                                           sticky="nsew")

    def start_quiz_page(self):
        self.frame.pack(fill="both", expand=True)

    def go_back(self):
        self.frame.pack_forget()
        self.app.home_page()

    def quiz_to_dict(self):
        self.app.make_dict_page()
        self.frame.pack_forget()
        to_load = self.kanji_answer.get()
        if not to_load[0].isalpha():
            x = to_load.index("'")
            y = to_load.index(",")
            to_load = to_load[x:y]
            to_load = to_load.replace("'", "")
        self.app.dictionary_page.load_from_quiz(to_load)

    def updateVariables(self):
        global answers
        answers = quiz_list.getAnswers()
        print(answers)
        self.kanji_question.set(answers[0])
        self.kanji_answer.set(answers[1])


class Quiz_Box(ctk.CTkFrame):
    def __init__(self, master, font, kanji_answer):
        super().__init__(master, fg_color=settings.BACKGROUND)

        ctk.CTkLabel(self,
                     text="kanji",
                     font=font,
                     textvariable=kanji_answer,
                     corner_radius=40,
                     fg_color=settings.FOREGROUND).pack(expand=True, fill="both")


class Submit(ctk.CTkFrame):
    def __init__(self, master, font, response_answer, kanji_answer, answersDestination):
        super().__init__(master, fg_color=settings.BACKGROUND)
        ctk.CTkEntry(self,
                     placeholder_text="name",
                     justify="center",
                     font=font,
                     textvariable=response_answer,
                     corner_radius=10,
                     width=500,
                     takefocus=True).pack(pady=20)

        ctk.CTkButton(self,
                      text="Submit",
                      command=lambda: quiz_list.checkAnswer(response_answer, kanji_answer, answersDestination),
                      width=500, height=70,
                      corner_radius=30).pack()


class Back_Button(ctk.CTkFrame):
    def __init__(self, master, font, mast2):
        super().__init__(master, fg_color="transparent")

        ctk.CTkButton(self, text="Back",
                      font=font,
                      command=mast2.go_back).pack(side="right", expand=True)


class Whats_Answer_Button(ctk.CTkFrame):
    def __init__(self, master, font):
        super().__init__(master, fg_color="transparent")

        self.answer_text = ctk.StringVar()

        ctk.CTkButton(self, text="Reveal",
                      font=font,
                      command=lambda: self.answer_text.set(self.getAnswer())).place(relx=0.5, rely=0.3, anchor="center")

        ctk.CTkLabel(self, textvariable=self.answer_text, justify="center", font=font).place(relx=0.5, rely=0.8,
                                                                                             anchor="center")

    def getAnswer(self):
        ans = ""
        if type(answers[1]) == list:
            for x in answers[1]:
                ans += x + ", "
            ans = ans.lstrip(" ")
            return ans[:-2]
        else:
            ans = answers[1]
            return ans


class Dict_Button(ctk.CTkFrame):
    def __init__(self, master, font, mast2):
        super().__init__(master, fg_color="transparent")

        ctk.CTkButton(self, text="Load in\nDictionary",
                      font=font,
                      command=mast2.quiz_to_dict).pack(side="right", expand=True)
