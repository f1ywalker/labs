def z1():
    from PIL import Image

    filename = "3.jpg"
    with Image.open(filename) as img:
        img.load()

    img.show()
    width, height = img.size

    format = img.format

    mode = img.mode

    print("Ширина: ", width)
    print("Высота:  ", height)
    print("Формат: ", format)
    print("Цветовая модель:", mode)

def z2():
    from PIL import Image

    image1 = "4.jpg"
    with Image.open(image1) as img:
        img.load()
        new_img = img.resize((img.width // 3, img.height // 3))
        new_img.save("4_new.jpg")
        flipped1 = img.transpose(method=Image.FLIP_TOP_BOTTOM)
        flipped1.save("4.1_flipped.jpg")
    image2 = "4_new.jpg"
    with Image.open(image2) as img:
        img.load()
        flipped2=img.transpose(method=Image.FLIP_LEFT_RIGHT)
        flipped2.save("4.2_flipped.jpg")

def z3():
    from PIL import Image
    photos_list = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for photo_name in photos_list:
        image = Image.open(photo_name)
        gray_image = image.convert('L')
        gray_image.save("gray_" + photo_name)


z1(),z2(),z3()