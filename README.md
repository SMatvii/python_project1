# Telegram Group Assistant #

**Telegram group assistant bot:**  
Reminders, user activity stats, and a simple frontend for management.

## Project Structure

```
python/
├── backend/
│   ├── bot.py
│   ├── api.py
│   ├── storage.py
│   └── config.py
├── frontend/
│   ├── static/
│   │   ├── style.css
│   │   └── main.js
│   └── templates/
│       └── index.html
├── requirements.txt
└── README.md
```

## Installation

1. **Python 3.9+ required**  
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Set your Telegram bot token in `backend/config.py`:
    ```python
    TELEGRAM_BOT_TOKEN = "YOUR_TOKEN_HERE"
    ```

4. (Optional) Change `ADMIN_PASSWORD` for frontend/API access.

## Running the Project

### 1. Start the backend:
- **Bot:**  
    ```
    cd backend
    python bot.py
    ```
- **API (Flask):**  
    ```
    cd backend
    python api.py
    ```.

### 2. Start the frontend:
- Simply run the Flask server and open `frontend/templates/index.html` in your browser.
- By default, the site will be available at http://localhost:8000

## Features

- Add reminders to any group
- View user activity statistics
- Simple and easy to deploy

## Security

- API uses a simple bearer token password (see `ADMIN_PASSWORD` in config).
- Do not use this password in production without further protection!

---
