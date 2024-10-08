import os

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, apology

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['ENV'] = 'development'
Session(app)
def get_db():
    connection = sqlite3.connect('project.db', check_same_thread=False, timeout=10)
    connection.row_factory = sqlite3.Row
    return connection

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    with get_db() as conn:
        cursor = conn.cursor()
        user_id = session.get('user_id')
        cursor.execute("SELECT task_title, task, id FROM tasks WHERE user_id = ?", (user_id,))
        tasks = cursor.fetchall()

    return render_template("index.html", tasks=tasks)


@app.route('/update_task/<int:task_id>', methods=['POST'])
@login_required
def update_task(task_id):
    data = request.get_json()
    new_title = data.get('title')
    new_description = data.get('description')
    
    with get_db() as conn:
        cursor = conn.cursor()
        user_id = session.get('user_id')

        # Verifica se a tarefa pertence ao usuário logado
        cursor.execute("SELECT id FROM tasks WHERE id = ? AND user_id = ?", (task_id, user_id))
        task = cursor.fetchone()

        if task is None:
            return jsonify({'error': 'Task not found or unauthorized'}), 403

        # Atualiza o título e a descrição da tarefa
        cursor.execute("UPDATE tasks SET task_title = ?, task = ? WHERE id = ?", 
                       (new_title, new_description, task_id))
        conn.commit()
    
    return jsonify({'newTitle': new_title, 'newDescription': new_description})


@app.route('/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    with get_db() as conn:
        cursor = conn.cursor()
        user_id = session.get('user_id')
        cursor.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", (task_id, user_id))
        conn.commit()
    return jsonify({'message': 'Task deleted successfully'}), 200

if __name__ == '__main__':
    app.run()

@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Query database for username
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),))
        user = cursor.fetchone()

        # Ensure username exists and password is correct
        if user is None or not check_password_hash(user["hash"], request.form.get("password")):
            conn.close()
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = user["id"]

        # Redirect user to home page
        conn.close()
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
    
@app.route("/logout")
@login_required
def logout():
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        
        password = request.form.get("password")

        confirm = request.form.get("confirmation")

        if confirm != password:
            return apology("Passwords don't match")
        
        db = get_db()
        cursor = db.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone() # cursor.fetchone() retorna None se não encontrar uma linha.
        
        if user is None:
            hashed_pwd = generate_password_hash(password)
            cursor.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (username, hashed_pwd))
            db.commit()
            db.close()
            return redirect("/")
        else:
            db.close()
            return apology("This username already exists")
    else:
        return render_template("register.html")
    

@app.route("/task", methods =["GET", "POST"])
@login_required
def task():
    if request.method == "GET":
        return render_template("task.html")
    
    else:
        user_id = session["user_id"]
        task_title = request.form.get("task_title")
        task = request.form.get("description")
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (user_id, task_title, task) VALUES (?, ?, ?)", (user_id, task_title, task))
            conn.commit()
        return redirect("/")