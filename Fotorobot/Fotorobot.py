from tkinter.messagebox import showinfo
from tkinter import simpledialog, Canvas
from PIL import Image, ImageTk
import customtkinter as ctk

pildid = {}
objektid = {}
olemas = {}

silmad_pildid = ["silmad1.png", "silmad2.png", "silmad3.png", "silmad4.png", "silmad5.png"]
nina_pildid = ["nina1.png", "nina2.png", "nina3.png", "nina4.png", "nina5.png"]
suu_pildid = ["suu1.png", "suu2.png", "suu3.png", "suu4.png", "suu5.png", "suu6.png"]

silmad_index = 0
nina_index = 0
suu_index = 0

#suurus
silmad_suurus = (300, 300)
nina_suurus = (270, 270)
suu_suurus = (270, 270)

#koordinaadid
silmad_pos = (200, 190)
nina_pos = (200, 200)
suu_pos = (200, 230)

def toggle_osa(nimi, failide_loend, suurus, pos_x, pos_y):
    global silmad_index, nina_index, suu_index
    if nimi == "silmad":
        silmad_index = (silmad_index + 1) % len(failide_loend)
        fail = failide_loend[silmad_index]
    elif nimi == "nina":
        nina_index = (nina_index + 1) % len(failide_loend)
        fail = failide_loend[nina_index]
    elif nimi == "suu":
        suu_index = (suu_index + 1) % len(failide_loend)
        fail = failide_loend[suu_index]

    pil_img = Image.open(fail).convert("RGBA").resize(suurus)
    tk_img = ImageTk.PhotoImage(pil_img)

    if olemas.get(nimi):
        canvas.delete(objektid[nimi])

    pildid[nimi] = tk_img
    objektid[nimi] = canvas.create_image(pos_x, pos_y, image=tk_img)
    olemas[nimi] = True

def salvesta_nägu():
    failinimi = simpledialog.askstring("Salvesta pilt", "Sisesta faili nimi (ilma laiendita):")
    if not failinimi:
        return

    lõpp_pilt = Image.new("RGBA", (400, 400), (255, 255, 255, 0))
    kihid = {
        "nägu": "alus.png",
        "silmad": silmad_pildid[silmad_index],
        "nina": nina_pildid[nina_index],
        "suu": suu_pildid[suu_index],
    }

    for nimi, failitee in kihid.items():
        if olemas.get(nimi) and failitee:
            if nimi == "silmad":
                osa = Image.open(failitee).convert("RGBA").resize(silmad_suurus)
            elif nimi == "nina":
                osa = Image.open(failitee).convert("RGBA").resize(nina_suurus)
            elif nimi == "suu":
                osa = Image.open(failitee).convert("RGBA").resize(suu_suurus)
            lõpp_pilt.alpha_composite(osa)

    lõpp_pilt.save(f"{failinimi}.png")
    showinfo("Pilt salvestatud", f"Faili nimi on {failinimi}.png")


app = ctk.CTk()
app.geometry("600x600")
app.title("Näo koostaja")

canvas = Canvas(app, width=400, height=400, bg="#d6a48b")
canvas.pack(side="right", padx=10, pady=10)


base_img = Image.open("alus.png").convert("RGBA").resize((400, 400))
base_tk_img = ImageTk.PhotoImage(base_img)
canvas.create_image(200, 200, image=base_tk_img)

# Hoidke aluspilti globaalsetes muutujates, et vältida selle kadumist
pildid["alus"] = base_tk_img

frame = ctk.CTkFrame(app)
frame.pack(side="left", padx=10, pady=10)

nuppu_seaded = {
    "width": 150, "height": 40,
    "font": ("Segoe UI Emoji", 20),
    "fg_color": "#4cafeb",
    "text_color": "white",
    "corner_radius": 20,
    "bg_color": "lightgrey"
    }

ctk.CTkLabel(frame, text="Vali näoosad:", **nuppu_seaded).pack(pady=5)

ctk.CTkButton(frame, text="Silmad", command=lambda: toggle_osa("silmad", silmad_pildid, silmad_suurus, silmad_pos[0], silmad_pos[1]), **nuppu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Nina", command=lambda: toggle_osa("nina", nina_pildid, nina_suurus, nina_pos[0], nina_pos[1]), **nuppu_seaded).pack(pady=3)
ctk.CTkButton(frame, text="Suu", command=lambda: toggle_osa("suu", suu_pildid, suu_suurus, suu_pos[0], suu_pos[1]), **nuppu_seaded).pack(pady=3)

ctk.CTkButton(frame, text="Salvesta nägu", command=salvesta_nägu, **nuppu_seaded).pack(pady=10)

app.mainloop()
