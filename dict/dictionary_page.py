import customtkinter as ctk
import settings
import dict.translator as translator


class Dictionary_Page(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.frame = ctk.CTkFrame(self.master, fg_color=settings.BACKGROUND)

        # layout
        self.frame.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.frame.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")

        # data
        self.kanji_answer = ctk.StringVar(value="kanji")
        self.phonetic_kana_answer = ctk.StringVar(value="phonetic kanji")
        self.kana_answer = ctk.StringVar(value="kana")
        self.vocab_answer = ctk.StringVar(value="vocab")
        self.phonetic_vocab_answer = ctk.StringVar(value="phonetic vocab")
        self.actual_name = ctk.StringVar(value="name")
        self.text_input = ctk.StringVar(value="")

        # fonts
        phonetic_font = ctk.CTkFont(settings.FONT, 40, weight="bold")
        kana_font = ctk.CTkFont(settings.FONT, 40)
        kanji_font = ctk.CTkFont(settings.FONT, 60, weight="bold")

        # KANJI

        Kanji(self.frame, self.kanji_answer, kanji_font).grid(column=0, row=0, columnspan=2,
                                                                                sticky="nsew", padx=15,
                                                                                pady=10)

        # NAME
        Name(self.frame, kanji_font, self.actual_name).grid(column=2, row=0, columnspan=2,
                                                                                sticky="nsew", padx=15,
                                                                                pady=10)

        # ANSWERS
        AnswerSection(self.frame, self.phonetic_kana_answer, phonetic_font, "Kanji Phonetic").grid(column=0, row=1,
                                                                                                   rowspan=2,
                                                                                                   sticky="nsew",
                                                                                                   padx=15,
                                                                                                   pady=15)
        AnswerSection(self.frame, self.kana_answer, kana_font, "Kanji Kana").grid(column=1, row=1, rowspan=2,
                                                                                  sticky="nsew",
                                                                                  padx=15, pady=15)
        AnswerSection(self.frame, self.vocab_answer, kana_font, "Vocab Kana").grid(column=2, row=1, rowspan=2,
                                                                                   sticky="nsew",
                                                                                   padx=15, pady=15)
        AnswerSection(self.frame, self.phonetic_vocab_answer, phonetic_font, "Vocab Phonetic").grid(column=3, row=1,
                                                                                                    rowspan=2,
                                                                                                    sticky="nsew",
                                                                                                    padx=15, pady=15)

        # ENTRY AND BUTTON
        self.submit = Submit(self.frame, self.text_input, phonetic_font, self).grid(row=3, column=0, columnspan=4,
                                                                                    rowspan=2,
                                                                                    sticky="nsew")

        # BACK BUTTON
        self.back = Back_Button(self.frame,
                                kanji_font,
                                self).place(relx=0, rely=1, anchor="sw")

    def start_dict_page(self):
        self.frame.pack(fill="both", expand=True)

    def go_back(self):
        self.frame.pack_forget()
        #self.app.start_page()

    def load_from_quiz(self, to_load):
        translator.translate(to_load, self)


class Kanji(ctk.CTkFrame):
    def __init__(self, master, kanji_answer, font):
        super().__init__(master, fg_color="transparent")
        ctk.CTkLabel(self,
                     text="kanji",
                     font=font,
                     textvariable=kanji_answer,
                     corner_radius=40,
                     fg_color=settings.FOREGROUND).pack(side="left", expand=True, fill="both", padx=15)


class Name(ctk.CTkFrame):
    def __init__(self, master, font, actual_name):
        super().__init__(master, fg_color="transparent")
        ctk.CTkLabel(self,
                     text="name",
                     font=font,
                     textvariable=actual_name,
                     corner_radius=40,
                     fg_color=settings.FOREGROUND).pack(side="left", expand=True, fill="both", padx=15)


class AnswerSection(ctk.CTkFrame):
    def __init__(self, master, answer_variable, font, type):
        super().__init__(master, fg_color=settings.BACKGROUND)

        # answer
        ctk.CTkLabel(self,
                     text="phonetic",
                     font=font,
                     textvariable=answer_variable,
                     corner_radius=20,
                     fg_color=settings.FOREGROUND).pack(fill="both", expand=True)
        # text
        ctk.CTkLabel(self,
                     text=type,
                     font=font,
                     corner_radius=20).pack(fill="both", expand=True)


class Submit(ctk.CTkFrame):
    def __init__(self, master, text_input, font, app):
        super().__init__(master, fg_color=settings.BACKGROUND)
        # bottom
        ctk.CTkEntry(self,
                     placeholder_text="name",
                     justify="center",
                     font=font,
                     textvariable=text_input,
                     corner_radius=10,
                     width=500,
                     takefocus=True).pack(pady=20)

        ctk.CTkButton(self,
                      text="Submit",
                      command=lambda: translator.translate(text_input, app),
                      width=500, height=70,
                      corner_radius=30).pack()


class Back_Button(ctk.CTkFrame):
    def __init__(self, master, font, mast2):
        super().__init__(master, fg_color="transparent")

        ctk.CTkButton(self, text="Back",
                      font=font,
                      command=mast2.go_back).place(relx=0, rely=1, x=25, y=-25, anchor="sw")
