def z1():
    from PIL import Image
    image = Image.open("dr.jpg")
    width, height = image.size
    cropped = image.crop((0, 0, width, height - 250))
    cropped.save("cropped_dr.jpg")

def z2():
    from PIL import Image
    cards = {
        "День рождения": "dr.jpg",
        "23 февраля": "23f.jpg",
        "8 марта": "8m.jpg"
    }
    holiday = input("Введите название праздника: ")

    if holiday in cards:
        name = cards[holiday]
        print(f"Вот открытка для праздника '{holiday}'")
        with Image.open(name) as img:
            img.show()
    else:
        print(f"Нет открытки для праздника {holiday}.")

def z3():
    from PIL import Image, ImageDraw, ImageFont
    with Image.open("dr.jpg") as img:
        width, height = img.size
        draw = ImageDraw.Draw(img)
        name = input("Кого Вы хотите поздравить? ")
        font = ImageFont.truetype("arial_bold.ttf", size=50)
        color = (255, 0, 0)
        position = (width // 2, height - 700)
        text = f"{name}, поздравляю!"
        draw.text(position, text, font=font, fill=color, anchor="ms")
        img.save("edited_dr.png")

z1(),z2(),z3()
