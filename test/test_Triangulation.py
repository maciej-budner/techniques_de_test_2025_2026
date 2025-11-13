import unittest
import pytest
import time
from unittest.mock import patch
from scr.triangulation import getResultFromAPI, calculeTriangulation, recuperePointBDD, dessigneResulta

@pytest.mark.integration
def test_IntegrationAPIConnectionEchouer(self):
    listPoint = [(0, 0),(1, 0),(0, 1)]
    resulta = getResultFromAPI(listPoint)
    resultaAttendu = None
    
    self.assertEqual(resultaAttendu, resulta)

@pytest.mark.unit_test
@patch("scr.triangulator.yaml.safe_load", return_value={"calculeResult": [[(0,0), (1,0), (0,1)],[(1,0), (0,1), (1,1)]]})
def test_CalculeTriangulationAPartirDe4PointValide(self, mock_yaml):
    listPoint = [(0, 0),(1, 0),(0, 1),(1, 1)]
    resulta = calculeTriangulation(listPoint)
    resultaAttendu = [[(0,0), (1,0), (0,1)],[(1,0), (0,1), (1,1)]]
    
    self.assertEqual(resultaAttendu, resulta)

@pytest.mark.unit_test
@patch("scr.triangulator.yaml.safe_load", return_value={"calculeResult": [[(0,0), (1,0), (0,1)]]})
def test_CalculeTriangulationAPartirDe3PointValide(self, mock_yaml):
    listPoint = [(0, 0),(1, 0),(0, 1)]
    resulta = calculeTriangulation(listPoint)
    resultaAttendu = [[(0,0), (1,0), (0,1)]]
    
    self.assertEqual(resultaAttendu, resulta)


@pytest.mark.integration
def test_IntegrationCalculeTriangulationAPartirDe4PointValide(self):
    listPoint = [(0, 0),(1, 0),(0, 1),(1, 1)]
    resulta = calculeTriangulation(listPoint)
    resultaAttendu = [[(0,0), (1,0), (0,1)],[(1,0), (0,1), (1,1)]]
    
    self.assertEqual(resultaAttendu, resulta)

@pytest.mark.integration
def test_IntegrationCalculeTriangulationAPartirDe3PointValide(self):
    listPoint = [(0, 0),(1, 0),(0, 1)]
    resulta = calculeTriangulation(listPoint)
    resultaAttendu = [[(0,0), (1,0), (0,1)]]
    
    self.assertEqual(resultaAttendu, resulta)

@pytest.mark.unit_test
def test_CalculeTriangulationAPartirDe2PointDansLeTable(self):
    listPoint = [(0, 0),(1, 0)]
    resulta = calculeTriangulation(listPoint)
    resultaAttendu = None#"ValueErreur: on atteint une liste de 3 point minimum"
    
    self.assertEqual(resultaAttendu, resulta)

@pytest.mark.unit_test
def test_CalculeTriangulationAPartirDe1PointDansLeTable(self):
    listPoint = [(0, 0)]
    resulta = calculeTriangulation(listPoint)
    resultaAttendu = None#"ValueErreur: on atteint une liste de 3 point minimum"
    
    self.assertEqual(resultaAttendu, resulta)

@pytest.mark.unit_test
def test_CalculeTriangulationAPartirDePointVide(self):
    listPoint = []
    resulta = calculeTriangulation(listPoint)
    resultaAttendu = None#"ValueErreur: on atteint une liste de 3 point minimum"
    
    self.assertEqual(resultaAttendu, resulta)

@pytest.mark.unit_test
def test_ErreurCalculeTriangulation3pointIdentique(self):
    listPoint = [(0, 0),(0, 0),(0, 0)]
    resulta = calculeTriangulation(listPoint)
    resultaAttendu = None#"ValueErreur: on doit avoir 3 point différent minimum"
    
    self.assertEqual(resultaAttendu, resulta)

@pytest.mark.unit_test
def test_ErreurCalculeTriangulation2pointIdentique(self):
    listPoint = [(0, 0),(0, 0),(0, 1)]
    resulta = calculeTriangulation(listPoint)
    resultaAttendu = None#"ValueErreur: on doit avoir 3 point différent minimum"
    
    self.assertEqual(resultaAttendu, resulta)


@pytest.mark.integration
def test_IntegrationRecupereListePointBDDSuccess(self):
    pointId=1
    listPoint = recuperePointBDD(pointId)
    resultaAttendu = [(0, 0),(1, 0),(0, 1),(1, 1)]
    self.assertEqual(resultaAttendu, listPoint)


@pytest.mark.integration
def test_IntegrationRecupereListePointBDDNonExistante(self):
    pointId=0 #0 car la bdd créera jamais un id 0, il commence toujour par 1
    listePoint = recuperePointBDD(pointId)
    resultaAttendu = []
    self.assertEqual(resultaAttendu, listePoint)


@pytest.mark.integration
def test_IntegrationErreurConnectionBDD(self):
    pointId=1
    listPoint = recuperePointBDD(pointId)
    resultaAttendu = None
    self.assertEqual(resultaAttendu, listPoint)

#def testDependanceAvecPointSetManager(self):
    #pas besoin de le faire car les test de recuperation de liste point font comme si c'etait un teste de dependance

@pytest.mark.performance
def test_CalculTriangulationlLargeData():
    listPoint = [(0, 0),(1, 0),(0, 1),(1, 1),(2, 1),(1, 2),(2, 2),(2, 0),(0, 2),(0, 3),(3, 0),(1, 3),(3, 3),(3,1),(2, 3),(3,2)]
    start = time.perf_counter()
    result = calculeTriangulation(listPoint)
    end = time.perf_counter()
    print(f"Triangulation took {end - start:.4f} seconds")
    assert result is not None

@pytest.mark.performance
def test_RealisationGraphLargeData():
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
    