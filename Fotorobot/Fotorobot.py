from tkinter.messagebox import showinfo
from tkinter import simpledialog, Canvas
from PIL import Image, ImageTk
import customtkinter as ctk
import pygame

pildid = {}
objektid = {}
olemas = {}

silmad_pildid = ["silmad1.png", "silmad2.png", "silmad3.png", "silmad4.png", "silmad5.png"]
nina_pildid = ["nina1.png", "nina2.png", "nina3.png", "nina4.png"]
suu_pildid = ["suu1.png", "suu2.png", "suu3.png"]

silmad_index = [0]
nina_index = [0]
suu_index = [0]

def toggle_osa(nimi, fail, x, y):
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi] = False
    else:
        pil_img = Image.open(fail).convert("RGBA").resize((400, 400))
        tk_img = ImageTk.PhotoImage(pil_img)
        pildid[nimi] = tk_img
        objektid[nimi] = canvas.create_image(x, y, image=tk_img)
        olemas[nimi] = True

def toggle_silmad():
    nimi = "silmad"
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi] = False
    fail = silmad_pildid[silmad_index[0]]
    pil_img = Image.open(fail).convert("RGBA").resize((400, 400))
    tk_img = ImageTk.PhotoImage(pil_img)
    pildid[nimi] = tk_img
    objektid[nimi] = canvas.create_image(200, 200, image=tk_img)
    olemas[nimi] = True
    silmad_index[0] = (silmad_index[0] + 1) % len(silmad_pildid)

def toggle_nina():
    nimi = "nina"
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi] = False
    fail = nina_pildid[nina_index[0]]
    pil_img = Image.open(fail).convert("RGBA").resize((400, 400))
    tk_img = ImageTk.PhotoImage(pil_img)
    pildid[nimi] = tk_img
    objektid[nimi] = canvas.create_image(200, 200, image=tk_img)
    olemas[nimi] = True
    nina_index[0] = (nina_index[0] + 1) % len(nina_pildid)

def toggle_suu():
    nimi = "suu"
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi] = False
    fail = suu_pildid[suu_index[0]]
    pil_img = Image.open(fail).convert("RGBA").resize((400, 400))
    tk_img = ImageTk.PhotoImage(pil_img)
    pildid[nimi] = tk_img
    objektid[nimi] = canvas.create_image(200, 200, image=tk_img)
    olemas[nimi] = True
    suu_index[0] = (suu_index[0] + 1) % len(suu_pildid)

def mängi_muusika():
    pygame.mixer.music.play(loops=-1)

def peata_muusika():
    pygame.mixer.music.stop()

def salvesta_nägu():
    failinimi = simpledialog.askstring("Salvesta pilt", "Sisesta faili nimi (ilma laiendita):")
    if not failinimi:
        return

    lõpp_pilt = Image.new("RGBA", (400, 400), (255, 255, 255, 255))
    kihid = {
        "nägu": "alus.png",
        "silmad": silmad_pildid[(silmad_index[0] - 1) % len(silmad_pildid)],
        "nina": nina_pildid[(nina_index[0] - 1) % len(nina_pildid)],
        "suu": suu_pildid[(suu_index[0] - 1) % len(suu_pildid)],
    }

    for nimi, failitee in kihid.items():
        if olemas.get(nimi) and failitee:
            osa = Image.open(failitee).convert("RGBA").resize((400, 400))
            lõpp_pilt.alpha_composite(osa)

    lõpp_pilt.save(f"{failinimi}.png")
    showinfo("Pilt salvestatud", f"Faili nimi on {failinimi}.png")

# GUI setup
pygame.mixer.init()
pygame.mixer.music.load("Betsy, Ely Oaks & Levinia - Sigma Boy (Lyrics) [Letra].mp3")

app = ctk.CTk()
app.geometry("800x500")
app.title("Näo koostaja")

canvas = Canvas(app, width=400, height=400, bg="white")
canvas.pack(side="right", padx=10, pady=10)

toggle_osa("nägu", "alus.png", 200, 200)
olemas["nägu"] = True

frame = ctk.CTkFrame(app)
frame.pack(side="left", padx=10, pady=10)

nuppu_seaded = {
    "width": 150, "height": 40,
    "font": ("Segoe UI Emoji", 20),
    "fg_color": "#4CAF50",
    "text_color": "white",
    "corner_radius": 20
}

ctk.CTkLabel(frame, text="Vali näoosad:", **nuppu_seaded).pack(pady=5)
ctk.CTkButton(frame, text="Silmad", command=toggle_silmad, **nuppu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Nina", command=toggle_nina, **nuppu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Suu", command=toggle_suu, **nuppu_seaded).pack(pady=3)

ctk.CTkButton(frame, text="Salvesta nägu", command=salvesta_nägu, **nuppu_seaded).pack(pady=10)

frame_mus = ctk.CTkFrame(frame)
frame_mus.pack(padx=10, pady=10)

ctk.CTkButton(frame_mus, text="Mängi muusikat", fg_color="#4CAF50", command=mängi_muusika).pack(side="left", pady=10)
ctk.CTkButton(frame_mus, text="Peata muusika", fg_color="#4CAF50", command=peata_muusika).pack(side="left", pady=10)

app.mainloop()