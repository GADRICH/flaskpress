📰 FlaskPress

A lightweight blogging platform built with Flask, featuring secure user authentication, post creation, and timestamped entries. FlaskPress is designed to be simple, elegant, and easy to extend — perfect for learning Flask or launching a small personal blog.

✨ Features
🔐 User Authentication – Register, log in, and manage accounts securely.

📝 Create & Manage Posts – Write posts with titles and content.

⏰ Timestamps – Posts automatically record when they were created, displayed in both full date and “time ago” format.

👤 Profile Pages – View posts by individual users.

🎨 Responsive UI – Clean, modern design with CSS/Bootstrap styling.

🗄️ Database Integration – Powered by SQLAlchemy with migrations handled by Flask‑Migrate.

🛠️ Tech Stack
Backend: Flask (Python)

Database: SQLAlchemy + Flask‑Migrate

Frontend: Jinja2 templates + CSS / Bootstrap

Environment: Virtualenv for dependency management

🚀 Getting Started
1. Clone the repository
bash
git clone https://github.com/yourusername/flaskpress.git
cd flaskpress
2. Create a virtual environment
bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
bash
pip install -r requirements.txt
4. Run migrations
bash
flask db upgrade
5. Start the app
bash
flask run
📖 Usage
Register a new account and log in.

Create posts with titles and content.

Posts will display with timestamps (e.g., “5 minutes ago”).

Visit profile pages to see posts by specific users.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License
This project is licensed under the MIT License — see the LICENSE file for details.
