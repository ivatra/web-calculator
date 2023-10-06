import os

from dotenv import load_dotenv
from sympy import SympifyError

load_dotenv()

from flask import Flask, redirect, render_template, session, request, url_for

from funcs import get_random_string, calculate_expression


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
user_id_len = int(os.getenv("USER_ID_STRING_LENGTH"))


def append_to_session_array(key: str, el: any):
    arr = session[key]
    arr.append(el)
    session[key] = arr


@app.before_request
def before_request():  # Делаю middleware в случае маcштабирования приложения (может быть несколько get url)
    if ("user_id" in session) == False:
        session["user_id"] = get_random_string(user_id_len)
        session["history"] = []


@app.get("/")
def get():
    return render_template(
        "home.html",
        history=session.get("history"),
        error_msg=session.get("error_msg"),
    )


@app.post("/")
def calculate():
    expr = request.form.get("expr")
    err, res = None, None

    try:
        res = calculate_expression(expr)
    except (TypeError, ZeroDivisionError, ValueError,SympifyError) as error:
        err = str(error)

    if not err:
        new_history_el = {"expr": expr, "result": res}
        append_to_session_array("history", new_history_el)

    session["error_msg"] = err
    return redirect(url_for("get"))


if __name__ == "__main__":
    app.run(debug=True)
