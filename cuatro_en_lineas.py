class Juego():
    def __init__(self):
        self.tablero = [[" " for i in range(8)] for i in range(8)] 
        self.jugador = True
        self.ficha = "x"
        self.jugando = True
        self.error = False

    def cambiar_jugador(self):
        if self.jugador == True:
            self.jugador = False 
            self.ficha = "o"
        else:
            self.jugador = True
            self.ficha = "x"

    def ingresar_ficha(self,columna):
            self.pongo_ficha(columna)
            if self.ganador():
                return True
            else:
                self.cambiar_jugador()
                
    def pongo_ficha(self, columna):
        posicion = 0
        sig_posicion = 1
        final = 7

        for index in self.tablero:
            if self.tablero[final][columna] == " ":
                self.tablero[final][columna] = self.ficha
                return self.tablero 
            if self.tablero[posicion][columna] == " " and self.tablero[sig_posicion][columna] != " ":
                self.tablero[posicion][columna] = self.ficha
                return self.tablero
            posicion += 1
            sig_posicion += 1
        

    def ganador_fila(self):
        #filas
        completado = False
        columna = 0
        pasar_filas = 0
        while pasar_filas < 8:
            for index in self.tablero[pasar_filas]:
                if self.tablero[pasar_filas][columna] == "x" and self.tablero[pasar_filas][columna + 1] == "x" and self.tablero[pasar_filas][columna + 2] == "x" and self.tablero[pasar_filas][columna + 3] == "x":
                    completado = True
                    return completado
                if self.tablero[pasar_filas][columna] == "o" and self.tablero[pasar_filas][columna + 1] == "o" and self.tablero[pasar_filas][columna + 2] == "o" and self.tablero[pasar_filas][columna + 3] == "o":
                    completado = True
                    return completado
                if columna == 4:
                    columna = 0
                    break
                columna += 1
            pasar_filas += 1
        if completado == False:
            return False


    def ganador_columna(self):
        #columnas
        completado = False
        fila = 0
        pasar_columnas = 0
        while pasar_columnas < 8:
            for index in self.tablero:
                if self.tablero[fila][pasar_columnas] == "x" and self.tablero[fila+1][pasar_columnas] == "x" and self.tablero[fila+2][pasar_columnas] == "x" and self.tablero[fila+3][pasar_columnas] == "x":
                    completado = True
                    return completado
                if self.tablero[fila][pasar_columnas] == "o" and self.tablero[fila+1][pasar_columnas] == "o" and self.tablero[fila+2][pasar_columnas] == "o" and self.tablero[fila+3][pasar_columnas] == "o":
                    completado = True
                    return completado
                if fila == 4:
                    fila = 0
                    break

                fila +=1
            pasar_columnas +=1
        
        if completado == False:
            return False

    def ganador_diagonal_abajo(self):
        #diagonal_abajo
        completado = False
        fila = 7
        columna = 7
        while fila >= 0:
            for i in self.tablero:
                if self.tablero[fila][columna] == "x" and self.tablero[fila-1][columna-1] == "x" and self.tablero[fila-2][columna-2] == "x" and self.tablero[fila-3][columna-3] == "x":
                    completado = True
                    return completado
                if self.tablero[fila][columna] == "o" and self.tablero[fila-1][columna-1] == "o" and self.tablero[fila-2][columna-2] == "o" and self.tablero[fila-3][columna-3] == "o":
                    completado = True
                    return completado
                if columna == 3:
                    columna = 7
                    break
                columna -= 1
            fila -= 1

        if completado == False:
            return False

    def ganador_diagonal_arriba(self):
        #diagonal_arriba
        completado = False
        fila = 7
        columna = 0
        while fila >= 0:
            for index in self.tablero:
                if self.tablero[fila][columna] == "x" and self.tablero[fila-1][columna+1] == "x" and self.tablero[fila-2][columna+2] == "x" and self.tablero[fila-3][columna+3] == "x":
                    completado = True
                    return completado
                if self.tablero[fila][columna] == "o" and self.tablero[fila-1][columna+1] == "o" and self.tablero[fila-2][columna+2] == "o" and self.tablero[fila-3][columna+3] == "o":
                    completado = True
                    return completado
                if columna == 4:
                    columna = 0
                    break
                columna += 1
            fila -= 1
            
        if completado == False:
            return False
        
    def ganador(self):
        if self.ganador_columna():
            return True
        elif self.ganador_fila():
            return True
        elif self.ganador_diagonal_arriba():
            return True
        elif self.ganador_diagonal_abajo():
            return True
        else:
            return False

def main():
    juego = Juego()
    print("Vamos a jugar al 4 en linea!!")
    for fila in juego.tablero:
        print(fila) 
    while juego.jugando:
        columna = int(input("Ingrese la columna entre el 1 y el 8 para ingresar la ficha: "))
        juego.error = False
        while juego.error == False:
            if columna > 8 or columna < 1:
                print("Columna incorrecta! Vuelve a ingresar")
                columna = int(input("Ingrese la columna para ingresar la ficha: "))
            elif juego.tablero[0][columna-1] == "x" or juego.tablero[0][columna-1] == "o":
                print("Columna llena!! Vuelva a ingresar")
                columna = int(input("Ingrese la columna para ingresar la ficha: "))
            else:
                juego.error = True
        juego.ingresar_ficha(columna-1)
        for fila in juego.tablero:
            print(fila)

        if juego.ganador() == True:
            if juego.jugador == False:
                juego.jugador = input("Ingrese nombre de usuario: ")
            else:
                juego.jugador = input("Ingrese nombre de usuario: ")

            if juego.ganador_columna() == True:
                print("Has hecho 4 en linea en columna!!")
            
            if juego.ganador_fila() == True:
                print("Has hecho 4 en linea en fila!!")
            
            if juego.ganador_diagonal_abajo() == True:
                print("Has hecho 4 en linea en diagonal!!")
            
            if juego.ganador_diagonal_arriba() == True:
                print("Has hecho 4 en linea en diagonal!!")

            print(f"Felicidades has ganado! {juego.jugador.upper()}")
            juego.jugando = False
    
    print("Gracias por jugar! \n Desea seguir jugando? \n Escriba SI si quieres seguir jugando \n Escriba NO para salir!")
    eleccion = input("")
    finalizar = False
    while finalizar == False:
        if eleccion.lower() == "si":
            finalizar = True
            main()
        elif eleccion.lower() == "no":
            print("Adios")
            finalizar = True
        else:
            print("Has ingresado incorrectamente la respuesta!!")
            print("Desea seguir jugando? \n Escriba SI si quieres seguir jugando \n Escriba NO para salir!")
            eleccion = input("")

if __name__ == '__main__':
    main()
            
        
