import customtkinter as ctk
from side_bar_navigation import show_navigation
from main_content_widgets import show_main_content
from history_page_interface import show_history_page


app=ctk.CTk(fg_color="#0b131e")
app.geometry("800x400")
app.title("Weather app")


app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)
app.grid_columnconfigure(2,weight=1)
app.grid_columnconfigure(3,weight=8)
app.grid_columnconfigure(4,weight=1)
app.grid_rowconfigure(0, weight=1)


side_bar=ctk.CTkFrame(app, fg_color="#202b3b", corner_radius=20)
side_bar.grid(row=0, column=1, sticky="nsew")

side_bar.grid_columnconfigure((0,2),weight=1)
side_bar.grid_columnconfigure(1,weight=0)


main_content=ctk.CTkFrame(app, fg_color="transparent", corner_radius=20)
main_content.grid(row=0, column=3, sticky="nsew")

main_content.grid_columnconfigure(0, weight=1)

history_frame = ctk.CTkScrollableFrame(app, fg_color="transparent", corner_radius=20)
history_frame._scrollbar.configure(width=1, fg_color=history_frame.cget("fg_color"))

history_frame.grid_columnconfigure(0,weight=1)

show_history_page(history_frame)
show_main_content(main_content)


show_navigation(side_bar, main_content, history_frame)
app.mainloop()