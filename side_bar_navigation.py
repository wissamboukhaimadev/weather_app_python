from PIL import Image
import customtkinter as ctk

weather_icon=Image.open("./icons/cloudy.png")
burger_icon=Image.open("./icons/burger-bar.png")
search_icon=Image.open("./icons/search.png")
history_icon=Image.open("./icons/bar-chart.png")

labels=["Weather","Chart"]

icons={
    "Weather":weather_icon,
    "Chart": history_icon,
    
}

def on_enter(event):
    event.widget.configure(cursor="hand2")   

def on_leave(event):
    event.widget.configure(cursor="")  

def handle_navigation(event,label, main_content, history_frame):
    if label=="Weather":
        main_content.grid(row=0, column=3, sticky="nsew")
        history_frame.grid_forget() 

    elif label=="Chart":
        main_content.grid_forget() 
        history_frame.grid(row=0, column=3, sticky="nsew")

def show_navigation(side_bar, main_content, history_frame):
    for i, label_text in enumerate(labels):
        side_bar_navigation=ctk.CTkFrame(side_bar,fg_color="transparent")
        side_bar_navigation.grid(row=i,column=1,pady=20)

        side_bar_navigation.bind("<Button-1>",  lambda event, label=label_text: handle_navigation(event, label, main_content, history_frame))


        side_bar_navigation.bind("<Enter>", on_enter)
        side_bar_navigation.bind("<Leave>", on_leave)

        my_image = ctk.CTkImage(light_image=icons[label_text], dark_image=icons[label_text], size=(30, 30))
        image_label = ctk.CTkLabel(side_bar_navigation, image=my_image, text="")  # display image with a CTkLabel


        image_label.grid(row=0, column=1, pady=5, padx=20)

        text_label=ctk.CTkLabel(side_bar_navigation,text=label_text)
        text_label.grid(row=1, column=1, pady=5, padx=20)