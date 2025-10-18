import json
import tempfile
import subprocess
from pathlib import Path

DATA_PATH = Path("data/cards.json")


# ───────────────────────────────────────────────
# 🔹 Entrada multilínea desde el editor (nano)
# ───────────────────────────────────────────────
def input_editor(prompt):
    """Abre el editor de texto (nano) para ingresar contenido."""
    print(f"\n📝 {prompt}")
    print("   (Se abrirá el editor nano. Escribe tu texto, guarda con Ctrl+O, cierra con Ctrl+X.)")

    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False, mode="w+", encoding="utf-8") as tmp:
        tmp_path = Path(tmp.name)
        subprocess.call(["nano", str(tmp_path)])  # Abre el editor
        tmp.seek(0)
        content = tmp.read().strip()

    if not content:
        print("⚠️ No se ingresó contenido. Puedes intentarlo de nuevo si fue un error.")
    return content


# ───────────────────────────────────────────────
# 🔹 Cargar y guardar tarjetas
# ───────────────────────────────────────────────
def load_cards():
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_cards(cards):
    DATA_PATH.parent.mkdir(exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(cards, f, indent=4, ensure_ascii=False)


# ───────────────────────────────────────────────
# 🔹 Generar ID incremental
# ───────────────────────────────────────────────
def generate_id(cards):
    if not cards:
        return 1
    return max(card["id"] for card in cards) + 1


# ───────────────────────────────────────────────
# 🔹 Agregar tarjeta con editor y soporte de imagen
# ───────────────────────────────────────────────
def add_card(pregunta=None, respuesta=None, imagen=None):
    cards = load_cards()

    if not pregunta:
        pregunta = input_editor("Escribe la **pregunta** de la tarjeta:")

    if not respuesta:
        respuesta = input_editor("Escribe la **respuesta** de la tarjeta:")

    if not imagen:
        ruta_img = input("🖼️ (Opcional) Escribe la ruta de la imagen o deja vacío: ").strip()
        if ruta_img:
            ruta = Path(ruta_img)
            if ruta.exists():
                imagen = str(ruta.resolve())
                print("✅ Imagen agregada correctamente.")
            else:
                print("⚠️ No se encontró la ruta de la imagen, se omitirá.")
                imagen = None

    nueva = {
        "id": generate_id(cards),
        "pregunta": pregunta.strip(),
        "respuesta": respuesta.strip(),
        "imagen": imagen.strip() if imagen else None,
        "nivel_memoria": 0,
        "ultima_revision": None
    }

    cards.append(nueva)
    save_cards(cards)
    print(f"\n✅ Tarjeta #{nueva['id']} creada correctamente.")


# ───────────────────────────────────────────────
# 🔹 Listar, eliminar y buscar tarjetas
# ───────────────────────────────────────────────
def list_cards():
    cards = load_cards()
    if not cards:
        print("⚠️ No hay tarjetas registradas aún.")
        return
    for card in cards:
        print(f"\n🆔 {card['id']}")
        print(f"❓ Pregunta:\n{card['pregunta']}")
        print(f"💬 Respuesta:\n{card['respuesta']}")
        if card["imagen"]:
            print(f"🖼️ Imagen: {card['imagen']}")


def delete_card(card_id):
    cards = load_cards()
    updated = [c for c in cards if c["id"] != card_id]
    if len(updated) == len(cards):
        print("⚠️ No se encontró una tarjeta con ese ID.")
        return
    save_cards(updated)
    print(f"🗑️ Tarjeta #{card_id} eliminada correctamente.")


def search_card(keyword):
    cards = load_cards()
    results = [
        c for c in cards if keyword.lower() in c["pregunta"].lower()
        or keyword.lower() in c["respuesta"].lower()
    ]
    if not results:
        print("🔍 No se encontraron coincidencias.")
        return
    for card in results:
        print(f"\n🆔 {card['id']} — {card['pregunta']}")
