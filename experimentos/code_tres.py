import curses
import unicodedata

def char_width(ch: str) -> int:
    # Emojis y caracteres fullwidth suelen ser de 2 columnas
    return 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    y, x = 5, 5
    sprite = "🟫"
    w = char_width(sprite)

    while True:
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()

        # Limitar coordenadas (usando el ancho w del sprite)
        if y < 0: y = 0
        if y > max_y - 1: y = max_y - 1
        if x < 0: x = 0
        if x > max_x - w: x = max_x - w

        # Dibujar de forma segura (evita crash en bordes)
        try:
            stdscr.addstr(y, x, sprite)
        except curses.error:
            pass

        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP: y -= 1
        elif key == curses.KEY_DOWN: y += 1
        elif key == curses.KEY_LEFT: x -= 1
        elif key == curses.KEY_RIGHT: x += 1
        elif key == ord("q"): break

curses.wrapper(main)

