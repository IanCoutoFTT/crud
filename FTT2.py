from Flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para criar a tabela de tarefas se ela não existir
def create_table():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done BOOLEAN NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
@app.route('/') # o resto do projeto 
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    cur.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tasks (task, completed) VALUES (%s, 0)", (task,))
        mysql.connection.commit()
        cur.close()
        flash('Tarefa adicionada com sucesso!', 'success')
    return redirect(url_for('index'))

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        new_task = request.form['new_task']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tasks SET task = %s WHERE id = %s", (new_task, task_id))
        mysql.connection.commit()
        cur.close()
        flash('Tarefa editada com sucesso!', 'success')
        return redirect(url_for('index'))
    else:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
        task = cur.fetchone()
        cur.close()
        return render_template('edit_task.html', task=task)

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    mysql.connection.commit()
    cur.close()
    flash('Tarefa excluída com sucesso!', 'success')
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    cur = mysql.connection.cursor()
    cur.execute('UPDATE tasks SET completed = 1 WHERE id = %s', (task_id,))
    mysql.connection.commit()
    cur.close()
    flash('Tarefa concluída e marcada com sucesso!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
