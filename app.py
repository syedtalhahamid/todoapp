from flask import Flask, render_template, request, redirect
import MySQLdb

app = Flask(__name__)

# MySQL RDS configuration
db = MySQLdb.connect(
    host="terraform-20251002135421645500000001.cq7quaee28jc.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="Password123!",
    db="mydb"
)

cursor = db.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL
)
""")
db.commit()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    cursor.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
    db.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM todos WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
