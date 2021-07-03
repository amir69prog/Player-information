from tkinter import *
from datetime import datetime
from PIL import ImageTk, Image
import requests
from tkinter import messagebox

# ========= functions ==========
def search_player():
	page = requests.get("https://www.easports.com/fifa/ultimate-team/api/fut/item").json()
	players = page['items']
	name = name_input.get()
	exists = 0
	if name is None or len(name) < 2:
		messagebox.showerror("Info Player","please enter your player soccer name")
	else:
		for player in players:
			if name.title() in player['commonName'] or name.title() in player['firstName'] or name.title() in player['lastName']:
				ent_team = Entry(root,border=2,bg="lightgray",width=10,borderwidth=2,font=("Scooby Doo",10))
				ent_team.place(x=80,y=150)
				ent_team.insert(END,player["club"]["name"])

				ent_natinal = Entry(root,border=2,bg="lightgray",width=10,borderwidth=2,font=("Scooby Doo",10))
				ent_natinal.place(x=80,y=230)
				ent_natinal.insert(END,player["nation"]["name"])

				ent_age = Entry(root,border=2,bg="lightgray",width=10,borderwidth=2,font=("Scooby Doo",10))
				ent_age.place(x=80,y=310)
				ent_age.insert(END,player['age'])

				ent_foot = Entry(root,border=2,bg="lightgray",width=10,borderwidth=2,font=("Scooby Doo",10))
				ent_foot.place(x=80,y=390)
				ent_foot.insert(END,player['foot'])

				ent_dribling = Entry(root,border=2,bg="lightgray",width=10,borderwidth=2,font=("Scooby Doo",10))
				ent_dribling.place(x=370,y=150)
				ent_dribling.insert(END,player['dribbling'])

				ent_jumping = Entry(root,border=2,bg="lightgray",width=10,borderwidth=2,font=("Scooby Doo",10))
				ent_jumping.place(x=370,y=230)
				ent_jumping.insert(END,player['jumping'])

				ent_sprintspeed = Entry(root,border=2,bg="lightgray",width=10,borderwidth=2,font=("Scooby Doo",10))
				ent_sprintspeed.place(x=370,y=310)
				ent_sprintspeed.insert(END,player['sprintspeed'])

				ent_longshots = Entry(root,border=2,bg="lightgray",width=10,borderwidth=2,font=("Scooby Doo",10))
				ent_longshots.place(x=370,y=390)
				ent_longshots.insert(END,player['longshots'])


				exists = 1
			else:
				continue
		if not exists:
			messagebox.showwarning("Info Player","name is not found\nsearch another player")


# ========== Initial ==========
root = Tk()
root.title("Player")
root.geometry("600x450")
root.resizable(False,False)
root.iconbitmap("images/football.ico")
root.config(bg="green")


# =========== label title ==========
label_title = Label(root,text="Info Player",font=("Dirty Headline",30,"bold"),bg="green")
label_title.place(x=10,y=10)

# =========== label date ===========
label_date = Label(root,text=datetime.now().date(),font=("Scooby Doo",12),bg="green",fg="white")
label_date.place(x=500,y=15)


# =========== search part ===========
label_desc = Label(root,text="please enter your player soccer name",font=("Scooby Doo",15),bg="green")
label_desc.place(x=10,y=80)

name_input = Entry(root,border=2,bg="lightgray",width=30,borderwidth=5,font=("Scooby Doo",10))
name_input.place(x=10,y=110)

search_button = Button(root,text="Search",width=10,bg="lightgray",border=1,borderwidth=3,
	font=("Scooby Doo",10,"bold"),command=search_player)
search_button.place(x=300,y=110)


# ============ attrs ============
img_team = ImageTk.PhotoImage(Image.open("images/football-club.png"))
team_image = Label(root,image=img_team,bg="green")
team_image.place(x=10,y=140)


img_national = ImageTk.PhotoImage(Image.open("images/germany.png"))
national_image = Label(root,image=img_national,bg="green")
national_image.place(x=10,y=220)


img_age = ImageTk.PhotoImage(Image.open("images/age.png"))
age_image = Label(root,image=img_age,bg="green")
age_image.place(x=10,y=300)


img_foot = ImageTk.PhotoImage(Image.open("images/footwear.png"))
foot_image = Label(root,image=img_foot,bg="green")
foot_image.place(x=10,y=380)


img_dribling = ImageTk.PhotoImage(Image.open("images/dribble.png"))
dribling_image = Label(root,image=img_dribling,bg="green")
dribling_image.place(x=300,y=140)


img_jumping = ImageTk.PhotoImage(Image.open("images/man-jumping-up.png"))
jumping_image = Label(root,image=img_jumping,bg="green")
jumping_image.place(x=300,y=220)


img_sprintspeed = ImageTk.PhotoImage(Image.open("images/speed.png"))
sprintspeed_image = Label(root,image=img_sprintspeed,bg="green")
sprintspeed_image.place(x=300,y=300)


img_longshots = ImageTk.PhotoImage(Image.open("images/football.png"))
longshots_image = Label(root,image=img_longshots,bg="green")
longshots_image.place(x=300,y=380)


# ========= Run ============
root.mainloop()
