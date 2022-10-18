import unittest
from cuatro_en_lineas import Juego

class testCuatroEnLinea(unittest.TestCase):
    
    def test_tablero(self):
        juego = Juego()
        self.assertEqual(len(juego.tablero), 8)
        self.assertEqual(len(juego.tablero[0]), 8)
    
    def test_cambiar_jugador(self):
        juego = Juego()
        juego.cambiar_jugador()
        self.assertEqual(juego.jugador, False)
        self.assertEqual(juego.ficha, "o")
        juego.cambiar_jugador()
        self.assertEqual(juego.jugador,True)
        self.assertEqual(juego.ficha ,"x")

    def test_ingresar_ficha(self):
        juego = Juego()
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(6)
        self.assertEqual(juego.tablero[7][3],"x")
        self.assertEqual(juego.tablero[7][5],"o")
        self.assertEqual(juego.tablero[7][6],"x")
        self.assertEqual(juego.tablero[6][6],"o")
    
    def test_ganador_columna(self):
        juego = Juego()
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(3)
        # for fila in juego.tablero:
        #     print(fila)
        self.assertEqual(juego.ganador_columna(), True)
    
    def test_ganador_fila(self):
        juego = Juego()
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(6)
        # for fila in juego.tablero:
        #     print(fila)
        self.assertEqual(juego.ganador_fila(),True)
    
    def test_ganador_diagonal_abajo(self):
        juego = Juego()
        juego.ingresar_ficha(3)#x
        juego.ingresar_ficha(3)#o
        juego.ingresar_ficha(3)#x
        juego.ingresar_ficha(3)#o
        juego.ingresar_ficha(4)#x
        juego.ingresar_ficha(4)#o
        juego.ingresar_ficha(5)#x
        juego.ingresar_ficha(4)#o
        juego.ingresar_ficha(7)#x
        juego.ingresar_ficha(5)#o
        juego.ingresar_ficha(7)#x
        juego.ingresar_ficha(6)#o
        # for fila in juego.tablero:
        #     print(fila)
        self.assertEqual(juego.ganador_diagonal_abajo(),True)

    def test_ganador_diagonal_arriba(self):
        juego = Juego()
        juego.ingresar_ficha(0)#x
        juego.ingresar_ficha(1)#o
        juego.ingresar_ficha(1)#x
        juego.ingresar_ficha(2)#o
        juego.ingresar_ficha(2)#x
        juego.ingresar_ficha(3)#o
        juego.ingresar_ficha(2)#x
        juego.ingresar_ficha(3)#o
        juego.ingresar_ficha(3)#x
        juego.ingresar_ficha(5)#o
        juego.ingresar_ficha(3)#x
        # for fila in juego.tablero:
        #     print(fila)
        self.assertEqual(juego.ganador_diagonal_arriba(),True)

    def test_ganador_columna2(self):
        juego = Juego()
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(3)
        # for fila in juego.tablero:
        #     print(fila)
        self.assertEqual(juego.ganador_columna(), True)
        self.assertEqual(juego.ganador_fila(), False)
        self.assertEqual(juego.ganador_diagonal_arriba(), False)
        self.assertEqual(juego.ganador_diagonal_abajo(), False)
    
    def test_ganador_fila2(self):
        juego = Juego()
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(3)
        # for fila in juego.tablero:
        #     print(fila)
        self.assertEqual(juego.ganador(),True)
        self.assertEqual(juego.ganador_columna(),False)
        self.assertEqual(juego.ganador_fila(),False)
        self.assertEqual(juego.ganador_diagonal_abajo(),False)
        self.assertEqual(juego.ganador_diagonal_arriba(),True)

    def test_ganador_diagonal_abajo2(self):
        juego = Juego()
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(0)
        # for fila in juego.tablero:
        #     print(fila)
        self.assertEqual(juego.ganador(),True)
        self.assertEqual(juego.ganador_columna(),False)
        self.assertEqual(juego.ganador_fila(),False)
        self.assertEqual(juego.ganador_diagonal_abajo(),True)
        self.assertEqual(juego.ganador_diagonal_arriba(),False)
    
    def test_diagonal_arriba2(self):
        juego = Juego()
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(0)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(3)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(2)
        juego.ingresar_ficha(4)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(5)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(6)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(7)
        juego.ingresar_ficha(1)
        juego.ingresar_ficha(7)
        self.assertEqual(juego.ganador(),True)
        self.assertEqual(juego.ganador_columna(),False)
        self.assertEqual(juego.ganador_fila(),False)
        self.assertEqual(juego.ganador_diagonal_abajo(),False)
        self.assertEqual(juego.ganador_diagonal_arriba(),True)
    
if __name__ == '__main__':
    unittest.main()