function factoresPrimos(n) {
    let divisor = 2;
    let temp = n;
    while (temp > 1) {
        while (temp % divisor === 0) {
            console.log(divisor);
            temp /= divisor;
        }
        divisor++;
    }
}