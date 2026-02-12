function binarioADecimal(binario) {
    let decimal = 0;
    let base = 1; // 2^0
    let resto = binario;

    while (resto > 0) {
        let ultimoDigito = resto % 10;
        decimal += ultimoDigito * base;
        base *= 2;
        resto = (resto - ultimoDigito) / 10;
    }
    return decimal;
}