#!/usr/bin/env python3
"""Hello, World — but make it a spectacle.

Matrix rain decodes into a hand-rolled block-letter banner, which then
shimmers through a rainbow gradient. Zero dependencies. Ctrl+C to bow out.
"""
import math
import random
import shutil
import sys
import time

FONT = {
    "H": ["█   █", "█   █", "█████", "█   █", "█   █"],
    "E": ["█████", "█    ", "████ ", "█    ", "█████"],
    "L": ["█    ", "█    ", "█    ", "█    ", "█████"],
    "O": [" ███ ", "█   █", "█   █", "█   █", " ███ "],
    "W": ["█   █", "█   █", "█ █ █", "██ ██", "█   █"],
    "R": ["████ ", "█   █", "████ ", "█  █ ", "█   █"],
    "D": ["████ ", "█   █", "█   █", "█   █", "████ "],
    ",": ["     ", "     ", "     ", "  ██ ", " ██  "],
    "!": ["  █  ", "  █  ", "  █  ", "     ", "  █  "],
    " ": ["   ", "   ", "   ", "   ", "   "],
}
GLYPHS = "ｱｲｳｴｵｶｷｸｹｺ0123456789@#$%&*+=<>"


def banner(text):
    return ["  ".join(FONT[c][row] for c in text) for row in range(5)]


def rgb(r, g, b):
    return f"\x1b[38;2;{r};{g};{b}m"


def rainbow(x, t):
    return rgb(*(int(127 + 127 * math.sin(0.15 * x + t + p)) for p in (0, 2.09, 4.19)))


def main():
    art = banner("HELLO, WORLD!")
    cols, rows = shutil.get_terminal_size((100, 24))
    width = len(art[0])
    if width > cols:
        art, width = banner("HI!"), len(banner("HI!")[0])
    top, left = max(0, (rows - 5) // 2), max(0, (cols - width) // 2)
    out = sys.stdout.write
    out("\x1b[?25l\x1b[2J")
    try:
        # Act I: the decode — each cell locks in at a random moment.
        lock = [[random.uniform(0.2, 1.8) for _ in row] for row in art]
        start = time.time()
        while (elapsed := time.time() - start) < 2.0:
            frame = []
            for y, row in enumerate(art):
                frame.append(f"\x1b[{top + y + 1};{left + 1}H")
                for x, ch in enumerate(row):
                    if elapsed >= lock[y][x]:
                        frame.append(rgb(255, 255, 255) + ch)
                    else:
                        frame.append(rgb(0, random.randint(120, 255), 70) + random.choice(GLYPHS))
            out("".join(frame))
            sys.stdout.flush()
            time.sleep(0.03)
        # Act II: the shimmer.
        t = 0.0
        while t < 6.0 or "--forever" in sys.argv:
            frame = []
            for y, row in enumerate(art):
                frame.append(f"\x1b[{top + y + 1};{left + 1}H")
                frame.extend(rainbow(x + y * 2, t) + ch for x, ch in enumerate(row))
            out("".join(frame))
            sys.stdout.flush()
            t += 0.12
            time.sleep(0.03)
    except KeyboardInterrupt:
        pass
    finally:
        out(f"\x1b[0m\x1b[?25h\x1b[{top + 7};1H")
        print(" " * max(0, (cols - 13) // 2) + "Hello, World!")


if __name__ == "__main__":
    main()
