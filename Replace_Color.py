import os
from PIL import Image, ImageDraw

def apply_color_to_images(folder_path):
    # Список цветов и их названий
    colors = [
        (16, 24, 63),    # синий
        (255, 255, 255), # белый
        (0, 0, 0),       # черный
        (251, 184, 0),   # желтый
        (243, 112, 24),  # оранжевый
        (192, 0, 0)      # красный
    ]

    color_names = [
        "Синий",
        "Белый",
        "Черный",
        "Желтый",
        "Оранжевый",
        "Красный"
    ]

    print("Выберите цвет:")
    for i, color_name in enumerate(color_names):
        print(f"{i + 1}. {color_name}")

    selected_color_index = int(input("Введите номер цвета: ")) - 1

    if not os.path.exists(folder_path):
        print("Указанный путь не существует.")
    else:
        output_folder = os.path.join(folder_path, "output_images")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        files = os.listdir(folder_path)

        png_files = [f for f in files if f.lower().endswith('.png')]

        if png_files:
            print("Найдены следующие PNG-файлы:")
            for png_file in png_files:
                print(png_file)

                image_file = os.path.join(folder_path, png_file)

                img = Image.open(image_file).convert('RGBA')

                pixdata = img.load()

                color_rgb = colors[selected_color_index]

                for y in range(img.size[1]):
                    for x in range(img.size[0]):
                        alpha = pixdata[x, y][3]
                        if alpha:
                            pixdata[x, y] = (*color_rgb, alpha)

                output_file = os.path.join(output_folder, png_file)

                img.save(output_file)
                print(f"Изображение {png_file} успешно обработано и сохранено как {output_file}")
        else:
            print("В указанной папке не найдено PNG-файлов.")

def apply_gradient_to_icons(folder_path):
    def apply_gradient_to_icon(icon_path, output_folder):

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        icon = Image.open(icon_path).convert('RGBA')

        icon_alpha = icon.split()[3]

        gradient_layer = Image.new('RGBA', icon.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(gradient_layer)

        for x in range(icon.width):
            alpha = int(x / icon.width * 255)  
            draw.line([(x, 0), (x, icon.height)], fill=(0, 0, 0, alpha))
        
        result_icon = Image.alpha_composite(icon, gradient_layer)
        result_icon.putalpha(icon_alpha)

        output_file = os.path.join(output_folder, os.path.basename(icon_path))

        result_icon.save(output_file)

    if not os.path.exists(folder_path):
        print("Указанный путь не существует.")
    else:
        output_folder = os.path.join(folder_path, "output_icons")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        files = os.listdir(folder_path)
        png_files = [f for f in files if f.lower().endswith('.png')]

        if png_files:
            print("Найдены следующие PNG-файлы:")
            for png_file in png_files:
                print(png_file)

                icon_path = os.path.join(folder_path, png_file)

                apply_gradient_to_icon(icon_path, output_folder)

                print(f"Изображение {png_file} успешно обработана и сохранена в {output_folder}")
        else:
            print("В указанной папке не найдено PNG-файлов.")

choice = print("1.Заливка\n2.Градиент")
action = input("Выберите цифру: ")

if action == '1':
    folder_path = input("Введите путь к папке с PNG-файлами: ")
    apply_color_to_images(folder_path)
elif action == '2':
    folder_path = input("Введите путь к папке с PNG-файлами: ")
    apply_gradient_to_icons(folder_path)
else:
    print("Неверный ввод. Пожалуйста, введите '1' или '2'.")
