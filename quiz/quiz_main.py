import customtkinter as ctk

import settings
import dict.translator as translator
import quiz.quiz_list as quiz_list


class Quiz_Page(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.frame = ctk.CTkFrame(self.master, fg_color=settings.BACKGROUND)
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
                                 self.kanji_question).grid(column=0, row=0, columnspan=3, padx=50, pady=20, sticky="nsew")

        # SUBMIT ANSWER BUTTON
        self.submit = Submit(self.frame,
                             kanji_font,
                             self.response_answer,
                             self.kanji_answer,
                             self).grid(column=0, row=2, columnspan=3, padx=50, pady=20, sticky="nsew")

        # BACK BUTTON
        self.back = Back_Button(self.frame,
                                kanji_font,
                                self).place(relx=0, rely=1, anchor="sw")

    def start_quiz_page(self):
        self.frame.pack(fill="both", expand=True)

    def go_back(self):
        self.frame.pack_forget()

    def updateVariables(self):
        answers = quiz_list.getAnswers()
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
    def __init__(self, master, font, response_answer, kanji_answer, answersDesination):
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
                      command=lambda: quiz_list.checkAnswer(response_answer, kanji_answer, answersDesination),
                      width=500, height=70,
                      corner_radius=30).pack()


class Back_Button(ctk.CTkFrame):
    def __init__(self, master, font, mast2):
        super().__init__(master, fg_color="transparent")

        ctk.CTkButton(self, text="Back",
                      font=font,
                      command=mast2.go_back).place(relx=0, rely=1, x=25, y=-25, anchor="sw")