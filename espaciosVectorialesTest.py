import unittest
import espaciosVectoriales as es
import numpy as np

class TeststringMethods(unittest.TestCase):

    def test_sumvector(self):
        a = np.array([complex(1, 5), complex(2, 8)])
        b = np.array([complex(1, 3), complex(1, -2)])
        c = np.array([(2+8j), (3+6j)])
        self.assertTrue(np.array_equal(es.suma_vec(a, b), c))

    def test_inversevec(self):
        a = np.array([complex(5, 5), complex(6, 9)])
        b = np.array([(-5-5j), (-6-9j)])
        self.assertTrue(np.array_equal(es.inversoVec(a), b))

    def test_kporVector(self):
        a = np.array([complex(2, 3), complex(9, 9)])
        k = 2
        b = np.array([(4+6j), (18+18j)])
        self.assertTrue(np.array_equal(es.mult_escalar_vec(k, a), b))

    def test_sumaMatrix(self):
        a = np.array([[complex(3, 4), complex(4, 3)], [complex(1, 2), complex(5, 6)]])
        b = np.array([[complex(10, 4), complex(7, 2)], [complex(-1, -2), complex(7, 7)]])
        c = np.array([[complex(13,8), complex(11,5)], [complex(0,0), complex(12,13)]])
        self.assertTrue(np.array_equal(es.sumMatriz(a, b), c))

    def test_inverseMatrix(self):
        a = np.array([[complex(3, 4), complex(4, 3)], [complex(1, 2), complex(5, 6)]])
        b = np.array([[complex(-3, -4), complex(-4, -3)], [complex(-1, -2), complex(-5, -6)]])
        self.assertTrue(np.array_equal(es.inversoMatriz(a), b))

    def test_kpormatrix(self):
        a = np.array([[complex(13, 8), complex(11, 5)], [complex(0, 0), complex(12, 13)]])
        k = 7
        b = np.array([[(91+56j), (77+35j)], [0j, (84+91j)]])
        self.assertTrue(np.array_equal(es.mult_escalar_matriz(k, a), b))

    def test_transpuesta(self):
        a = np.array([[complex(-83,54), complex(91,35)], [complex(-9,-9), complex(10,12)]])
        b = np.array([[(-83+54j), (-9-9j)], [(91+35j), (10+12j)]])
        self.assertTrue(np.array_equal(es.transpuesta(a), b))

    def test_conjugada(self):
        a = [[(17, 34), (-9, 9)], [(1, 1), (7, 7)]]
        b = [['17-34j', '-9-9j'], ['1-1j', '7-7j']]
        self.assertTrue(np.array_equal(es.conjugada(a), b))

    def test_adjunta(self):
        a = np.array([[0,0,4], [0,3,0], [2,0,0]])
        b = np.array([[0, 0, -6], [0, -8, 0], [-12, 0, 0]])
        self.assertTrue(np.array_equal(es.adjunta(a), b))

    def test_multMatrix(self):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[-1, 12], [5, 7]])
        c = np.array([[9, 26], [17, 64]])
        self.assertTrue(np.array_equal(es.multiplicar(a, b), c))

    def test_accionMatrix(self):
        a = np.array([[5, 2], [5, 4]])
        b = np.array([[1, 2]])
        c = np.array([9, 13])
        self.assertTrue(np.array_equal(es.accion(a, b), c))

    def test_productoInterno(self):
        a = ([(1, 0), (0, 1), (1, -3)])
        b = np.array([complex(2, 1), complex(0, 1), complex(2, 0)])
        c = (5+7j)
        self.assertTrue(np.array_equal(es.productoInterno(a, b), c))

    def test_norma(self):
        a = np.array([(1,2), (3,4)])
        b = 5.477225575051661
        self.assertTrue(np.array_equal(es.norma(a), b))

    def test_distancia(self):
        a = np.array([(1, 3), (2, 5)])
        b = np.array([(5, 3), (7, 7)])
        c = 6.708203932499369
        self.assertTrue(np.array_equal(es.distancia(a,b), c))

    def test_unitaria(self):
        a = np.array([[complex(1,1), complex(0,0)], [complex(0,0),complex(0,1)]]).all()
        self.assertTrue(a == False)

    def test_hermitiana(self):
        a = np.array([[complex(1,1), complex(0,0)], [complex(0,0),complex(0,1)]]).all()
        self.assertTrue(a == False)

    def test_tensor(self):
        a = np.array([[1, 0, 9], [0, 1, 3], [0, 2, 1]])
        b = np.array([[1, 2], [5, 6]])
        c = np.array([[1, 2, 0, 0, 9, 18], [5, 6, 0, 0, 45, 54], [0, 0, 1, 2, 3, 6], [0, 0, 5, 6, 15, 18], [0, 0, 2, 4, 1, 2], [0, 0, 10, 12, 5, 6]])
        self.assertTrue(np.array_equal(es.productoTensor(a,b), c))



if __name__ == '__main__':
    unittest.main()
