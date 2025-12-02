import yaml

class Triangulation():
    def __init__(self):
        pass

    def getResultFromAPI(self, listPoint): 
        with open("triangulator.yml") as calculator:
            try:
                dataYaml = yaml.safe_load(calculator)
                path = dataYaml.get("paths",{})
                route = path.get("/triangulation/{pointSetId}", {})
                method = route.get("GET".lower(), {})
                toutTriangle = method.get("200", {}).get("centent", {})

                return toutTriangle
            except yaml.YAMLError as exc:
                print(exc)
        print("On n'a pas reussis a calculer les triangle")
        return None

    #Fonction qui return Tout les triangle possible avec une liste de point donner
    #si cette liste de point a minimum 3 point et minimum 3 point diferent entre elle
    def calculeTriangulation(self, listPoint): 
        if(len(listPoint) < 3):
            print("ValueErreur: on atteint une liste de 3 point minimum")
            return None
        else:
            listSansDoublant = listPoint.set()
            #si le nombre de point identique est inferieur a de qui est tolérer on peut continuer sinon erreur
            if(len(listPoint) -len(listSansDoublant) <= len(listPoint) -3):#-3 car on attent au moins 3 point identique
                #on peut faire les triangle
                toutLesTriangle = self.getResultFromAPI(listPoint)
                if(toutLesTriangle is not None):
                    return toutLesTriangle
                else:
                    print("Erreur API: une erreur est survenue lors de l'appel de l'api")
                    return None
            else:
                print("ValueErreur: on doit avoir 3 point différent minimum")
                return None

    def recuperePointBDD(self, pointId):
        return None
        
    def dessigneResulta(self, resulta):
        return None