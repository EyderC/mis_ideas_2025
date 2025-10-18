
from flashcard_manager import add_card, list_cards, delete_card, search_card

while True:
    print("\n=== GESTOR DE FLASHCARDS ===")
    print("1. Crear nueva tarjeta")
    print("2. Listar tarjetas")
    print("3. Buscar tarjeta")
    print("4. Eliminar tarjeta")
    print("5. Salir")
    op = input("Opción: ")

    if op == "1":
        add_card()
        
    elif op == "2":
        list_cards()
    elif op == "3":
        key = input("Palabra clave: ")
        search_card(key)
    elif op == "4":
        id_card = int(input("ID de la tarjeta a eliminar: "))
        delete_card(id_card)
    elif op == "5":
        break
