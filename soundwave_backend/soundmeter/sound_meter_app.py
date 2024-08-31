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

        # Variables pour afficher les niveaux sonores
        self.sound_level = tk.DoubleVar(value=0.0)
        self.min_level = tk.DoubleVar(value=0.0)
        self.max_level = tk.DoubleVar(value=0.0)
        self.avg_level = tk.DoubleVar(value=0.0)
        self.measure_time = tk.StringVar(value="00:00")

        self.is_measuring = False
        self.arduino_thread = None
        self.serial_connection = None

        self.create_widgets()
        self.start_reading()  # Démarrage immédiat de la lecture


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
        self.stop_button = tk.Button(self.root, text="Stop Measuring", command=self.stop_measuring, state=tk.NORMAL)
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

    def start_reading(self):
        self.is_measuring = True

        self.port = find_arduino_port()
        if not self.port:
            messagebox.showerror("Error", "Arduino not found. Please connect the Arduino.")
            return

        try:
            self.serial_connection = serial.Serial(self.port, 9600, timeout=1)
        except serial.SerialException as e:
            messagebox.showerror("Error", f"Failed to connect to Arduino: {e}")
            return

        self.arduino_thread = threading.Thread(target=self.read_arduino_data)
        self.arduino_thread.start()

    def stop_measuring(self):
        self.is_measuring = False
        self.stop_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.NORMAL)
        
        if self.serial_connection:
            self.serial_connection.close()

    def read_arduino_data(self):
        self.start_time = time.time()
        min_level = float('inf')
        max_level = 0
        total_level = 0
        count = 0

        while self.is_measuring and self.serial_connection.is_open:
            line = self.serial_connection.readline().decode('utf-8').strip()
            if line.startswith("CURRENT:"):
                try:
                    # Parse the values from the serial data
                    data = line.split(',')
                    current_dB = float(data[0].split(':')[1])
                    min_dB = float(data[1].split(':')[1])
                    max_dB = float(data[2].split(':')[1])
                    avg_dB = float(data[3].split(':')[1])

                    # Update the GUI with the received values
                    self.sound_level.set(current_dB)
                    self.min_level.set(min_dB)
                    self.max_level.set(max_dB)
                    self.avg_level.set(avg_dB)
                    
                    count += 1

                    # Update the timer
                    elapsed_time = time.time() - self.start_time
                    minutes = int(elapsed_time // 60)
                    seconds = int(elapsed_time % 60)
                    self.measure_time.set(f"{minutes:02d}:{seconds:02d}")

                except (ValueError, IndexError) as e:
                    print(f"Error parsing data: {e}")

            time.sleep(0.2)  # Wait before the next read

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
        self.min_level.set(0.0)
        self.max_level.set(0.0)
        self.avg_level.set(0.0)
        self.measure_time.set("00:00")
        self.save_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = ElectronicSoundMeterApp(root)
    root.mainloop()
