
class PointSetManage:
    """class imaginaire juste pour que triangulation marche"""
    def __init__(self):
        """
        inisialise la class.

        Pour notre cas, 
        elle sert juste pour uttiliser ces fonction.       
        """
        pass

    def recupéreListePoint(self, idPoint):
        """c'est une BDD Imaginaire avec un appel Imaginaire

        Cette fonction possaide que 3 possibilité:
        soit idPoint =1, alors en a une donner dans la BDD
        soit idPoint =0, la donner existe pas
        soit idPoint>1, erreur de la bdd
        
        Parameters
        ----------
        pointId : it

        Returns
        -------
        tableau de Point or None
        """
        if idPoint == 1:
            return [(0, 0),(1, 0),(0, 1),(1, 1)]
        elif idPoint == 0:
            return []
        else:
            return None