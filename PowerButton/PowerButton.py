from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 10") 
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

st= Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="steelblue")

r_button= Button(st, text='Restart', font=("Time New Roman", 10, "bold"), relief=RAISED, cursor="arrow", command=restart)
r_button.place(x=150,y=60, height=50, width=200,)

rt_button= Button(st, text='Restart Time', font=("Time New Roman", 10, "bold"), relief=RAISED, command=restart_time)
rt_button.place(x=150,y=160, height=50, width=200,)

lg_button= Button(st, text='Log-Out', font=("Time New Roman", 10, "bold"), relief=RAISED, command=logout)
lg_button.place(x=150,y=260, height=50, width=200,)

st_button= Button(st, text='ShutDown', font=("Time New Roman", 10, "bold"), relief=RAISED, command=shutdown)
st_button.place(x=150,y=360, height=50, width=200,)

st.mainloop()