from tkinter.messagebox import showinfo
import customtkinter as ctk
from tkinter import simmoledialog, Canvas
from PIL import image, ImageTk
import pygame
pildid={}
objektid={}
olemas={}
silmad_pildid = ["silmad1.png", "silmad2.png", "silmad3.png", "silmad4.png", "silmad5.png"]
nina_pildid=["nina1.png","nina2.png", "nina3.png", "nina4.png"]

def toggle_osa(nimi, fail, x, y):
    if olemas. get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi] = False
    else:
        pil_img = image. open(fail). convert ("RGBA"). resize((400, 400))
        tk_img = ImageTk. PhotoImage(pil_img)
        pildid[nimi] = tk_img
        objektid[nimi] = canvas. create_image(x, y, image=tk_img)
        olemas[nimi] = True

def toggle_silmad():
    nimi = "silmad"
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi] = False

    fail = silmad_pildid[silmad_index[0]]
    pil_img = image.open(fail).convert("RGBA").resize((400, 400))
    tk_img = ImageTk.PhotoImage(pil_img)
    pildid[nimi] = tk_img
    objektid[nimi] = canvas.create_image(200, 200, image=tk_img)
    olemas[nimi] = True
    silmad_index[0] = (silmad_index[0] + 1) % len(silmad_pildid)


def mängi_muusika():
    pygame.mixer.music.play(loops=-1)

def peata_muusika():
    pygame.mixer.music.stop(loops=-1)


pygame.mixer.init()
pygame.mixer.music.load("Betsy, Ely Oaks & Levinia - Sigma Boy (Lyrics) [Letra].mp3")
app=ctk.CTk()
app.geometry("800x500")
app.title("nao koostaja")
canvas = Canvas(app, width=400, height=400,bg="white")
canvas.pack(side="right", padx=10, pady=10)



def salvesta_nägu():
    failinimi = simmoledialog.askstring("Salvesta pilt", "Sisesta faili nimi (ilma laiendita):")
    if not failinimi:
        return

lõpp_pilt = image.new("RGBA", (400, 400), (255, 255, 255, 255))


for nimi in ["nägu","otsmik","silmad", "nina", "suu"]:
    if olemas. get (nimi) :
        failitee = {
            "nägu": "alus.png",
            "silmad": silmad_pildid[silmad_index[0]],
            "nina": "",
            "suu": ""
            } .get(nimi)
        if failitee:
            osa = image.open(failitee). convert ("RGBA"). resize((400, 400))
            lõpp_pilt.alpha_composite(osa)

lõpp_pilt.save(f"{failinimi}.png")
showinfo(f"pilt salvestatud:" f"faili nimi on {failinimi} .png")

toggle_osa("nägu", "alus.png", 200, 200)
olemas["nägu"] = True

frame =ctk.CTkFrame(app)
frame.pack(side="left", padx=10, pady=10)
nuppu_seaded={ 
    "width": 150, "height": 40,
    "font": ("Segoe UI Emoji", 32),
    "fg_color": "#4CAF50",
    "text_color": "white",
    "corner radius": 20 
    }

ctk.CTkLabel(frame, text="Vali näoosad:", **nuppu_seaded). pack(pady=5)
ctk.CkButton(frame, text="Silmad", command=lambda: toggle_osa("silmad",command=toggle_silmad), **nuppu_seaded). pack(pady=3)
ctk.CTkButton(frame, text=" Nina", command=lambda: toggle_osa("nina", "nina.png", 200, 200), **nuppu_seaded) .pack(pady=3)
ctk.CTkButton(frame, text="Suu", command=lambda: toggle_osa("suu", "suu.png", 200, 200), **nuppu_seaded). pack(pady=3)
nupp = ctk.CTkButton(frame, text="Salvesta nägu", command=salvesta_nägu, **nuppu_seaded)
nupp.pack(pady=10)

frame_mus = ctk. CTkFrame(frame)
frame_mus. pack(padx=10, pady=10)
ctk.CTkButton(frame_mus, text="Mängi muusikat", fg_color="#4CAF50",
command=mängi_muusika).pack(side="left", pady=10)
ctk.CTkButton(frame_mus, text="Peata muusika",
fg_color="#4CAF50", command=peata_muusika).pack(side="Left", pady=10)


app.mainloop()