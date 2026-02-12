function diaDelAño(dia, mes, año) {
    let esBisiesto = (año % 4 === 0 && año % 100 !== 0) || (año % 400 === 0);
    let totalDias = dia;

    for (let m = 1; m < mes; m++) {
        if (m === 2) {
            totalDias += esBisiesto ? 29 : 28;
        } else if (m === 4 || m === 6 || m === 9 || m === 11) {
            totalDias += 30;
        } else {
            totalDias += 31;
        }
    }
    return totalDias;
}