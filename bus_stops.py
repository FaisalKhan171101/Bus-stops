import tkinter

characters = 20
i = text_element = 0
x, y = characters * 10, 50

canvas = tkinter.Canvas(bg="#282c34", width=characters * 20, height=100)
canvas.pack()

f = open("zastavky.txt", "r", encoding="Windows-1250")
lines = f.readlines()

canvas.create_text(x, y, text="░" * characters, fill="#185566", font=("JetBrains Mono", 30))


def draw():
    global line, text_element, text_pos

    if text_pos < 0:
        if characters + text_pos > len(line):
            text = line.ljust(characters + text_pos).rjust(characters)
        else:
            text = line[0:characters + text_pos].rjust(characters)
    else:
        text = line[text_pos:text_pos + characters].ljust(characters)

    canvas.delete(text_element)
    text_element = canvas.create_text(x, y, text=text, fill="#32b1d3", font=("JetBrains Mono", 30))

    if text_pos > len(line) - 2:
        text_pos = -1 * characters

    text_pos += 1


def keypress(_):
    global lines, line, i, text_pos

    line = lines[i].strip()
    text_pos = -1 * characters + 1

    if (line == lines[-1].strip()):
        line += " | KONEČNÁ ZASTÁVKA"
    else:
        i += 1


canvas.bind_all("<Key>", keypress)
keypress(None)

while True:
    draw()
    canvas.after(200)
    canvas.update()