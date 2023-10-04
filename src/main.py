# Создать изолированную среду
# Мат выражение - *, :, ^, -, +
# Создать гет и пост запрос, сперва сделать html документ с формой ввода мат строки, кнопочкой снизу и сверху сделаю сообщение об ошибке,
# а еще снизу история введеных строк и полученных результатов и у истории будет кнопка refresh
# Создать обьект хранящий сессии пользователей это sessionId:[line:str,res:number]
# при запросе localhost:3500 он должен отправлять html документ с формой
# при запросе localhost:3500/calc он должен принимать пост запрос
# Апи принимает пост запрос, парсит строку,валидирует все ли кнопочки закрыты, сохраняет в структуру данных хранящую сессию пользователя
# Пользователь ввел в форму мат выражение, нажал кнопку, мат выражение валидируется,
#  отправляется пост запрос на 'calc' с сессией, приходит ответ res и отображается в форме
import string
import random
from flask import Flask, render_template, session as _session
import os
from dotenv import load_dotenv
from types_ import SessionData


load_dotenv()

session: SessionData = _session

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
user_id_string_length = int(os.getenv("USER_ID_STRING_LENGTH"))


@app.before_request
def before_request():
    if ("user_id" in session) == False:
        session["error_msg"] = "An error"
        session["user_id"] = get_random_string(user_id_string_length)


@app.get("/")
def get() -> str:  # html
    return render_template(
        "home.html",
        history=session['history'] if 'history' in session else {},
        error_msg=session['error_msg'] if "error_msg" in session else "",
    )


@app.get("/history")
def getSessionInfo(sessionId):  # json
    pass


@app.post("/calc")
def post(sessionId, calcStr):  # 400 or number
    pass


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


def parseAndValidateStr(str):  # [str,isValid]
    pass


print("i do work")
