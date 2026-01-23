print("=" * 60)
print("        🎮 AVENTURA EN EL BOSQUE OSCURO 🎮")
print("=" * 60)
print("\nTe encuentras caminando por un bosque oscuro 🌲🌌")
print("y encuentras dos objetos: un *FÓSFORO* y una *LINTERNA*")
print("¿Con cuál te quedas?")

# Primer nivel de decisión
respuesta = input("\nTu elección: ").lower().strip()

if respuesta == "fósforo" or respuesta == "fosforo":
    print("\n" + "=" * 60)
    print("Coges el fósforo y lo enciendes 🔥.")
    print("Por un instante, el bosque se ilumina...")
    print("¡Y ves un gran oso grizzly! 🐻 El fósforo se apaga.")
    print("\n¿Qué haces?")
    print("Opciones: CORRER, ESCONDERTE, QUEDARTE QUIETO")
    
    respuesta = input("\nTu elección: ").lower().strip()
    
    if respuesta == "correr":
        # Segundo nivel de decisión (rama 1)
        print("\n" + "=" * 60)
        print("Corres tan rápido como puedes 💨")
        print("El oso te persigue, pero encuentras un río 🏞️")
        print("\n¿Qué haces?")
        print("Opciones: CRUZAR EL RÍO, ESCONDERTE ENTRE LOS ÁRBOLES, SUBIR A UN ÁRBOL")
        
        respuesta = input("\nTu elección: ").lower().strip()
        
        if respuesta == "cruzar el río" or respuesta == "cruzar":
            # Tercer nivel de decisión (rama 1.1)
            print("\n" + "=" * 60)
            print("Te lanzas al agua y nadas hasta la otra orilla 🌊")
            print("El oso no te sigue, ¡estás a salvo!")
            print("Al otro lado ves una cueva misteriosa 🕳️")
            print("\n¿Qué haces?")
            print("Opciones: ENTRAR EN LA CUEVA, SEGUIR POR EL CAMINO, BUSCAR REFUGIO")
            
            respuesta = input("\nTu elección: ").lower().strip()
            
            if respuesta == "entrar en la cueva" or respuesta == "entrar":
                # Cuarto nivel de decisión (rama 1.1.1)
                print("\n" + "=" * 60)
                print("Entras en la cueva y encuentras un viejo cofre 💎")
                print("También ves pinturas rupestres en las paredes 🎨")
                print("\n¿Qué haces?")
                print("Opciones: ABRIR EL COFRE, ESTUDIAR LAS PINTURAS, SALIR DE LA CUEVA")
                
                respuesta = input("\nTu elección: ").lower().strip()
                
                if respuesta == "abrir el cofre" or respuesta == "abrir":
                    # Quinto nivel de decisión (rama 1.1.1.1)
                    print("\n" + "=" * 60)
                    print("¡El cofre contiene un mapa del tesoro! 🗺️")
                    print("Y una antigua espada mágica ⚔️")
                    print("\n¿Qué haces?")
                    print("Opciones: SEGUIR EL MAPA, TOMAR LA ESPADA, DEJAR TODO Y SALIR")
                    
                    respuesta = input("\nTu elección: ").lower().strip()
                    
                    if respuesta == "seguir el mapa" or respuesta == "seguir":
                        # Sexto nivel de decisión (rama 1.1.1.1.1)
                        print("\n" + "=" * 60)
                        print("Sigues el mapa y encuentras un tesoro perdido! 💰✨")
                        print("¡FELICIDADES! Has ganado la aventura 🏆")
                        print("=" * 60)
                    elif respuesta == "tomar la espada" or respuesta == "tomar":
                        # Sexto nivel de decisión (rama 1.1.1.1.2)
                        print("\n" + "=" * 60)
                        print("La espada brilla con energía mágica ✨")
                        print("Te sientes más valiente y decides explorar más el bosque")
                        print("Encuentras la salida del bosque sano y salvo 🏡")
                        print("¡FIN DE LA AVENTURA!")
                        print("=" * 60)
                    elif respuesta == "dejar todo y salir" or respuesta == "dejar":
                        # Sexto nivel de decisión (rama 1.1.1.1.3)
                        print("\n" + "=" * 60)
                        print("Decides que el tesoro no es para ti...")
                        print("Sales de la cueva y encuentras un camino a casa 🏠")
                        print("¡FIN DE LA AVENTURA!")
                        print("=" * 60)
                    else:
                        print("\nOpción no válida. La aventura termina aquí.")
                        
                elif respuesta == "estudiar las pinturas" or respuesta == "estudiar":
                    # Quinto nivel de decisión (rama 1.1.1.2)
                    print("\n" + "=" * 60)
                    print("Las pinturas muestran la historia de una civilización perdida 🏺")
                    print("Aprendes secretos antiguos pero no encuentras tesoros")
                    print("Sales de la cueva con conocimiento, pero sin riquezas 📚")
                    print("¡FIN DE LA AVENTURA!")
                    print("=" * 60)
                elif respuesta == "salir de la cueva" or respuesta == "salir":
                    # Quinto nivel de decisión (rama 1.1.1.3)
                    print("\n" + "=" * 60)
                    print("Sales de la cueva y te pierdes en el bosque 🌲")
                    print("Después de horas de caminar, encuentras ayuda 🚶‍♂️")
                    print("¡FIN DE LA AVENTURA!")
                    print("=" * 60)
                else:
                    print("\nOpción no válida. La aventura termina aquí.")
                    
            elif respuesta == "seguir por el camino" or respuesta == "seguir":
                # Cuarto nivel de decisión (rama 1.1.2)
                print("\n" + "=" * 60)
                print("Sigues el camino y encuentras una cabaña abandonada 🛖")
                print("Dentro hay provisiones y un lugar seguro para descansar")
                print("¡Has encontrado refugio por la noche! 🌙")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            elif respuesta == "buscar refugio" or respuesta == "buscar":
                # Cuarto nivel de decisión (rama 1.1.3)
                print("\n" + "=" * 60)
                print("Buscas refugio y encuentras un árbol hueco 🌳")
                print("Pasas la noche allí y al amanecer encuentras el camino a casa ☀️")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            else:
                print("\nOpción no válida. La aventura termina aquí.")
                
        elif respuesta == "esconderte entre los árboles" or respuesta == "esconderte":
            # Tercer nivel de decisión (rama 1.2)
            print("\n" + "=" * 60)
            print("Te escondes entre los árboles 🌳🌳🌳")
            print("El oso pasa de largo sin verte 👀")
            print("¡Estás a salvo! Encuentras un sendero iluminado por la luna 🌕")
            print("\n¿Qué haces?")
            print("Opciones: SEGUIR EL SENDERO, DESCANSAR, BUSCAR COMIDA")
            
            respuesta = input("\nTu elección: ").lower().strip()
            
            if respuesta == "seguir el sendero" or respuesta == "seguir":
                # Cuarto nivel de decisión (rama 1.2.1)
                print("\n" + "=" * 60)
                print("El sendero te lleva a un claro mágico ✨")
                print("Ves hadas y criaturas del bosque bailando 🧚‍♂️")
                print("Pasan la noche con ellos y al amanecer te guían a casa 🏡")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            elif respuesta == "descansar" or respuesta == "descansar":
                print("\n" + "=" * 60)
                print("Descansas bajo un árbol y te quedas dormido 😴")
                print("Al despertar, el sol está saliendo y encuentras el camino ☀️")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            elif respuesta == "buscar comida" or respuesta == "comida":
                print("\n" + "=" * 60)
                print("Encuentras bayas silvestres 🍓 y setas 🍄")
                print("Te alimentas y recuperas fuerzas para continuar 💪")
                print("Encuentras el camino de vuelta a la civilización 🚶‍♂️")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            else:
                print("\nOpción no válida. La aventura termina aquí.")
                
        elif respuesta == "subir a un árbol" or respuesta == "subir":
            # Tercer nivel de decisión (rama 1.3)
            print("\n" + "=" * 60)
            print("Subes rápidamente a un árbol alto 🌲")
            print("El oso no puede alcanzarte y finalmente se va 🐻")
            print("Desde arriba ves luces a lo lejos 💡")
            print("\n¿Qué haces?")
            print("Opciones: ESPERAR A QUE AMANEZCA, BAJAR Y BUSCAR LAS LUCES, GRITAR PIDIENDO AYUDA")
            
            respuesta = input("\nTu elección: ").lower().strip()
            
            if respuesta == "esperar a que amanezca" or respuesta == "esperar":
                print("\n" + "=" * 60)
                print("Esperas en el árbol hasta el amanecer 🌅")
                print("Con la luz del día, encuentras fácilmente el camino a casa 🏠")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            elif respuesta == "bajar y buscar las luces" or respuesta == "bajar":
                print("\n" + "=" * 60)
                print("Bajas y caminas hacia las luces 🚶‍♂️")
                print("Encuentras un campamento de excursionistas 🏕️")
                print("Te ayudan y te llevan de vuelta a la civilización 🤝")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            elif respuesta == "gritar pidiendo ayuda" or respuesta == "gritar":
                print("\n" + "=" * 60)
                print("Gritas pidiendo ayuda 🗣️")
                print("Un grupo de guardabosques te escucha y viene a rescatarte 👮‍♂️")
                print("¡Estás a salvo!")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            else:
                print("\nOpción no válida. La aventura termina aquí.")
        else:
            print("\nOpción no válida. La aventura termina aquí.")
            
    elif respuesta == "esconderte":
        # Segundo nivel de decisión (rama 2)
        print("\n" + "=" * 60)
        print("Te escondes detrás de un árbol grande 🌳")
        print("El oso pasa de largo sin verte 👀")
        print("Escuchas un ruido extraño detrás de ti...")
        print("\n¿Qué haces?")
        print("Opciones: INVESTIGAR EL RUIDO, QUEDARTE ESCONDIDO, SALIR CORRIENDO")
        
        respuesta = input("\nTu elección: ").lower().strip()
        
        if respuesta == "investigar el ruido" or respuesta == "investigar":
            # Tercer nivel de decisión (rama 2.1)
            print("\n" + "=" * 60)
            print("Investigas y encuentras un zorro herido 🦊")
            print("\n¿Qué haces?")
            print("Opciones: AYUDAR AL ZORRO, DEJARLO, BUSCAR AYUDA")
            
            respuesta = input("\nTu elección: ").lower().strip()
            
            if respuesta == "ayudar al zorro" or respuesta == "ayudar":
                print("\n" + "=" * 60)
                print("Ayudas al zorro y él te guía a un camino seguro 🦊➡️")
                print("Resulta ser un espíritu del bosque que te recompensa con buena suerte 🍀")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            elif respuesta == "dejarlo":
                print("\n" + "=" * 60)
                print("Decides no involucrarte y continuar tu camino")
                print("Te pierdes en el bosque por varias horas 🌲")
                print("Finalmente encuentras salida al anochecer 🌙")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            elif respuesta == "buscar ayuda":
                print("\n" + "=" * 60)
                print("Buscas ayuda y encuentras un guardabosques 👨‍✈️")
                print("Juntos ayudan al zorro y él te guía fuera del bosque")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            else:
                print("\nOpción no válida. La aventura termina aquí.")
                
        elif respuesta == "quedarte escondido" or respuesta == "quedarte":
            print("\n" + "=" * 60)
            print("Te quedas escondido hasta que amanece 🌅")
            print("Con la luz del día, el bosque parece menos amenazador")
            print("Encuentras el camino a casa sin problemas 🏡")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        elif respuesta == "salir corriendo" or respuesta == "salir":
            print("\n" + "=" * 60)
            print("Sales corriendo y tropiezas con una raíz 🌳")
            print("Te lastimas el pie, pero logras llegar a un camino 🚶‍♂️")
            print("Un automovilista te ve y te lleva al pueblo 🚗")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        else:
            print("\nOpción no válida. La aventura termina aquí.")
            
    elif respuesta == "quedarte quieto":
        # Segundo nivel de decisión (rama 3)
        print("\n" + "=" * 60)
        print("Te quedas completamente quieto 🧍‍♂️")
        print("El oso te huele pero decide no atacarte 🐻👃")
        print("Se aleja lentamente...")
        print("Encuentras un objeto brillante en el suelo 💎")
        print("\n¿Qué haces?")
        print("Opciones: RECOGER EL OBJETO, IGNORARLO, EXAMINARLO CON CUIDADO")
        
        respuesta = input("\nTu elección: ").lower().strip()
        
        if respuesta == "recoger el objeto" or respuesta == "recoger":
            print("\n" + "=" * 60)
            print("Es una piedra preciosa mágica que brilla en la oscuridad 💎✨")
            print("Con su luz, encuentras fácilmente el camino a casa 🏡")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        elif respuesta == "ignorarlo":
            print("\n" + "=" * 60)
            print("Decides ignorarlo y continuar tu camino")
            print("Te pierdes un poco más pero finalmente sales del bosque 🌲")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        elif respuesta == "examinarlo con cuidado" or respuesta == "examinar":
            print("\n" + "=" * 60)
            print("Al examinarlo, descubres que es una brújula mágica 🧭✨")
            print("Siempre apunta hacia el lugar más seguro")
            print("Te guía directamente a la salida del bosque 🚶‍♂️➡️")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        else:
            print("\nOpción no válida. La aventura termina aquí.")
    else:
        print("\nOpción no válida. La aventura termina aquí.")
        
elif respuesta == "linterna":
    print("\n" + "=" * 60)
    print("Enciendes la linterna 💡 y ves un camino iluminado.")
    print("De pronto, oyes algo entre los árboles 🌿.")
    print("\n¿Qué haces?")
    print("Opciones: SEGUIR EL CAMINO, BUSCAR ENTRE LOS ÁRBOLES, APAGAR LA LINTERNA Y ESCONDERSE")
    
    respuesta = input("\nTu elección: ").lower().strip()
    
    if respuesta == "seguir el camino" or respuesta == "seguir":
        # Segundo nivel de decisión (rama 4)
        print("\n" + "=" * 60)
        print("Sigues el camino iluminado 🛤️")
        print("Llegas a un claro con un estanque brillante 💧✨")
        print("\n¿Qué haces?")
        print("Opciones: BEBER DEL ESTANQUE, REFLEJARTE EN EL AGUA, RODEAR EL ESTANQUE")
        
        respuesta = input("\nTu elección: ").lower().strip()
        
        if respuesta == "beber del estanque" or respuesta == "beber":
            # Tercer nivel de decisión (rama 4.1)
            print("\n" + "=" * 60)
            print("El agua es mágica y te da visión nocturna 🥽🌙")
            print("Ahora puedes ver perfectamente en la oscuridad")
            print("Encuentras fácilmente la salida del bosque 🚶‍♂️")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        elif respuesta == "reflejarte en el agua" or respuesta == "reflejarte":
            # Tercer nivel de decisión (rama 4.2)
            print("\n" + "=" * 60)
            print("Al reflejarte, ves un mensaje en el agua: 'Sigue la luz de la luna' 🌕")
            print("Sigues la luz lunar y encuentras un sendero secreto 🛤️")
            print("Te lleva directamente a la civilización 🏘️")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        elif respuesta == "rodear el estanque" or respuesta == "rodear":
            # Tercer nivel de decisión (rama 4.3)
            print("\n" + "=" * 60)
            print("Al rodear el estanque, encuentras una barca pequeña 🚣‍♂️")
            print("\n¿Qué haces?")
            print("Opciones: USAR LA BARCA, IGNORARLA, EXAMINARLA")
            
            respuesta = input("\nTu elección: ").lower().strip()
            
            if respuesta == "usar la barca" or respuesta == "usar":
                print("\n" + "=" * 60)
                print("Navegas por el estanque y llegas a la otra orilla 🚣‍♂️")
                print("Encuentras una cabaña con gente amable que te ayuda 🛖")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            elif respuesta == "ignorarla":
                print("\n" + "=" * 60)
                print("Ignoras la barca y continúas caminando 🚶‍♂️")
                print("Después de algunas horas, encuentras un camino familiar 🛣️")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            elif respuesta == "examinarla":
                print("\n" + "=" * 60)
                print("Al examinarla, encuentras un mapa debajo del asiento 🗺️")
                print("El mapa te muestra una ruta segura fuera del bosque 🗺️➡️")
                print("¡FIN DE LA AVENTURA!")
                print("=" * 60)
            else:
                print("\nOpción no válida. La aventura termina aquí.")
        else:
            print("\nOpción no válida. La aventura termina aquí.")
            
    elif respuesta == "buscar entre los árboles" or respuesta == "buscar":
        # Segundo nivel de decisión (rama 5)
        print("\n" + "=" * 60)
        print("Buscas entre los árboles y encuentras un cervatillo perdido 🦌")
        print("Parece asustado y solo 😢")
        print("\n¿Qué haces?")
        print("Opciones: AYUDAR AL CERVATILLO, DEJARLO, LLAMAR A SU MADRE")
        
        respuesta = input("\nTu elección: ").lower().strip()
        
        if respuesta == "ayudar al cervatillo" or respuesta == "ayudar":
            print("\n" + "=" * 60)
            print("Ayudas al cervatillo y su madre aparece para agradecerte 🦌❤️")
            print("La manada de ciervos te guía fuera del bosque 🦌➡️")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        elif respuesta == "dejarlo":
            print("\n" + "=" * 60)
            print("Decides no interferir y continúas tu camino")
            print("Te sientes culpable y te pierdes en el bosque 😔")
            print("Finalmente encuentras salida al amanecer 🌅")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        elif respuesta == "llamar a su madre":
            print("\n" + "=" * 60)
            print("Llamas suavemente y la madre cierva aparece 🦌")
            print("Ella te mira con gratitud y te muestra un camino seguro 🛤️")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        else:
            print("\nOpción no válida. La aventura termina aquí.")
            
    elif respuesta == "apagar la linterna y esconderse" or respuesta == "apagar":
        # Segundo nivel de decisión (rama 6)
        print("\n" + "=" * 60)
        print("Apagas la linterna y te escondes en la oscuridad 🌑")
        print("Escuchas pasos acercándose... 👣")
        print("\n¿Qué haces?")
        print("Opciones: ENCENDER LA LINTERNA, QUEDARTE QUIETO, HABLAR SUAVEMENTE")
        
        respuesta = input("\nTu elección: ").lower().strip()
        
        if respuesta == "encender la linterna" or respuesta == "encender":
            print("\n" + "=" * 60)
            print("Al encenderla, ves a otro excursionista perdido 👨‍🦯")
            print("Juntos encuentran el camino a casa más fácilmente 🤝")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        elif respuesta == "quedarte quieto":
            print("\n" + "=" * 60)
            print("Te quedas quieto y los pasos se alejan 🚶‍♂️")
            print("Esperas un rato y luego encuentras un camino iluminado por la luna 🌕")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        elif respuesta == "hablar suavemente":
            print("\n" + "=" * 60)
            print("Hablas suavemente: '¿Hay alguien ahí?' 🗣️")
            print("Una voz amigable responde: '¡Yo también estoy perdido!'")
            print("Se unen y juntos encuentran la salida 🧑‍🤝‍🧑")
            print("¡FIN DE LA AVENTURA!")
            print("=" * 60)
        else:
            print("\nOpción no válida. La aventura termina aquí.")
    else:
        print("\nOpción no válida. La aventura termina aquí.")
else:
    print("\nOpción no válida. Debes elegir entre FÓSFORO o LINTERNA.")

print("\n¡Gracias por jugar! Vuelve pronto para nuevas aventuras! 🎮✨")