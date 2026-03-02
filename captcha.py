import tkinter as tk
from PIL import Image, ImageTk
import random as rnd

rnd.seed()
DATA = {"apple":1, "car":0, "banana":1, "pineapple":1, "mango":1, "tire":0, "steering":0, "wheel":0}
#str:key, if key1 == key2 then str1 and str2 are related

def validate(mainWord, validWords, words):#will use tkinter display, button select, submit calls this
    if words[0] == '':
        for word in validWords:
            if DATA[word] == DATA[mainWord]:
                return False
    else:
        for word in words:
            if DATA[word] != DATA[mainWord]:
                return False

        for word in validWords:
            if (DATA[word] == DATA[mainWord]) & (word not in words):
                return False

    return True

def randomised():#returns str list(str)
    words = list(DATA.keys())

    usedInd = list()

    while len(usedInd) < 4:
        ind = rnd.randrange(len(words))
        if ind not in usedInd:
            usedInd.append(ind)

    validWords = [words[usedInd[i]] for i in range(1,4)]
    mainWord = words[usedInd[0]]

    return mainWord, validWords

class TuringTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Semantic Turing Test")
        self.root.geometry("600x600")

        # Top instruction label
        self.title_label = tk.Label(
            root,
            text="Select the correct distorted words related to this word",
            font=("Arial", 14)
        )
        self.title_label.pack(pady=20)

        self.main_word, self.valid_words = randomised()
        # Load main distorted word image (apple as placeholder)
        self.main_image = self.load_image(f"images/{self.main_word}.png", (200, 80))
        self.main_image_label = tk.Label(root, image=self.main_image)
        self.main_image_label.pack(pady=20)

        # Frame for options
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=20)

        self.check_vars = []
        self.option_images = []

        for word in self.valid_words:
            option_frame = tk.Frame(self.options_frame)
            option_frame.pack(side="left", padx=20)

            img = self.load_image(f"images/{word}.png", (150, 60))
            self.option_images.append(img)  # Keep reference

            img_label = tk.Label(option_frame, image=img)
            img_label.pack()

            var = tk.BooleanVar()
            self.check_vars.append(var)

            checkbox = tk.Checkbutton(option_frame, variable=var)
            checkbox.pack(pady=5)

        # Submit button
        self.submit_button = tk.Button(
            root,
            text="Submit",
            command=self.evaluate_selection
        )
        self.submit_button.pack(pady=20)

        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.quit_button = tk.Button(
            root,
            text="Quit",
            command=self.root.destroy
        )
        self.quit_button.pack(pady=10)

    def load_image(self, path, size):
        img = Image.open(path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)

    def evaluate_selection(self):
        selected = [
            word for word, var in zip(self.valid_words, self.check_vars)
            if var.get()
        ]

        truth_val = validate(self.main_word, self.valid_words, selected)
        if truth_val:
            self.result_label.config(text="You are a human")
        else:
            self.result_label.config(text="You are a bot")


if __name__ == "__main__":
    root = tk.Tk()
    app = TuringTestApp(root)
    root.mainloop()
