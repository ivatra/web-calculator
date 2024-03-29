var ExpressionValidator = ( () => {
    function setAlertMessage(msg) {
        var alertObj = document.getElementById('alert');
        var exprObject = document.getElementById('expr')
        alertObj.className = "alert alert-danger display-block";
        alertObj.innerText = msg;
        exprObject.value = ""
       
    }

    function isLetter(c) {
        return c.toLowerCase() != c.toUpperCase();
    }

    function validateExpression() {
        var expr = document.getElementById('expr').value;

        if (expr === '') {
            setAlertMessage('Выражение не должно быть пустым');
            return false;
        }

        for (let char of expr) {
            if (isLetter(char)) {
                setAlertMessage("B выражении не должно быть букв")
                return false
            }
        }

        if (expr.length > 40) {
            setAlertMessage("Выражение должно быть меньше 40 символов")
            return false
        }
        return true;
    }

    return {
        validateExpression: validateExpression
    };
})();
