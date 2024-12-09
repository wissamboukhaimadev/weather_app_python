import customtkinter as ctk
from utils.display_graph import display_graph
from utils.get_city_lattidude_longitude import get_coordinates
from utils.get_data_for_city_history import get_data_city_history
from tkinter import filedialog
import json

time_data=None
weather_code_data=None
temperature_max_data=None
temperature_mean_data=None
precipitation_sum_data=None
rain_sum_data=None
wind_speed_data=None

completed_search=None

def search_for_city(input_box):
    global time_data, weather_code_data, temperature_max_data, temperature_mean_data, precipitation_sum_data, rain_sum_data, wind_speed_data

    entered_text=input_box.get()
    latitude, longitude= get_coordinates(entered_text)
    if entered_text.strip():  
        data_time, data_weather_code, data_temperature_max, data_temperature_mean, data_precipitation_sum, data_rain_sum, data_wind_speed_10m_max= get_data_city_history(latitude, longitude)

        time_data=data_time
        weather_code_data=data_weather_code
        temperature_max_data=data_temperature_max
        temperature_mean_data=data_temperature_mean
        precipitation_sum_data=data_precipitation_sum
        rain_sum_data=data_rain_sum
        wind_speed_data=data_wind_speed_10m_max

        completed_search.configure(text="search complete, display data using the button")

def display_button_graph(frame,select_combobox):

    if select_combobox.get()=="max temperature":
        display_graph(frame, time_data, temperature_max_data)
    elif select_combobox.get()=="mean temperature":
        display_graph(frame, time_data, temperature_mean_data)
    elif select_combobox.get()=="precipitation":
        display_graph(frame, time_data, precipitation_sum_data)
    elif select_combobox.get()=="rain":
        display_graph(frame, time_data, rain_sum_data)
    else :
        display_graph(frame, time_data, wind_speed_data)
    completed_search.configure(text="")
    

def prepare_data_for_save(select_combobox):
    data={
        "x_coordinates":time_data,
        "y_coordinates": temperature_mean_data
    }

    if select_combobox.get()=="max temperature":
        data["y_coordinates"]=temperature_max_data
    elif select_combobox.get()=="mean temperature":
        data["y_coordinates"]=temperature_mean_data
    elif select_combobox.get()=="precipitation":
        data["y_coordinates"]=precipitation_sum_data
    elif select_combobox.get()=="rain":
        data["y_coordinates"]=rain_sum_data
    else :
        data["y_coordinates"]=wind_speed_data

    return data

def save_data_on_disk(select_combobox):
    data=prepare_data_for_save(select_combobox)
    file_path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
        title="Save JSON File"
    )
    if file_path:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

def load_data_from_disk(frame):

    file_path = filedialog.askopenfilename(
        defaultextension=".json",
        filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
        title="Save JSON File"
    )
    if file_path:
        with open(file_path, 'r') as json_file:
            data=json.load(json_file)
        
        display_graph(frame, data["x_coordinates"], data["y_coordinates"])

def show_history_page(history_frame):
    global completed_search

    input_box=ctk.CTkEntry(history_frame, placeholder_text="type a city")
    input_box.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

    button_box=ctk.CTkButton(history_frame, text="search", command=lambda : search_for_city(input_box) )
    button_box.grid(row=0, column=1, pady=20, sticky="ew")


    select_combobox=ctk.CTkOptionMenu(history_frame, values=["max temperature", "mean temperature", "precipitation", "rain", "wind"] )
    select_combobox.set("max temperature")
    select_combobox.grid(row=1, column=1, pady=5, sticky="ew")

    completed_search=ctk.CTkLabel(history_frame, text="")
    completed_search.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    

    save_button=ctk.CTkButton(history_frame, text="save data", command=lambda: save_data_on_disk(select_combobox))
    save_button.grid(row=4, column=1, padx=20, pady=20, sticky="ew")

    

    graph_frame = ctk.CTkFrame(history_frame, fg_color="transparent")
    graph_frame.grid(row=6, column=0, padx=20, pady=20, sticky="ew")


    display_button=ctk.CTkButton(history_frame, text="display data", command=lambda: display_button_graph(graph_frame,select_combobox))
    display_button.grid(row=3, column=1, padx=20, pady=20, sticky="ew")

    load_button=ctk.CTkButton(history_frame, text="load data", command=lambda: load_data_from_disk(graph_frame))
    load_button.grid(row=5, column=1, padx=20, pady=20, sticky="ew")
