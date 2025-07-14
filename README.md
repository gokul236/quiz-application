# Django Quiz Application

A modern, responsive web-based Quiz Application built with Django. This project allows users to register, log in, take quizzes in various subjects, view their results, and manage their profiles. Admins can manage users and quiz questions through a dedicated interface.

---

## 🚀 Features

- **User Registration & Login**
- **Quiz by Subject** (Current Affairs, Social Studies, Science, Mathematics, etc.)
- **Multiple Choice Questions**
- **Result Calculation & Display**
- **Profile Management**
- **Admin Dashboard** (Manage Users & Questions)
- **Modern UI/UX** (Bootstrap + Custom CSS)
- **Responsive & Mobile-Friendly**

---

## 🏗️ Project Structure

```
quiz application/
├── main.py
├── mypro/
│   ├── db.sqlite3
│   ├── manage.py
│   ├── myapp/
│   ├── mypro/
│   ├── static/
│   │   └── custom.css
│   ├── media/
│   └── templates/
│       ├── loginpage.html
│       ├── registerpage.html
│       ├── userhome.html
│       ├── adminhome.html
│       ├── questiondisplay.html
│       ├── resultpage.html
│       ├── addquestions.html
│       ├── viewprofile.html
│       └── ...
├── venv/
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd "quiz application"
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install django
   ```

4. **Apply migrations:**
   ```bash
   cd mypro
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the app:**
   - Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 👤 Admin Access

To create a superuser (admin):
```bash
python manage.py createsuperuser
```
Then log in at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📁 Key Folders

- `mypro/myapp/` - Main Django app (models, views, etc.)
- `mypro/templates/` - HTML templates
- `mypro/static/` - Static files (CSS, images)
- `mypro/media/` - Uploaded user photos
- `mypro/db.sqlite3` - SQLite database

---

## ✨ Customization
- Update questions, categories, and users via the admin dashboard.
- Change branding, colors, and images in `static/` and `templates/`.

---

## 🤝 Contributing
1. Fork this repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

---

## 📄 License
This project is for educational/demo purposes. Please add your own license if you plan to use it in production.

---

## 🙏 Acknowledgements
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Google Fonts](https://fonts.google.com/)

---

Happy quizzing! 🎉 
