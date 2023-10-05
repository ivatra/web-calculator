import os

from dotenv import load_dotenv

load_dotenv()

from flask import Flask, redirect, render_template, session, request, url_for

from funcs import get_random_string, validate_and_calculate_expression


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
user_id_len = int(os.getenv("USER_ID_STRING_LENGTH"))


def session_append(key:str,el:any):
    arr = session[key]
    arr.append(el)
    session[key] = arr


@app.before_request
def before_request():  # Делаем middleware в случае маштабирования приложения (может быть несколько get url)
    if ("user_id" in session) == False:
        session["user_id"] = get_random_string(user_id_len)
        session["history"] = []


@app.get("/")
def get():
    return render_template(
        "home.html",
        expr_result=session.get("expr_result"),
        history=session.get("history"),
        error_msg=session.get("error_msg"),
    )


@app.post("/")
def calculate():
    expr = request.form.get("expr")
    res, err = validate_and_calculate_expression(expr)
    if err:
        session["error_msg"] = err
    else:
        new_history_el = {"expr": expr, "result": res}
        session_append("history",new_history_el)
        
    return redirect(url_for("get"))

if __name__ == "__main__":
    app.run(debug=True)
