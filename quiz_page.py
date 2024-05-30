import customtkinter as ctk

import quiz.quiz_main
import settings
import dict.dictionary_page as dictionary_page
import dict.translator as translator


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=settings.BACKGROUND)
        self.title("Dictionary and Quiz")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.bind("<Escape>", lambda event: self.quit())

        # font
        font = ctk.CTkFont(settings.FONT, 120, weight="bold")

        # layout
        self.home_frame = ctk.CTkFrame(self, width=1280, height=720, fg_color="transparent")
        self.home_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.dictionary_page = dictionary_page.Dictionary_Page(self)
        self.quiz_page = quiz.quiz_main.Quiz_Page(self)  # folder, file name, class name

        dict_button = ctk.CTkButton(self.home_frame, font=font, text="Dictionary",
                                    width=900, height=300, corner_radius=60, command=self.make_dict_page).place(relx=0.5, rely=0.25,
                                                                                                     anchor="center")
        quiz_button = ctk.CTkButton(self.home_frame, font=font, text="Quizzing",
                                    width=900, height=300, corner_radius=60, command=self.make_quiz_page).place(relx=0.5, rely=0.75,
                                                                                                     anchor="center")

        self.mainloop()

    def home_page(self):
        self.home_frame.place(relx=0.5, rely=0.5, anchor="center")

    def make_dict_page(self):
        self.home_frame.pack_forget()
        self.dictionary_page.start_dict_page()

    def load_in_dict(self):
        self.dictionary_page.text_input.set("woman")
        translator.translate("woman", self.dictionary_page)

    def make_quiz_page(self):
        self.home_frame.pack_forget()
        self.quiz_page.start_quiz_page()

    def remove_frame(self):
        self.home_frame.pack_forget()


App()
