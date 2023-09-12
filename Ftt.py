from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def create_task(task):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, completed) VALUES (?, 0)", (task,))
    conn.commit()
    conn.close()

def list_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def edit_task(task_id, new_task):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_task, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

def mark_task_completed(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

while True:
    print("\n1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Editar tarefa")
    print("4. Excluir tarefa")
    print("5. Marcar tarefa como concluída")
    print("6. Sair")

    choice = input("Escolha uma opção: ")

    if choice == "1":
        task = input("Digite a tarefa: ")
        create_task(task)
        print("Tarefa adicionada com sucesso!")
    elif choice == "2":
        tasks = list_tasks()
        print("\nLista de Tarefas:")
        for task in tasks:
            status = "Concluída" if task[2] else "Pendente"
            print(f"{task[0]}. [{status}] {task[1]}")
    elif choice == "3":
        task_id = input("Digite o ID da tarefa a ser editada: ")
        new_task = input("Digite a nova descrição da tarefa: ")
        edit_task(task_id, new_task)
        print("Tarefa editada com sucesso!")
    elif choice == "4":
        task_id = input("Digite o ID da tarefa a ser excluída: ")
        delete_task(task_id)
        print("Tarefa excluída com sucesso!")
    elif choice == "5":
        task_id = input("Digite o ID da tarefa a ser marcada como concluída: ")
        mark_task_completed(task_id)
        print("Tarefa marcada como concluída com sucesso!")
    elif choice == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")