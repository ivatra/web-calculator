const AcceptableSymbols = ["(", ")", "+", "-", "/", "*", " "]

function _isNumber(char) {
    return !isNaN(parseInt(char)) && isFinite(char);
}

function _isAcceptableSymbol(char) {
    return AcceptableSymbols.includes(char)
}

function validateExpression() {
    var expr = document.getElementById('expr').value;

    if (expr === '') {
        alert('Выражение не должно быть пустым');
        return false;
    }

    for (let char of expr) {
        if (!_isNumber(char) && !_isAcceptableSymbol(char)) {
            alert('Выражение имеет не разрешенные символы')
            return false
        }
    }
    return true;
}