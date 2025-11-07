import unittest
from unittest import mock, TestCase
import pytest
import time

class TriangulationTest(unittest.TestCase):
    
    def testCalculeTriangulationAPartirDePointValide(self):
        listPoint = [(0, 0),(1, 0),(0, 1),(1, 1)]
        resulta = calculeTriangulation(listPoint)
        resultaAttendu = [[(0,0), (1,0), (0,1)],[(1,0), (0,1), (1,1)]]
        
        self.assertEqual(resultaAttendu, resulta)
    
    def testCalculeTriangulationAPartirDePointInvalide(self):
        listPoint = [(0, 0),(1, 0)]
        resulta = calculeTriangulation(listPoint)
        resultaAttendu = "ValueErreur: on atteint une liste de 3 point minimum"
        
        self.assertEqual(resultaAttendu, resulta)
    
    def testCalculeTriangulationAPartirDePointVide(self):
        listPoint = []
        resulta = calculeTriangulation(listPoint)
        resultaAttendu = "ValueErreur: on atteint une liste de 3 point minimum"
        
        self.assertEqual(resultaAttendu, resulta)

    def testErreurCalculeTriangulation(self):
        listPoint = [(0, 0),(0, 0),(0, 0)]
        resulta = calculeTriangulation(listPoint)
        resultaAttendu = "ValueErreur: on doit avoir 3 point différent minimum"
        
        self.assertEqual(resultaAttendu, resulta)

    def testRecupereListePointBDDSuccess(self):
        pointId=1
        listPoint = recuperePointBDD(pointId)
        resultaAttendu = [(0, 0),(1, 0),(0, 1),(1, 1)]
        self.assertEqual(resultaAttendu, listPoint)

    def testRecupereListePointBDDNonExistante(self):
        pointId=0 #0 car la bdd créera jamais un id 0, il commence toujour par 1
        listePoint = recuperePointBDD(pointId)
        resultaAttendu = []
        self.assertEqual(resultaAttendu, listPoint)

    def testErreurConnectionBDD(self):
        pointId=1
        listPoint = recuperePointBDD(pointId)
        resultaAttendu = None
        self.assertEqual(resultaAttendu, listPoint)

    #def testDependanceAvecPointSetManager(self):
        #pas besoin de le faire car les test de recuperation de liste point font comme si c'etait un teste de dependance
    
    #TODO test de performence

    @pytest.mark.performance
    def testCalculTriangulationlLargeData():
        listPoint = [(0, 0),(1, 0),(0, 1),(1, 1),(2, 1),(1, 2),(2, 2),(2, 0),(0, 2),(0, 3),(3, 0),(1, 3),(3, 3),(3,1),(2, 3),(3,2)]
        start = time.perf_counter()
        result = calculeTriangulation(listPoint)
        end = time.perf_counter()
        print(f"Triangulation took {end - start:.4f} seconds")
        assert result is not None

    @pytest.mark.performance
    def testRealisationGraphLargeData():
        resulta = [
    [(0,0), (1,0), (0,1)],
    [(1,0), (0,1), (1,1)],
    [(0,0), (2,0), (0,2)],
    [(1,3), (3,1), (1,1)],
    [(2,3), (3,2), (2,2)],
    [(0,2), (2,0), (2,2)],
    [(1,1), (2,1), (1,2)],
    [(2,1), (3,0), (3,1)],
    [(1,2), (2,2), (1,3)],
    [(2,2), (3,1), (2,3)],
    [(0,3), (1,2), (0,2)],
    [(3,0), (3,1), (2,0)],
    [(2,0), (3,1), (2,1)],
    [(0,1), (1,1), (0,2)],
    [(1,1), (2,2), (1,2)],
    [(2,2), (3,2), (2,3)]]
    
    start = time.perf_counter()
    result = dessigneResulta(resulta)
    end = time.perf_counter()
    print(f"Dessiner les triangle sa a prit {end - start:.4f} seconds")
    assert result is not None


if __name__ == '__main__':
    unittest.main()
    