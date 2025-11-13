# Installer les dépendances
install:
    pip install -r requirement.txt

# Installer les dépendances developpeur
install_dev:
    pip install -r dev_requirement.txt

#lance tous les tests
test:
	pytest .\test\test_Triangulation.py

#lance tous les tests sauf les tests de performance 
unit_test:
	pytest -m unit_test

#lance uniquement les tests de performance
perf_test:
	pytest -m performan

#génère un rapport de couverture de code 
coverage:
	coverage run -m pytest

#valide la qualité de code
lint:
	ruff check

#génère la documentation en HTML
doc:
	pdoc3 .\main\Triangulation.py