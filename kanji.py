import customtkinter as ctk
import settings
import translator


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=settings.BACKGROUND)
        self.title("Dictionary")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.bind("<Escape>", lambda event: self.quit())

        # layout
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")

        # data
        self.kanji_answer = ctk.StringVar(value="kanji")
        self.phonetic_kana_answer = ctk.StringVar(value="phonetic kanji")
        self.kana_answer = ctk.StringVar(value="kana")
        self.vocab_answer = ctk.StringVar(value="vocab")
        self.phonetic_vocab_answer = ctk.StringVar(value="phonetic vocab")
        self.text_input = ctk.StringVar(value="")

        # font
        phonetic_font = ctk.CTkFont(settings.FONT, 40, weight="bold")
        kana_font = ctk.CTkFont(settings.FONT, 40)
        kanji_font = ctk.CTkFont(settings.FONT, 60, weight="bold")

        # KANJI

        Kanji(self, self.kanji_answer, kanji_font).grid(column=0, row=0, columnspan=4, sticky="nsew", padx=150, pady=10)

        # ANSWERS
        AnswerSection(self, self.phonetic_kana_answer, phonetic_font, "Phonetic").grid(column=0, row=1, rowspan=2, sticky="nsew", padx=15, pady=15)
        AnswerSection(self, self.kana_answer, kana_font, "Kana").grid(column=1, row=1, rowspan=2, sticky="nsew", padx=15, pady=15)
        AnswerSection(self, self.vocab_answer, kana_font, "Vocab Kana").grid(column=2, row=1, rowspan=2, sticky="nsew", padx=15, pady=15)
        AnswerSection(self, self.phonetic_vocab_answer, phonetic_font, "Vocab Phonetic").grid(column=3, row=1, rowspan=2, sticky="nsew", padx=15, pady=15)

        # ENTRY AND BUTTON
        Submit(self, self.text_input, phonetic_font).grid(row=3, column=0, columnspan=4, rowspan=2, sticky="nsew")

        self.mainloop()


class Kanji(ctk.CTkFrame):
    def __init__(self, master, kanji_answer, font):
        super().__init__(master, fg_color=settings.BACKGROUND)
        ctk.CTkLabel(self,
                     text="kanji",
                     font=font,
                     textvariable=kanji_answer,
                     corner_radius=40,
                     fg_color=settings.FOREGROUND).pack(expand=True, fill="both")


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
    def __init__(self, master, text_input, font):
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
                      command=lambda: translator.translate(text_input, master),
                      width=500, height=70,
                      corner_radius=30).pack()


App()