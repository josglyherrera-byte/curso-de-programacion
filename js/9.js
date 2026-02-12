function cajero(monto) {
    let restante = monto;

    // Procesar cada denominación secuencialmente
    let b100 = (restante - (restante % 100)) / 100;
    restante %= 100;
    if (b100 > 0) console.log(b100 + " billetes de 100");

    let b50 = (restante - (restante % 50)) / 50;
    restante %= 50;
    if (b50 > 0) console.log(b50 + " billetes de 50");

    let b20 = (restante - (restante % 20)) / 20;
    restante %= 20;
    if (b20 > 0) console.log(b20 + " billetes de 20");

    let b10 = (restante - (restante % 10)) / 10;
    restante %= 10;
    if (b10 > 0) console.log(b10 + " billetes de 10");

    let b5 = (restante - (restante % 5)) / 5;
    restante %= 5;
    if (b5 > 0) console.log(b5 + " billetes de 5");

    if (restante > 0) console.log(restante + " billetes de 1");
}