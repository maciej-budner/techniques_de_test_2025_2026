import unittest
import pytest
import time
from unittest.mock import patch
from scr.triangulation import Triangulation


@pytest.mark.integration
def test_IntegrationAPIConnectionEchouer():
    listPoint = [(0, 0),(1, 0),(0, 1)]
    obj = Triangulation()
    resulta = obj.getResultFromAPI(listPoint)
    resultaAttendu = None
    
    assert resultaAttendu== resulta

@pytest.mark.unit_test
@patch("scr.triangulation.yaml.safe_load", return_value={"calculeResult": [[(0,0), (1,0), (0,1)],[(1,0), (0,1), (1,1)]]})
def test_CalculeTriangulationAPartirDe4PointValide(mock_safe_load):
    listPoint = [(0, 0),(1, 0),(0, 1),(1, 1)]
    obj = Triangulation()
    resulta = obj.calculeTriangulation(listPoint)
    resultaAttendu = [[(0,0), (1,0), (0,1)],[(1,0), (0,1), (1,1)]]
    
    assert resultaAttendu== resulta

@pytest.mark.unit_test
@patch("scr.triangulation.yaml.safe_load", return_value={"calculeResult": [[(0,0), (1,0), (0,1)]]})
def test_CalculeTriangulationAPartirDe3PointValide(mock_safe_load):
    listPoint = [(0, 0),(1, 0),(0, 1)]
    obj = Triangulation()
    resulta = obj.calculeTriangulation(listPoint)
    resultaAttendu = [[(0,0), (1,0), (0,1)]]
    
    assert resultaAttendu== resulta


@pytest.mark.integration
def test_IntegrationCalculeTriangulationAPartirDe4PointValide():
    listPoint = [(0, 0),(1, 0),(0, 1),(1, 1)]
    obj = Triangulation()
    resulta = obj.calculeTriangulation(listPoint)
    resultaAttendu = [[(0,0), (1,0), (0,1)],[(1,0), (0,1), (1,1)]]
    
    assert resultaAttendu== resulta

@pytest.mark.integration
def test_IntegrationCalculeTriangulationAPartirDe3PointValide():
    listPoint = [(0, 0),(1, 0),(0, 1)]
    obj = Triangulation()
    resulta = obj.calculeTriangulation(listPoint)
    resultaAttendu = [[(0,0), (1,0), (0,1)]]
    
    assert resultaAttendu== resulta

@pytest.mark.unit_test
def test_CalculeTriangulationAPartirDe2PointDansLeTable():
    listPoint = [(0, 0),(1, 0)]
    obj = Triangulation()
    resulta = obj.calculeTriangulation(listPoint)
    resultaAttendu = None#"ValueErreur: on atteint une liste de 3 point minimum"
    
    assert resultaAttendu== resulta

@pytest.mark.unit_test
def test_CalculeTriangulationAPartirDe1PointDansLeTable():
    listPoint = [(0, 0)]
    obj = Triangulation()
    resulta = obj.calculeTriangulation(listPoint)
    resultaAttendu = None#"ValueErreur: on atteint une liste de 3 point minimum"
    
    assert resultaAttendu== resulta

@pytest.mark.unit_test
def test_CalculeTriangulationAPartirDePointVide():
    listPoint = []
    obj = Triangulation()
    resulta = obj.calculeTriangulation(listPoint)
    resultaAttendu = None#"ValueErreur: on atteint une liste de 3 point minimum"
    
    assert resultaAttendu== resulta

@pytest.mark.unit_test
def test_ErreurCalculeTriangulation3pointIdentique():
    listPoint = [(0, 0),(0, 0),(0, 0)]
    obj = Triangulation()
    resulta = obj.calculeTriangulation(listPoint)
    resultaAttendu = None#"ValueErreur: on doit avoir 3 point différent minimum"
    
    assert resultaAttendu== resulta

@pytest.mark.unit_test
def test_ErreurCalculeTriangulation2pointIdentique():
    listPoint = [(0, 0),(0, 0),(0, 1)]
    obj = Triangulation()
    resulta = obj.calculeTriangulation(listPoint)
    resultaAttendu = None#"ValueErreur: on doit avoir 3 point différent minimum"
    
    assert resultaAttendu== resulta


@pytest.mark.integration
def test_IntegrationRecupereListePointBDDSuccess():
    pointId=1
    obj = Triangulation()
    listPoint = obj.recuperePointBDD(pointId)
    resultaAttendu = [(0, 0),(1, 0),(0, 1),(1, 1)]
    assert resultaAttendu== listPoint


@pytest.mark.integration
def test_IntegrationRecupereListePointBDDNonExistante():
    pointId=0 #0 car la bdd créera jamais un id 0, il commence toujour par 1
    obj = Triangulation()
    listPoint = obj.recuperePointBDD(pointId)
    resultaAttendu = []
    assert resultaAttendu== listPoint


@pytest.mark.integration
def test_IntegrationErreurConnectionBDD():
    pointId=1
    obj = Triangulation()
    listPoint = obj.recuperePointBDD(pointId)
    resultaAttendu = None
    assert resultaAttendu== listPoint

#def testDependanceAvecPointSetManager(self):
    #pas besoin de le faire car les test de recuperation de liste point font comme si c'etait un teste de dependance

@pytest.mark.performance
def test_CalculTriangulationlLargeData():
    listPoint = [(0, 0),(1, 0),(0, 1),(1, 1),(2, 1),(1, 2),(2, 2),(2, 0),(0, 2),(0, 3),(3, 0),(1, 3),(3, 3),(3,1),(2, 3),(3,2)]
    start = time.perf_counter()
    obj = Triangulation()
    result = obj.calculeTriangulation(listPoint)
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
    obj = Triangulation()
    start = time.perf_counter()
    result = obj.dessigneResulta(resulta)
    end = time.perf_counter()
    print(f"Dessiner les triangle sa a prit {end - start:.4f} seconds")
    assert result is not None


if __name__ == '__main__':
    unittest.main()
    