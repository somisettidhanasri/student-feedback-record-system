from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# DB Connection
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create Tables
def init_db():
    conn = get_db()

    conn.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    ''')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS feedback(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        message TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

# ---------------- LOGIN ----------------

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()

        if user:
            session['user'] = username
            return redirect('/')
        else:
            return "Invalid Login"

    return render_template('login.html')


@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db()
        conn.execute(
            "INSERT INTO users(username,password) VALUES (?,?)",
            (username, password)
        )
        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


# ---------------- FEEDBACK ----------------

@app.route('/')
def index():
    if 'user' not in session:
        return redirect('/login')

    conn = get_db()
    data = conn.execute("SELECT * FROM feedback").fetchall()
    return render_template('index.html', data=data)


@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        msg = request.form['message']

        conn = get_db()
        conn.execute(
            "INSERT INTO feedback(name,email,message) VALUES (?,?,?)",
            (name,email,msg)
        )
        conn.commit()
        return redirect('/')

    return render_template('add_feedback.html')


@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    conn = get_db()
    data = conn.execute("SELECT * FROM feedback WHERE id=?",(id,)).fetchone()

    if request.method == 'POST':
        conn.execute(
            "UPDATE feedback SET name=?,email=?,message=? WHERE id=?",
            (request.form['name'],request.form['email'],request.form['message'],id)
        )
        conn.commit()
        return redirect('/')

    return render_template('edit_feedback.html', data=data)


@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM feedback WHERE id=?",(id,))
    conn.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)