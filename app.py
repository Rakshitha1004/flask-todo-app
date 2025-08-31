from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# store tasks
todo_list = []

# HTML template
template = """
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: #fff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
            width: 400px;
        }
        h1 {
            text-align: center;
            color: #444;
            margin-bottom: 20px;
        }
        form {
            display: flex;
            margin-bottom: 20px;
        }
        input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
        }
        button {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            margin-left: 8px;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover {
            background: #45a049;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #eee;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .done {
            text-decoration: line-through;
            color: gray;
        }
        .actions a {
            text-decoration: none;
            padding: 6px 10px;
            border-radius: 6px;
            font-size: 14px;
            margin-left: 6px;
        }
        .mark-done {
            background: #2196F3;
            color: white;
        }
        .mark-done:hover {
            background: #1976D2;
        }
        .delete {
            background: #f44336;
            color: white;
        }
        .delete:hover {
            background: #d32f2f;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>✅ To-Do List</h1>
        <form method="POST" action="/add">
            <input name="task" placeholder="Enter new task..." required>
            <button type="submit">Add</button>
        </form>
        <ul>
            {% for t in tasks %}
                <li>
                    <span class="{{ 'done' if t['done'] else '' }}">{{ loop.index }}. {{ t['task'] }}</span>
                    <div class="actions">
                        {% if not t['done'] %}
                            <a class="mark-done" href="/done/{{ loop.index }}">✔️ Done</a>
                        {% endif %}
                        <a class="delete" href="/delete/{{ loop.index }}">❌ Delete</a>
                    </div>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(template, tasks=todo_list)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    todo_list.append({"task": task, "done": False})
    return redirect("/")

@app.route("/done/<int:index>")
def done(index):
    if 0 < index <= len(todo_list):
        todo_list[index - 1]["done"] = True
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 < index <= len(todo_list):
        todo_list.pop(index - 1)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
