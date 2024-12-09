from PIL import Image
import customtkinter as ctk
from utils.get_city_lattidude_longitude import get_coordinates
from utils.get_data_for_city import get_data_city
from utils.weather_conditions import get_weathercode_icon
from utils.get_data_for_city_history import get_data_city_history
from utils.get_data_for_city_forecast import get_data_city_forecast
import calendar


sun_icon=Image.open("./icons/rain.png")

clear_sky=Image.open("./icons/new/clear-sky.png")
moon=Image.open("./icons/new/moon.png")
partly_cloudy=Image.open("./icons/new/partly-cloudy.png")
overcast=Image.open("./icons/new/overcast.png")
foggy=Image.open("./icons/new/foggy.png")
drizzle=Image.open("./icons/new/drizzle.png")
cloud=Image.open("./icons/new/cloud.png")
freezing_rain=Image.open("./icons/new/freezing_rain.png")
snow=Image.open("./icons/new/snow.png")
shower=Image.open("./icons/new/shower.png")
sun=Image.open("./icons/new/sun.png")



wind_value=None
temperature_value=None
humidity_value=None


forcast_title_labels=[]
forcast_image_labels=[]
forcast_degree_labels=[]


def search_button_command(input_box, city_name, degre_label, image_label):
    entered_text=input_box.get()
    latitude, longitude= get_coordinates(entered_text)

    if entered_text.strip():       
        donne_temperature, donne_humidite, donne_vitesse_vent, donne_heure, donnees_weather_code=get_data_city(latitude, longitude)

        city_name.configure(text=entered_text[0].upper()+entered_text[1:]) 
        degre_label.configure(text=f'{donne_temperature}°') 
        wind_value.configure(text=f'{donne_vitesse_vent} km/h') 
        temperature_value.configure(text=f'{donne_temperature}°') 
        humidity_value.configure(text=f'{donne_humidite} %') 

        dynamic_icon=get_weathercode_icon(donnees_weather_code, clear_sky, moon, partly_cloudy, overcast, foggy, drizzle, cloud, freezing_rain, snow, shower, sun)

        new_image = ctk.CTkImage(light_image=dynamic_icon, dark_image=dynamic_icon, size=(100, 100))
        image_label.configure(image=new_image)

        # city history
        data_time, data_weather_code, data_temperature_max=get_data_city_forecast(latitude,longitude,19)
        for i in range(0,len(data_time)):
            year, month, day=map(int, data_time[i].split('-'))
            day_of_week=calendar.weekday(year, month, day)
            forcast_title_labels[i].configure(text=calendar.day_name[day_of_week]) 
            forcast_degree_labels[i].configure(text=data_temperature_max[i]) 
            dynamic_icon_label=get_weathercode_icon(data_weather_code[i], clear_sky, moon, partly_cloudy, overcast, foggy, drizzle, cloud, freezing_rain, snow, shower, sun)
            new_image = ctk.CTkImage(light_image=dynamic_icon_label, dark_image=dynamic_icon_label, size=(50, 50))

            forcast_image_labels[i].configure(image=new_image)



 

def show_main_content(main_content_frame):
    input_box=ctk.CTkEntry(main_content_frame, placeholder_text="type a city")
    input_box.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

    button_box=ctk.CTkButton(main_content_frame, text="search", command=lambda: search_button_command(input_box, city_name, degre_label, image_label) )
    button_box.grid(row=0, column=1, pady=20)

    header_area=ctk.CTkFrame(main_content_frame, fg_color="transparent")
    header_area.grid(row=1,column=0,pady=20, sticky="ew")
    header_area.columnconfigure(0,weight=1)
    header_area.columnconfigure(1,weight=3)
    header_area.columnconfigure(2,weight=1)

    city_name=ctk.CTkLabel(header_area, text="", font=("Arial", 28, "bold"))
    city_name.grid(row=0, column=0)


    my_image = ctk.CTkImage(light_image=sun_icon, dark_image=sun_icon, size=(100, 100))
    image_label = ctk.CTkLabel(header_area, image=my_image, text="")  
    image_label.grid(row=1, column=3, pady=5, padx=20)


    degre_label=ctk.CTkLabel(header_area, text="", font=("Arial", 31))
    degre_label.grid(row=0, column=1)


    forcast_table=ctk.CTkFrame(main_content_frame, fg_color="#202b3b", corner_radius=20)
    forcast_table.grid(row=2,column=0,pady=20, sticky="ew")

    forcast_table.grid_columnconfigure(0, weight=1)
    forcast_table.grid_columnconfigure(1, weight=0)
    forcast_table.grid_columnconfigure(2, weight=1)
    forcast_table.grid_columnconfigure(3, weight=0)
    forcast_table.grid_columnconfigure(4, weight=1)
    forcast_table.grid_columnconfigure(5, weight=0)
    forcast_table.grid_columnconfigure(6, weight=1)
    forcast_table.grid_columnconfigure(7, weight=0)
    forcast_table.grid_columnconfigure(8, weight=1)
    forcast_table.grid_columnconfigure(9, weight=0)
    forcast_table.grid_columnconfigure(10, weight=1)
    forcast_table.grid_columnconfigure(11, weight=0)
    forcast_table.grid_columnconfigure(12, weight=1)
    forcast_table.grid_columnconfigure(13, weight=0)
    forcast_table.grid_columnconfigure(14, weight=1)

    forcat_title=ctk.CTkLabel(forcast_table, text="Forecast")
    forcat_title.grid(row=0, column=0, padx=10, pady=10)
    
    show_forcast(forcast_table)

    conditions_frame=ctk.CTkFrame(main_content_frame, fg_color="#202b3b", corner_radius=20)
    conditions_frame.grid(row=3,column=0,pady=20, sticky="ew")
    conditions_frame.grid_columnconfigure(0, weight=1)
    conditions_frame.grid_columnconfigure(1, weight=4)
    conditions_frame.grid_columnconfigure(2, weight=1)
    conditions_frame.grid_columnconfigure(3, weight=4)
    conditions_frame.grid_columnconfigure(4, weight=2)
    conditions_frame.grid_columnconfigure(5, weight=1)

    conditions_title=ctk.CTkLabel(conditions_frame, text="Conditions")
    conditions_title.grid(row=0, column=0, padx=10, pady=10)

    show_conditions(conditions_frame)


dates = ["", "", "", "", "", "", ""]


def show_forcast(forcast_table):
    global forcast_title_labels, forcast_image_labels, forcast_degree_labels
    for i in range(0,15):
        date_index = (i // 2)  

        if i%2!=0:
            if date_index < len(dates):
                forcat_title=ctk.CTkLabel(forcast_table, text=dates[date_index], font=("Arial", 18, "bold"))
                forcat_title.grid(row=1, column=i, padx=10, pady=10)
                forcast_title_labels.append(forcat_title)
                

                my_image = ctk.CTkImage(light_image=sun_icon, dark_image=sun_icon, size=(50, 50))
                image_label = ctk.CTkLabel(forcast_table, image=my_image, text="")  
                image_label.grid(row=2, column=i, pady=5, padx=10)
                forcast_image_labels.append(image_label)

                degre_text=ctk.CTkLabel(forcast_table, text="" , font=("Arial", 20, "bold"))
                degre_text.grid(row=3, column=i, padx=10, pady=10)
                forcast_degree_labels.append(degre_text)


def show_conditions(conditions_frame):
    global wind_value, temperature_value, humidity_value

    wind_speed=ctk.CTkLabel(conditions_frame, text="Wind speed", font=("FiraCode Nerd Font", 23), text_color="#6b7280")
    wind_speed.grid(row=1, column=1, padx=10, pady=2, sticky="w")

    wind_value=ctk.CTkLabel(conditions_frame, text="0.0 km/h", font=("Arial", 22, "bold"))
    wind_value.grid(row=2, column=1, padx=20, pady=10, sticky="w")

    temperature_label=ctk.CTkLabel(conditions_frame, text="Temperature", font=("FiraCode Nerd Font", 23), text_color="#6b7280")
    temperature_label.grid(row=1, column=3, padx=200, pady=2, sticky="e")

    temperature_value=ctk.CTkLabel(conditions_frame, text="0.0°", font=("Arial", 22, "bold"))
    temperature_value.grid(row=2, column=3, padx=20, pady=10)

    humidity_label=ctk.CTkLabel(conditions_frame, text="Humidity", font=("FiraCode Nerd Font", 23), text_color="#6b7280")
    humidity_label.grid(row=3, column=1, padx=10, pady=2, sticky="w")

    humidity_value=ctk.CTkLabel(conditions_frame, text="0.0%", font=("Arial", 22, "bold"))
    humidity_value.grid(row=4, column=1, padx=20, pady=10, sticky="w")

    