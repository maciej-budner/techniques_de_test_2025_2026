# Installer les dépendances
install:
    pip install -r requirements.txt

# Installer les dépendances developpeur
install_dev:
    pip install -r dev_requirements.txt

#lance tous les tests
test:
	pytest .\test\test_Triangulation.py

#lance tous les tests sauf les tests de performance et integration
unit_test:
	pytest -m unit_test

#lance tous les tests sauf les tests de performance et unit_test
integration:
	pytest -m integration

#lance uniquement les tests de performance et integration
perf_test:
	pytest -m performan

#génère un rapport de couverture de code 
coverage:
	coverage run -m pytest test

#valide la qualité de code
lint:
	ruff check scr/triangulation.py 

#génère la documentation en HTML
doc:
	pdoc3 -w scr.triangulation.py test.test_Triangulation