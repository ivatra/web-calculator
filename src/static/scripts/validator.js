var ExpressionValidator = ( () => {
    function setAlertMessage(msg) {
        var alertObj = document.getElementById('alert');
        alertObj.className = "alert alert-danger display-block";
        alertObj.innerText = msg;
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
            setAlertMessage("Слишком большое выражение")
            return false
        }
        return true;
    }

    return {
        validateExpression: validateExpression
    };
})();
