function invertirNumero(n) {
    let acumulador = 0;
    let resto = n;
    
    while (resto > 0) {
        let ultimoDigito = resto % 10;
        acumulador = (acumulador * 10) + ultimoDigito;
        resto = (resto - ultimoDigito) / 10; // División entera manual
    }
    return acumulador;
}