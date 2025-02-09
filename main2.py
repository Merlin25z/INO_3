from PIL import Image
import matplotlib.pyplot as plt

# Загружаем изображение
I = Image.open("i_i.jpg")  # Укажи путь к своему изображению

# Изменяем размер изображения до 500x300 пикселей
I_resized = I.resize((500, 300))

# Сохраняем изменённое изображение в формате JPEG
I_resized.save("resized_image.jpg", "JPEG")

# Конвертируем изображение в RGB и в градации серого
I_rgb = I.convert("RGB")
I_gray = I.convert("L")

# Отображаем оба изображения
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# RGB изображение
axes[0].imshow(I_rgb)
axes[0].set_title('RGB')
axes[0].axis('off')

# Grayscale изображение
axes[1].imshow(I_gray, cmap='gray')
axes[1].set_title('Grayscale')
axes[1].axis('off')

# Показываем график
plt.show()
