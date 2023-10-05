// Выражение может содержать скобочки "()" , мат знаки "+ - / *" и цифры от 0 до 9

const AcceptableSymbols = ["(", ")", "+", "-", "/", "*"]

function isNumber(char) {
    return !isNaN(parseInt(char)) && isFinite(char);
}

function isAcceptableSymbol(char) {
    return AcceptableSymbols.includes(char)
}

function validateExpression() {
    var expr = document.getElementById('expr').value;
    
    if (expr === '') {
        alert('Выражение не должно быть пустым');
        return false;
    }

    for (let char of expr) {
        if (isNumber(char) || isAcceptableSymbol(char)) {
            console.log('good')
        } else {
            alert('Выражение имеет не разрешенные символы')
            return false
        }
    }

    return true;
}