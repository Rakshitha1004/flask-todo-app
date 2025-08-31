from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# store tasks as dictionary with extra details
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
            min-height: 100vh;
            margin: 0;
        }
        .container {
            background: #fff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
            width: 500px;
        }
        h1 {
            text-align: center;
            color: #444;
            margin-bottom: 20px;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 20px;
        }
        input, select {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
        }
        button {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover { background: #45a049; }
        ul { list-style-type: none; padding: 0; }
        li {
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #eee;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .done { text-decoration: line-through; color: gray; }
        .actions a {
            text-decoration: none;
            padding: 6px 10px;
            border-radius: 6px;
            font-size: 14px;
            margin-left: 6px;
        }
        .mark-done { background: #2196F3; color: white; }
        .mark-done:hover { background: #1976D2; }
        .delete { background: #f44336; color: white; }
        .delete:hover { background: #d32f2f; }
        .clear { background: #ff9800; color: white; margin-top: 10px; display: block; text-align: center; padding: 8px; border-radius: 8px; }
        .clear:hover { background: #e68900; }
        .priority-high { background: #e74c3c; color: white; padding: 3px 6px; border-radius: 5px; font-size: 12px; }
        .priority-medium { background: #f39c12; color: white; padding: 3px 6px; border-radius: 5px; font-size: 12px; }
        .priority-low { background: #2ecc71; color: white; padding: 3px 6px; border-radius: 5px; font-size: 12px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>✅ To-Do List</h1>
        <form method="POST" action="/add">
            <input name="task" placeholder="Enter new task..." required>
            <input type="date" name="due_date" required>
            <select name="priority">
                <option value="High">🔥 High</option>
                <option value="Medium">⚡ Medium</option>
                <option value="Low">🌱 Low</option>
            </select>
            <button type="submit">Add Task</button>
        </form>
        <ul>
            {% for t in tasks %}
                <li>
                    <span class="{{ 'done' if t['done'] else '' }}">
                        {{ loop.index }}. {{ t['task'] }}
                        <small>(Due: {{ t['due'] }})</small>
                        {% if t['priority'] == 'High' %}
                            <span class="priority-high">High</span>
                        {% elif t['priority'] == 'Medium' %}
                            <span class="priority-medium">Medium</span>
                        {% else %}
                            <span class="priority-low">Low</span>
                        {% endif %}
                    </span>
                    <div class="actions">
                        {% if not t['done'] %}
                            <a class="mark-done" href="/done/{{ loop.index }}">✔️ Done</a>
                        {% endif %}
                        <a class="delete" href="/delete/{{ loop.index }}">❌ Delete</a>
                    </div>
                </li>
            {% endfor %}
        </ul>
        {% if tasks %}
            <a class="clear" href="/clear">🗑️ Clear All</a>
        {% endif %}
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
    due_date = request.form["due_date"]
    priority = request.form["priority"]
    todo_list.append({"task": task, "done": False, "due": due_date, "priority": priority})
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

@app.route("/clear")
def clear():
    todo_list.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
