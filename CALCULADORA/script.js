const pantalla = document.getElementById('current-operand');
let operacion = '';

function actualizarPantalla() {
    // Si la cadena está vacía, mostramos 0
    pantalla.innerText = operacion || '0';
}

function numero(valor) {
    // Si hay un error en pantalla, limpiamos antes de escribir
    if (operacion === "Error") operacion = '';
    
    // No permitir dos puntos decimales
    if (valor === '.' && operacion.includes('.')) return;
    
    operacion += valor;
    actualizarPantalla();
}

function operar(operador) {
    if (operacion === "Error") operacion = '';
    if (operacion === '') return; // No empezar con operador
    
    operacion += operador;
    actualizarPantalla();
}

function cientifica(tipo) {
    try {
        let valorActual = eval(operacion);
        if (tipo === 'sqrt') operacion = Math.sqrt(valorActual);
        if (tipo === 'cos') operacion = Math.cos(valorActual);
        if (tipo === 'tan') operacion = Math.tan(valorActual);
        
        operacion = operacion.toString();
        actualizarPantalla();
    } catch {
        operacion = "Error";
        actualizarPantalla();
    }
}

function limpiar() {
    operacion = '';
    actualizarPantalla();
}

function borrar() {
    operacion = operacion.slice(0, -1);
    actualizarPantalla();
}

function calcular() {
    try {
        // eval realiza la cuenta matemática automáticamente
        let resultado = eval(operacion);
        operacion = resultado.toString();
        actualizarPantalla();
    } catch {
        operacion = "Error";
        actualizarPantalla();
    }
}
