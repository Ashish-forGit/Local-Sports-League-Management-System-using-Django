# 🏆 Local Sports League Management System

A web-based sports league management system built with **Django** to streamline team registrations, match scheduling, score tracking, and player performance analytics for local leagues. Includes real-time updates, external player stats API integration, and role-based dashboards.

---

## 📌 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [API Integration](#api-integration)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## ✅ Features

- 📝 **Team Registration** with role-based access (Admin, Manager, Player)
- 📅 **Match Scheduling** (Football/Cricket) with time, venue, and team details
- 📊 **Live Score Tracking** using WebSockets (Django Channels)
- 🧮 **Player Stats Management** and Analytics
- 📈 **Real-time Leaderboards**
- 🔍 **Cricket Player Search** using External API
- 🛡️ **Secure Authentication** with Django’s built-in auth
- 📢 **Push Notifications** for upcoming matches
- 🌐 Responsive UI with Bootstrap 5

---

## 🧰 Tech Stack

**Frontend:**
- HTML5, CSS3, Bootstrap
- JavaScript (for dynamic rendering)

**Backend:**
- Python 3, Django 4+
- Django Channels (WebSocket-based updates)

**Database:**
- SQLite3 (default), can be migrated to PostgreSQL/MySQL

**APIs & Integration:**
- External Cricket Player API: `https://cricket-api-demo.up.railway.app/players/{player_name}`
- Custom REST endpoints for match data

**Deployment:**
- Backend: Heroku / Railway / AWS Elastic Beanstalk
- Frontend: Netlify (for static hosting if needed)

---

## 🖼️ Screenshots

![Home Page](static/images/homepage-screenshot.png)
![Match Schedule](static/images/match-schedule.png)
![Live Score](static/images/live-score.png)
![Player Stats](static/images/player-stats.png)

---

## 🛠️ Installation

### Prerequisites:
- Python 3.9+
- pip
- virtualenv

### Steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/sports-league-system.git
cd sports-league-system

# Create virtual environment
python -m venv env
source env/bin/activate  # on Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
