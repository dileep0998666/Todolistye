from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__, template_folder="templates")

todos = [{"task": "Samples Todo", "done": False}]

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task": todo, "done": False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    if request.method == "POST":
        # Update the todo item in the list
        todos[index]["task"] = request.form['todo']
        return redirect(url_for("index"))
    else:
        # Render the edit form with the todo item data
        todo = todos[index]["task"]
        return render_template("edit.html", todo=todo, index=index)

@app.route("/check/<int:index>")
def check(index):
    todos[index]['done']=not todos[index]['done']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))
if __name__ == '__main__':
    app.run(debug=True)
