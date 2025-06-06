from tkinter.messagebox import showinfo
from tkinter import simpledialog, Canvas
from PIL import Image, ImageTk
import customtkinter as ctk
import pygame

# Globaalid
pildid = {}
objektid = {}
olemas = {}

# Pildifailid
silmad_pildid = ["silmad1.png", "silmad2.png", "silmad3.png", "silmad4.png", "silmad5.png"]
nina_pildid = ["nina1.png", "nina2.png", "nina3.png", "nina4.png"]
suu_pildid = ["suu1.png", "suu2.png", "suu3.png", "suu4.png", "suu5.png", "suu6.png"]

silmad_index = [0]
nina_index = [0]
suu_index = [0]

# Funktsioonid
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

def uuenda_osa(nimi, pildid_list, index_list):
    index_list[0] = (index_list[0] + 1) % len(pildid_list)
    fail = pildid_list[index_list[0]]
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
    pil_img = Image.open(fail).convert("RGBA").resize((400, 400))
    tk_img = ImageTk.PhotoImage(pil_img)
    pildid[nimi] = tk_img
    objektid[nimi] = canvas.create_image(200, 200, image=tk_img)
    olemas[nimi] = True

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
        "silmad": silmad_pildid[silmad_index[0]],
        "nina": nina_pildid[nina_index[0]],
        "suu": suu_pildid[suu_index[0]],
    }

    for nimi, failitee in kihid.items():
        if olemas.get(nimi) and failitee:
            osa = Image.open(failitee).convert("RGBA").resize((400, 400))
            lõpp_pilt.alpha_composite(osa)

    lõpp_pilt.save(f"{failinimi}.png")
    showinfo("Pilt salvestatud", f"Faili nimi on {failinimi}.png")


def kustuta_koik():
    for nimi in list(olemas.keys()):
        if nimi != "nägu" and olemas[nimi]:
            canvas.delete(objektid[nimi])
            olemas[nimi] = False


# Pygame algus
pygame.mixer.init()
pygame.mixer.music.load("Betsy, Ely Oaks & Levinia - Sigma Boy (Lyrics) [Letra].mp3")

# Rakendus
app = ctk.CTk()
app.geometry("800x500")
app.title("Näo koostaja")

canvas = Canvas(app, width=400, height=400, bg="white")
canvas.pack(side="right", padx=10, pady=10)

# Alusta piltidega
toggle_osa("nägu", "alus.png", 200, 200)
olemas["nägu"] = True

toggle_osa("silmad", silmad_pildid[0], 200, 190)
olemas["silmad"] = True

toggle_osa("nina", nina_pildid[0], 200, 185)
olemas["nina"] = True

toggle_osa("suu", suu_pildid[0], 200, 215)
olemas["suu"] = True

# Vasak paneel
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
ctk.CTkButton(frame, text="Silmad", command=lambda: uuenda_osa("silmad", silmad_pildid, silmad_index), **nuppu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Nina", command=lambda: uuenda_osa("nina", nina_pildid, nina_index), **nuppu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Suu", command=lambda: uuenda_osa("suu", suu_pildid, suu_index), **nuppu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Kustuta kõik", command=kustuta_koik, **nuppu_seaded).pack(pady=10)

ctk.CTkButton(frame, text="Salvesta nägu", command=salvesta_nägu, **nuppu_seaded).pack(pady=10)

# Muusika nupud
frame_mus = ctk.CTkFrame(frame)
frame_mus.pack(padx=10, pady=10)

ctk.CTkButton(frame_mus, text="Mängi muusikat", fg_color="#4CAF50", command=mängi_muusika).pack(side="left", pady=10)
ctk.CTkButton(frame_mus, text="Peata muusika", fg_color="#4CAF50", command=peata_muusika).pack(side="left", pady=10)

# Käivita
app.mainloop()
