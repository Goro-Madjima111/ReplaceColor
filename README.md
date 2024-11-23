# ReplaceColor

Этот проект предоставляет функционал для обработки PNG-изображений, включая:
1. Применение заливки выбранным цветом.
2. Наложение градиента на иконки.

## Требования

Перед использованием необходимо установить следующий зависимость:

- **Pillow**: Библиотека для работы с изображениями в Python. Установите её, выполнив следующую команду:

```bash
pip install pillow
```

## Использование

### 1. Заливка изображений цветом

Этот функционал позволяет перекрасить все видимые пиксели PNG-изображений в выбранный цвет.

1. Поместите PNG-файлы в отдельную папку.
2. Запустите скрипт и выберите режим "1" (Заливка).
3. Введите путь к папке с изображениями.
4. Выберите один из доступных цветов:
   - Синий
   - Белый
   - Черный
   - Желтый
   - Оранжевый
   - Красный
5. Обработанные изображения будут сохранены в папке `output_images` внутри указанной директории.

### 2. Применение градиента к иконкам

Этот функционал добавляет градиентный эффект к PNG-иконкам.

1. Поместите PNG-файлы в отдельную папку.
2. Запустите скрипт и выберите режим "2" (Градиент).
3. Введите путь к папке с изображениями.
4. Обработанные иконки будут сохранены в папке `output_icons` внутри указанной директории.

### Запуск скрипта

1. Скачайте и поместите скрипт `image_processing.py` в любую папку на вашем компьютере.
2. Запустите скрипт, выполнив следующую команду:

```bash
python image_processing.py
```

3. Следуйте инструкциям, выводимым в консоль.

## Пример кода

```python
python image_processing.py
```

- Введите `1` для заливки изображений цветом.
- Введите `2` для применения градиента к иконкам.

## Примечания

- Скрипт поддерживает только PNG-изображения.

