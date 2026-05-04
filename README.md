# 🎓 Student Feedback Record System using Flask

A simple web application built using Flask that allows users to manage student feedback with CRUD operations (Create, Read, Update, Delete).


## 🚀 Features

- ➕ Add feedback  
- 📋 View feedback list  
- ✏️ Update feedback  
- ❌ Delete feedback  
- 🔐 User Login & Signup system  



## 🛠️ Technologies Used

- Python (Flask)
- SQLite (Database)
- HTML, CSS (Bootstrap)
- Jinja2 Templates


Project Structure

student_feedback_system/
│
├── app.py                
├── requirements.txt     
├── database.db          
├── README.md           
├── .gitignore           
│
├── templates/           
│   ├── base.html
│   ├── index.html
│   ├── add_feedback.html
│   ├── edit_feedback.html
│   ├── login.html
│   ├── signup.html
│
├── static/              
│   ├── style.css
│   └── bg.jpg
│
└── venv/


Running Commands:

Create Virtual Environment
python -m venv venv
3️⃣ Activate Virtual Environment
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
4️⃣ Install Dependencies
pip install -r requirements.txt
pip install flask
5️⃣ Run the Application
python app.py
6️⃣ Open in Browser
http://127.0.0.1:5000/
