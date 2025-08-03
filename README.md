# 🌌 Space Photos Telegram Bot

## 📖 Описание проекта

Этот проект представляет собой автоматизированную систему для:

- 📥 Сбора космических фотографий из различных API:
    - NASA APOD (Astronomy Picture of the Day)
    - NASA EPIC (Earth Polychromatic Imaging Camera)
    - SpaceX
- 📤 Автоматической отправки фото в Telegram-канал с заданным интервалом

---

## ✨ Особенности

- Поддержка нескольких источников изображений
- Автоматическое удаление отправленных фото (для того чтобы не было повторений)
- Гибкая настройка интервала отправки
---

## ⚙️ Требования

- Python 3.8+
- API-ключ NASA
- Токен Telegram-бота

---

## 🚀 Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/W00lenW0lf/3_lesson_tg_channel.git
cd 3_lesson_tg_channel
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Создайте `.env` файл в корне проекта:

```env
NASA_API_KEY=ваш_ключ
TG_TOKEN=ваш_токен
NUMBER_SAVED_IMG=количество сохраняемых изображений с помощью NASA APOD
IMG_SENDING_DELAY=14400 задержка между отправкой изображений ботом в телеграм (14400 секунд это 4 часа)
```

---

## 🔑 Настройка API-ключей

- **NASA API**  
  Получите ключ на [api.nasa.gov](https://api.nasa.gov)  
  Добавьте его в `.env` как `API_KEY`

- **Telegram Bot**  
  Создайте бота через [@BotFather](https://t.me/BotFather)  
  Добавьте токен в `.env` как `TG_TOKEN`

---

## ⏲️ Настройка интервала

Измените переменную `IMG_SENDING_DELAY` в `.env`:

| Значение | Интервал |
|----------|----------|
| `3600`   | 1 час    |
| `14400`  | 4 часа   |
| `86400`  | 1 день   |

---

## ▶️ ЗапусК

Сначала загрузите изображения с помощью скриптов:

```bash
python download_image_nasa_apod.py
python download_image_nasa_epic.py
python download_image_spacex.py
```

Затем запустите Telegram-бота который будет отправлять фотографии в канал или группу в которой он находится:

```bash
python send_images_bot.py
```

---

## 📝 Примечания

Перед первым запуском убедитесь, что:

- Все API-ключи корректны
- Бот добавлен в Telegram-канал как администратор
- Папка `images/` существует и доступна для записи