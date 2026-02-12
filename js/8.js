function validarTarjeta(num) {
    let suma = 0;
    let temporal = num;

    for (let i = 1; i <= 8; i++) {
        let digito = temporal % 10;
        // Si la posición es par (contando de derecha a izquierda)
        if (i % 2 === 0) {
            digito *= 2;
            if (digito > 9) digito -= 9;
        }
        suma += digito;
        temporal = (temporal - (temporal % 10)) / 10;
    }
    return suma % 10 === 0;
}