# Создать изолированную среду
# Зависимости - Flask, Jinja
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
from flask import Flask,render_template,session

user_id_string_length = 25 # Move it to .env

app = Flask(__name__)

userSessions = {}                    #sessionId:{line:str,res:number}

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.get('/')
def get():                           #html
    # Если юзера нет то надо его создать и сгенерировать ему значение
    if(("user_id" in session) == False):
        session.error = 'errros'
        session['user_id'] = get_random_string(user_id_string_length)
    return render_template('home.html',arr=[1,2,3,4],error_msg=session.error if "error" in session else "")


@app.get("/history")
def getSessionInfo(sessionId):        #json  
    pass


@app.post('/calc')
def post(sessionId,calcStr):          #400 or number
    pass




def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def parseAndValidateStr(str):        #[str,isValid]
    pass


print('i work')



