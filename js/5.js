function sonAmigos(a, b) {
    let sumaA = 0;
    let sumaB = 0;

    for (let i = 1; i < a; i++) {
        if (a % i === 0) sumaA += i;
    }
    for (let j = 1; j < b; j++) {
        if (b % j === 0) sumaB += j;
    }

    return (sumaA === b && sumaB === a);
}