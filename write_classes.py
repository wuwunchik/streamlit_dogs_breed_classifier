import os

classes = sorted(os.listdir('./dataset'))  # Путь к папке с изображениями пород
with open("class_names.txt", "w") as f:
    for cls in classes:
        f.write(cls + "\n")

