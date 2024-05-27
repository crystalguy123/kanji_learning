import customtkinter as ctk
import settings
import translator


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=settings.BACKGROUND)
        self.title("Dictionary")
        self.geometry("600x600")
        self.resizable(False, False)
        self.bind("<Escape>", lambda event: self.quit())

        # layout
        self.columnconfigure((0, 2), weight=2, uniform="a")
        self.columnconfigure(1, weight=1, uniform="a")
        self.rowconfigure((0, 1, 2), weight=3, uniform="a")
        self.rowconfigure(3, weight=1, uniform="a")

        # data
        self.kanji_answer = ctk.StringVar(value="kanji")
        self.phonetic_answer = ctk.StringVar(value="phonetic")
        self.kana_answer = ctk.StringVar(value="kana")
        self.text_input = ctk.StringVar(value="")

        # font
        phonetic_font = ctk.CTkFont(settings.FONT, 40, weight="bold")
        kana_font = ctk.CTkFont(settings.FONT, 40)
        kanji_font = ctk.CTkFont(settings.FONT, 60, weight="bold")

        # start with random kanji, if settings says so
        translator.pick_random(self, settings.RANDOM)

        # top
        ctk.CTkLabel(self,
                     text="kanji",
                     font=kanji_font,
                     textvariable=self.kanji_answer,
                     corner_radius=40,
                     fg_color=settings.FOREGROUND).grid(column=0, row=0, columnspan=3, sticky="nsew", padx=15, pady=15)

        # middle
        ctk.CTkLabel(self,
                     text="phonetic",
                     font=phonetic_font,
                     textvariable=self.phonetic_answer,
                     corner_radius=20,
                     fg_color=settings.FOREGROUND).grid(column=0, row=1, sticky="nsew", padx=15, pady=15)
        ctk.CTkLabel(self,
                     text="kana",
                     font=kana_font,
                     textvariable=self.kana_answer,
                     corner_radius=20,
                     fg_color=settings.FOREGROUND).grid(column=2, row=1, sticky="nsew", padx=15, pady=15)

        # bottom
        ctk.CTkEntry(self,
                     placeholder_text="name",
                     justify="center",
                     font=phonetic_font,
                     textvariable=self.text_input,
                     width=250,
                     corner_radius=10).grid(column=0, row=2, columnspan=3)

        ctk.CTkButton(self,
                      text="Submit",
                      command=lambda: translator.translate(self.text_input, self),
                      width=300, height=80,
                      corner_radius=30).grid(column=0, row=3, columnspan=3, padx=20, pady=10)
        self.mainloop()


App()