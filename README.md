
---

```md
# 📝 Django To-Do List Application

A simple, clean, and professional **To-Do List web application** built using **Django**.  
This project demonstrates **CRUD operations**, task completion tracking, and secure handling of sensitive data using environment variables.

---

## 🚀 Features

- ➕ Add new tasks  
- 👀 View task details  
- ✏️ Edit existing tasks  
- 🗑️ Delete tasks with confirmation  
- ✅ Mark tasks as **Completed / Pending**  
- 🎨 Responsive and user-friendly UI using **Bootstrap 5**  
- 🔐 Secure handling of `SECRET_KEY` using `.env` file  
- 📦 Clean project structure following Django best practices  

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, Bootstrap 5, Font Awesome  
- **Database:** SQLite  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

```

django-todo-app/
│
├── todo/                 # To-Do application
│   ├── migrations/
│   ├── templates/
│   │   └── todo/
│   │       ├── list.html
│   │       ├── form.html
│   │       └── view.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── todoproject/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── .gitignore
├── .env.example
└── README.md

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/farzeenmuneer/django-todo-app.git
cd django-todo-app
````

---

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install django python-dotenv
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
```

> ⚠️ `.env` is ignored using `.gitignore` for security reasons.

---

### 5️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---
