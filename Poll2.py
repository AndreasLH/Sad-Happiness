import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as pd
import os
import platform
if platform.system() == 'Windows':
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
import random  # Import the random module

class PollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Poll")

        self.responses = []
        self.current_image_index = 0

        # Prompt the user for their name
        self.participant_name = self.get_participant_name()

        self.load_images()
        self.create_interface()
        self.create_dataframe()

    def get_participant_name(self):
        # Create a simple dialog to input the participant's name
        participant_name = tk.simpledialog.askstring("Participant's Name", "Please enter your name:")
        if participant_name is None:
            participant_name = "N/A"  # Set a default name if none is provided
        return participant_name

    def load_images(self):
        # Load images from KDEF_Straight folder
        self.image_paths = 40*[os.getcwd() + os.sep + "Experiment2" + os.sep + filename for filename in os.listdir("Experiment2")]
        # Shuffle the image_paths list
        random.shuffle(self.image_paths)
        self.images = [Image.open(path).resize((450, 610)) for path in self.image_paths]

    def create_interface(self):
        self.image_label = ttk.Label(self.root)
        self.image_label.pack(padx=20, pady=20)

        self.response_label = ttk.Label(self.root, text="How happy is this person?", font=("Helvetica", 24))
        self.response_label.pack(pady=10)

        self.response_var = tk.StringVar()
        self.response_var.set("")  # Initialize as empty

        option_happy_button = ttk.Button(self.root, text="happy", command=lambda: self.record_response("1"))
        option_nothappy_button = ttk.Button(self.root, text="not happy", command=lambda: self.record_response("0"))

        option_happy_button.pack(side="left", padx=10)
        option_nothappy_button.pack(side="left", padx=10)

        # Bind the Enter key to "0"
        self.root.bind("d", lambda event=None: self.record_response("0"))
        self.root.bind("k", lambda event=None: self.record_response("1"))

        self.show_next_image()

    def create_dataframe(self):
        self.csv_filename = "poll_responses2.csv"
        # Create a new DataFrame or load an existing one if the file already exists
        if os.path.exists(self.csv_filename):
            self.df = pd.read_csv(self.csv_filename)
        else:
            self.df = pd.DataFrame(columns=["Participant Name", "Image", "Response"])

    def record_response(self, response):
        image_name = self.image_paths[self.current_image_index - 1] if self.current_image_index > 0 else "N/A"
        image_name = os.path.basename(image_name)
        self.responses.append((self.participant_name, image_name, response))
        new_df = pd.DataFrame({"Participant Name": [self.participant_name],
                               "Image": [image_name],
                               "Response": [response]})
        self.df = pd.concat([self.df, new_df], ignore_index=True)
        self.df.to_csv(self.csv_filename, index=False)  # Append to or create the CSV file
        self.show_next_image()

    def show_next_image(self):
        if self.current_image_index < len(self.images):
            image = ImageTk.PhotoImage(self.images[self.current_image_index])
            self.image_label.config(image=image)
            self.image_label.image = image
            self.response_var.set("")  # Reset the response
            self.current_image_index += 1
        else:
            self.finish_poll()

    def finish_poll(self):
        self.image_label.config(image=None)
        self.image_label.pack_forget()
        self.response_label.pack_forget()  # Remove the response label
        self.response_label.config(text="Poll Finished!")

        print(f"Responses saved to {self.csv_filename}")

        # Close the GUI window
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = PollApp(root)
    root.mainloop()
