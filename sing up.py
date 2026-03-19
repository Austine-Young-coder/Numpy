from flask import Flask, request, redirect, render_template_string
import sqlite3
import hashlib

app = Flask(__name__)

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------- PASSWORD HASH ----------
def hash_pass(p):
    return hashlib.sha256(p.encode()).hexdigest()

# ---------- HTML + CSS ----------
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Signup</title>
<style>
body{
    background: linear-gradient(120deg, #000, #0f0);
    font-family: Arial;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}
.card{
    background:#111;
    padding:30px;
    border-radius:10px;
    width:320px;
    box-shadow:0 0 20px #0f0;
}
h2{color:#0f0;text-align:center;}
input{
    width:100%;
    padding:10px;
    margin:10px 0;
    background:#000;
    border:1px solid #0f0;
    color:white;
}
button{
    width:100%;
    padding:10px;
    background:#0f0;
    border:none;
    font-weight:bold;
}
.msg{color:yellow;text-align:center;}
</style>
</head>

<body>
<div class="card">
<h2>Create Account</h2>
<form method="POST">
<input type="text" name="name" placeholder="Full Name" required>
<input type="email" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign Up</button>
</form>
<p class="msg">{{msg}}</p>
</div>
</body>
</html>
"""

# ---------- ROUTE ----------
@app.route("/", methods=["GET", "POST"])
def signup():
    msg = ""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = hash_pass(request.form["password"])

        try:
            conn = sqlite3.connect("users.db")
            c = conn.cursor()
            c.execute("INSERT INTO users(name,email,password) VALUES(?,?,?)",
                      (name,email,password))
            conn.commit()
            conn.close()
            msg = "Account created successfully!"
        except:
            msg = "Email already exists!"

    return render_template_string(HTML, msg=msg)

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)