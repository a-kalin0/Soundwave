import serial
import serial.tools.list_ports

import threading
import tkinter as tk 
from tkinter import filedialog, messagebox 
import json 
import time


def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports: 
        if "Arduino" in p.description:
            return p.device
    return None


class ElectronicSoundMeterApp:
    def __init__(self, root):
        self.root = root
        
        self.root.title("Sound Meter")
        self.root.geometry("500x400")

        self.sound_level = tk.DoubleVar(value=50.0)
        self.min_level = tk.DoubleVar(value=45.0)
        self.max_level = tk.DoubleVar(value=55.0)
        self.avg_level = tk.DoubleVar(value=50.0)
        self.measure_time = tk.StringVar(value="00:00")

        self.is_measuring = False
        self.timer_started = False

        self.create_widgets()


    def create_widgets(self):

        tk.Label(self.root, text="Current Sound Level (dB):").pack()
        tk.Label(self.root, textvariable=self.sound_level).pack()

        tk.Label(self.root, text="Min Level (dB):").pack()
        tk.Label(self.root, textvariable=self.min_level).pack()

        tk.Label(self.root, text="Max Level (dB):").pack()
        tk.Label(self.root, textvariable=self.max_level).pack()

        tk.Label(self.root, text="Avg Level (dB):").pack()
        tk.Label(self.root, textvariable=self.avg_level).pack()

        # Timer
        tk.Label(self.root, text="Measurement Time:").pack()
        tk.Label(self.root, textvariable=self.measure_time).pack()

        # Control buttons
        self.start_button = tk.Button(self.root, text="Start Measuring", command=self.start_measuring)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop Measuring", command=self.stop_measuring, state=tk.DISABLED)
        self.stop_button.pack()

        self.save_button = tk.Button(self.root, text="Save Data", command=self.save_data, state=tk.DISABLED)
        self.save_button.pack()

        # Input fields for title and description
        self.title_entry = tk.Entry(self.root)
        self.title_entry.insert(0, "Enter title here")
        self.title_entry.pack()

        self.description_entry = tk.Entry(self.root)
        self.description_entry.insert(0, "Enter description here")
        self.description_entry.pack()

    def start_measuring(self):
        self.is_measuring = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.start_time = time.time()  # Start the timer
        self.update_timer()

        self.sound_level.set(50.0)
        self.min_level.set(45.0)
        self.max_level.set(55.0)
        self.avg_level.set(50.0)

    def stop_measuring(self):
        self.is_measuring = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.NORMAL)

    def update_timer(self):
        if self.is_measuring:
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            self.measure_time.set(f"{minutes:02d}:{seconds:02d}")
            self.root.after(1000, self.update_timer)

    def save_data(self):
        title = self.title_entry.get()
        description = self.description_entry.get()

        if title == "Enter title here" or not title:
            messagebox.showerror("Input Error", "Please enter a valid title")
            return 
        
        if description == "Enter description here" or not description:
            messagebox.showerror("Input Error", "Please enter a valid description.")
            return

        data = {
            'title': title,
            'description': description,
            'min_level': self.min_level.get(),
            'max_level': self.max_level.get(),
            'avg_level': self.avg_level.get(),
            'measurement_time': self.measure_time.get(),
        }

        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path: 
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        
        self.reset_measurements()

    def reset_measurements(self):
        self.min_level.set(45.0)
        self.max_level.set(55.0)
        self.avg_level.set(50.0)
        self.measure_time.set("00:00")
        self.save_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    port = find_arduino_port()
    if port:
        print("ça marche")
        root = tk.Tk()
        app = ElectronicSoundMeterApp(root)
        root.mainloop()
    else:
        print("Arduino not found. Please connect the Arduino and try again.")

