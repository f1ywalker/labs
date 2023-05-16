def z1():
    import os
    from PIL import Image
    input_folder = "images/"

    output_folder = "output_images/"
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            path = os.path.join(input_folder, file_name)
            image = Image.open(path)
            gray_image = image.convert('L')

            output_path = os.path.join(output_folder, "gray_" + file_name)
            gray_image.save(output_path)
def z2():
    import csv
    with open('new.csv', 'r', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        total = 0
        output = "Нужно купить:\n"

        for row in reader:
            product = row[0]
            count = int(row[1])
            price = int(row[2])
            output += f"{product} - {count} шт. за {price} руб.\n"
            total += count * price
        output += f"Итоговая сумма: {total} руб."
        print(output)
z1(),z2()
