function diamanteHueco(n) {
    let mitad = (n + 1) / 2;

    for (let i = 1; i <= n; i++) {
        let fila = "";
        // Calcular distancia al centro
        let dist = i <= mitad ? mitad - i : i - mitad;
        let espaciosExternos = dist;
        let espaciosInternos = n - 2 - (dist * 2);

        // Espacios iniciales
        for (let j = 0; j < espaciosExternos; j++) fila += " ";
        
        // Primer asterisco
        fila += "*";

        // Espacios internos y segundo asterisco
        if (espaciosInternos >= 0) {
            for (let k = 0; k < espaciosInternos; k++) fila += " ";
            fila += "*";
        }
        console.log(fila);
    }
}