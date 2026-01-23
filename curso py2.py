import os
import time

class SimuladorCestaCompras:
    def __init__(self):
        self.cesta = []
        self.precios = {}
        self.mensajes = {
            'bienvenida': """
            🛒💻 ¡BIENVENIDO AL SIMULADOR DE CESTA DE COMPRA! 💻🛒
            ============================================
            Gestiona tu cesta de compras de forma fácil y divertida
            """,
            'despedida': """
            \n👋 ¡Gracias por usar nuestro simulador de compras!
            ¡Vuelve pronto! 👋
            """,
            'opcion_invalida': "❌ ¡Ups! Esa opción no es válida. Intenta de nuevo.",
            'cesta_vacia': "🧺 Tu cesta está vacía. ¡Agrega algunos productos!"
        }
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_menu(self):
        """Muestra el menú principal del programa"""
        print("\n" + "="*50)
        print("🏪 MENÚ PRINCIPAL - CESTA DE COMPRAS 🏪")
        print("="*50)
        print("1. ➕ AGREGAR un nuevo elemento")
        print("2. 🧺 MOSTRAR el contenido de la cesta")
        print("3. ❌ ELIMINAR un elemento")
        print("4. 💰 CALCULAR el total de la compra")
        print("5. 👋 RENUNCIAR (Salir del programa)")
        print("="*50)
    
    def agregar_elemento(self):
        """Permite al usuario agregar un nuevo elemento a la cesta"""
        print("\n" + "="*50)
        print("➕ AGREGAR NUEVO PRODUCTO ➕")
        print("="*50)
        
        while True:
            producto = input("¿Qué producto quieres agregar? 📦: ").strip()
            if not producto:
                print("❌ El nombre del producto no puede estar vacío.")
                continue
            
            if producto in self.cesta:
                print(f"⚠️  '{producto}' ya está en la cesta. Agrega otro producto.")
                continue
            
            # Solicitar precio del producto
            while True:
                try:
                    precio = float(input(f"💵 Precio de '{producto}' (ej: 2.50): €"))
                    if precio <= 0:
                        print("❌ El precio debe ser mayor a 0.")
                        continue
                    break
                except ValueError:
                    print("❌ Por favor, introduce un número válido para el precio.")
            
            # Solicitar cantidad
            while True:
                try:
                    cantidad = int(input(f"🔢 Cantidad de '{producto}': "))
                    if cantidad <= 0:
                        print("❌ La cantidad debe ser mayor a 0.")
                        continue
                    break
                except ValueError:
                    print("❌ Por favor, introduce un número entero válido.")
            
            # Agregar producto a la cesta
            for _ in range(cantidad):
                self.cesta.append(producto)
            
            # Guardar precio del producto
            self.precios[producto] = precio
            
            print(f"\n✅ ¡Producto agregado! Se han añadido {cantidad} unidad(es) de '{producto}' a la cesta.")
            print(f"   📍 Precio unitario: €{precio:.2f}")
            
            agregar_otro = input("\n¿Quieres agregar otro producto? (s/n): ").lower()
            if agregar_otro != 's':
                break
    
    def mostrar_cesta(self):
        """Muestra el contenido actual de la cesta de compra"""
        print("\n" + "="*50)
        print("🧺 CONTENIDO DE TU CESTA 🧺")
        print("="*50)
        
        if not self.cesta:
            print(self.mensajes['cesta_vacia'])
            return
        
        # Contar productos únicos y sus cantidades
        productos_unicos = {}
        for producto in self.cesta:
            if producto in productos_unicos:
                productos_unicos[producto] += 1
            else:
                productos_unicos[producto] = 1
        
        # Mostrar productos con formato atractivo
        print(f"📊 Total de artículos en la cesta: {len(self.cesta)}")
        print("-"*50)
        
        for i, (producto, cantidad) in enumerate(productos_unicos.items(), 1):
            precio_unitario = self.precios.get(producto, 0)
            subtotal = precio_unitario * cantidad
            print(f"{i}. {producto.upper():<20} x{cantidad:<3} €{precio_unitario:<6.2f} c/u  Subtotal: €{subtotal:.2f}")
        
        print("="*50)
    
    def eliminar_elemento(self):
        """Permite al usuario eliminar un elemento de la cesta"""
        print("\n" + "="*50)
        print("❌ ELIMINAR PRODUCTO DE LA CESTA ❌")
        print("="*50)
        
        if not self.cesta:
            print(self.mensajes['cesta_vacia'])
            return
        
        # Mostrar productos únicos para eliminar
        productos_unicos = list(set(self.cesta))
        
        print("Productos en tu cesta:")
        for i, producto in enumerate(productos_unicos, 1):
            cantidad = self.cesta.count(producto)
            print(f"{i}. {producto} (Cantidad: {cantidad})")
        
        while True:
            try:
                opcion = int(input("\nSelecciona el número del producto a eliminar (0 para cancelar): "))
                
                if opcion == 0:
                    print("🚫 Operación cancelada.")
                    return
                
                if 1 <= opcion <= len(productos_unicos):
                    producto_a_eliminar = productos_unicos[opcion - 1]
                    
                    # Preguntar cuántos eliminar
                    cantidad_en_cesta = self.cesta.count(producto_a_eliminar)
                    print(f"\nHay {cantidad_en_cesta} unidad(es) de '{producto_a_eliminar}' en la cesta.")
                    
                    while True:
                        try:
                            cantidad_eliminar = int(input(f"¿Cuántas unidades quieres eliminar? (1-{cantidad_en_cesta}): "))
                            
                            if 1 <= cantidad_eliminar <= cantidad_en_cesta:
                                # Eliminar la cantidad especificada
                                for _ in range(cantidad_eliminar):
                                    self.cesta.remove(producto_a_eliminar)
                                
                                print(f"✅ Se eliminaron {cantidad_eliminar} unidad(es) de '{producto_a_eliminar}'.")
                                
                                # Si ya no hay más de ese producto, eliminar su precio
                                if producto_a_eliminar not in self.cesta:
                                    del self.precios[producto_a_eliminar]
                                
                                break
                            else:
                                print(f"❌ Cantidad no válida. Introduce un número entre 1 y {cantidad_en_cesta}.")
                        except ValueError:
                            print("❌ Por favor, introduce un número válido.")
                    
                    break
                else:
                    print("❌ Opción no válida. Intenta de nuevo.")
            except ValueError:
                print("❌ Por favor, introduce un número válido.")
    
    def calcular_total(self):
        """Calcula y muestra el total de la compra"""
        print("\n" + "="*50)
        print("💰 CALCULAR TOTAL DE LA COMPRA 💰")
        print("="*50)
        
        if not self.cesta:
            print(self.mensajes['cesta_vacia'])
            return
        
        # Mostrar contenido primero
        self.mostrar_cesta()
        
        # Calcular total
        total = 0
        productos_unicos = {}
        
        for producto in self.cesta:
            if producto in productos_unicos:
                productos_unicos[producto] += 1
            else:
                productos_unicos[producto] = 1
        
        print("\n" + "="*50)
        print("📋 RESUMEN DE COMPRA 📋")
        print("="*50)
        
        for producto, cantidad in productos_unicos.items():
            precio = self.precios.get(producto, 0)
            subtotal = precio * cantidad
            total += subtotal
            print(f"• {producto:<15} x{cantidad:<3} €{subtotal:.2f}")
        
        print("-"*50)
        print(f"💵 TOTAL A PAGAR: €{total:.2f}")
        
        # Efecto especial para el total
        if total > 0:
            print("\n" + "✨" * 25)
            print(f"   💳 TOTAL FINAL: €{total:.2f} 💳")
            print("✨" * 25)
            
            # Sugerencia según el total
            if total > 100:
                print("\n💡 ¡Vaya compra grande! ¿Necesitas ayuda para llevar las bolsas? 🛍️")
            elif total > 50:
                print("\n💡 ¡Buena compra! No olvides revisar las ofertas la próxima vez. 🏷️")
            else:
                print("\n💡 ¡Compra inteligente! Has mantenido un buen control de tu presupuesto. 👍")
    
    def ejecutar(self):
        """Método principal que ejecuta el simulador"""
        self.limpiar_pantalla()
        print(self.mensajes['bienvenida'])
        
        # Pausa para que el usuario pueda leer el mensaje de bienvenida
        input("\nPresiona Enter para continuar...")
        
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu()
            
            try:
                opcion = int(input("\n👉 Selecciona una opción (1-5): "))
                
                if opcion == 1:
                    self.agregar_elemento()
                elif opcion == 2:
                    self.mostrar_cesta()
                elif opcion == 3:
                    self.eliminar_elemento()
                elif opcion == 4:
                    self.calcular_total()
                elif opcion == 5:
                    # Confirmar salida
                    confirmar = input("\n¿Estás seguro de que quieres salir? (s/n): ").lower()
                    if confirmar == 's':
                        print(self.mensajes['despedida'])
                        break
                    else:
                        print("¡Continuamos con la compra! 🛒")
                        continue
                else:
                    print(self.mensajes['opcion_invalida'])
                
                # Pausa antes de volver al menú
                input("\nPresiona Enter para volver al menú principal...")
                
            except ValueError:
                print(self.mensajes['opcion_invalida'])
                time.sleep(1.5)

# Función principal para ejecutar el programa
def main():
    simulador = SimuladorCestaCompras()
    simulador.ejecutar()

# Punto de entrada del programa
if __name__ == "__main__":
    main()