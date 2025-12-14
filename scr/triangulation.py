"""Module de triangulation.

Ce module gère les opérations liées à la triangulation.
"""

import math
from scr.PointSetManage import PointSetManage
class Triangulation:
    """Gère les opérations liées à la triangulation.
    
    la class possede toute les fonction qui nous permet 
    de realiser une triangulation et avoir un aspect visuel
    """

    def __init__(self):
        """Inisialise la class.

        Pour notre cas,
        elle sert juste pour uttiliser ces fonction.
        """
        pass

    def getResultFromAPI(self, listPoint):
        """Organise les points et génère une triangulation.

        Cette fonction nous permettra d'avoir une
        liste de triangles qui permettra
        de designer les figures.

        Parameters
        ----------
        listPoint : tableau de Point
            Liste des points à trianguler.

        Returns
        -------
        liste de Point

        """
        minx = min(x for x,y in listPoint)
        maxx = max(x for x,y in listPoint)
        miny = min(y for x,y in listPoint)
        maxy = max(y for x,y in listPoint)

        dx = maxx - minx
        dy = maxy - miny
        delta = max(dx, dy) * 10

        p1 = (minx - delta, miny - delta)
        p2 = (minx + 2*delta, miny - delta)
        p3 = (minx - delta, miny + 2*delta)

        triangles = [(p1, p2, p3)]

        for point in listPoint:
            triangleIncorecte = []
            for partieTriangle in triangles:
                (ax, ay), (bx, by), (cx, cy) = partieTriangle
                d = 2 * (ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
                if d == 0:
                    center, radius = None, None, float("inf")
                else:
                    ux = ((ax*ax + ay*ay)*(by-cy) + 
                          (bx*bx + by*by)*(cy-ay) + 
                          (cx*cx + cy*cy)*(ay-by)) / d
                    uy = ((ax*ax + ay*ay)*(cx-bx) + 
                          (bx*bx + by*by)*(ax-cx) + 
                          (cx*cx + cy*cy)*(bx-ax)) / d

                    r = math.dist((ux, uy), (ax, ay))
                    
                    center, radius = (ux, uy), r
                if center is None:
                    continue
                if math.dist(point, center) < radius:
                    triangleIncorecte.append(partieTriangle)

            boundary = []
            for partieTriangle in triangleIncorecte:
                for edge in [(partieTriangle[0], partieTriangle[1]), 
                             (partieTriangle[1], partieTriangle[2]), 
                             (partieTriangle[2], partieTriangle[0])]:
                    if not any(edge == (e[1], e[0]) for b in triangleIncorecte for e in 
                               [(b[0], b[1]), (b[1], b[2]), (b[2], b[0])]):
                        boundary.append(edge)

            for partieTriangle in triangleIncorecte:
                triangles.remove(partieTriangle)

            for edge in boundary:
                triangles.append((edge[0], edge[1], point))

        #renplie notre resulta avec la composition de triangle
        resulta = []
        for partgeo in triangles:
            if p1 not in partgeo and p2 not in partgeo and p3 not in partgeo:
                resulta.append(partgeo)

        return resulta


    #Fonction qui return Tout les triangle possible avec une liste de point donner
    #si cette liste de point a minimum 3 point et minimum 3 point diferent entre elle
    def calculeTriangulation(self, listPoint):
        """Vérifie si la list de Point valide, et return resulta.

        Cette fonction verifie :
        si la list est plus grande ou egale a 3.
        Si parmit cette list il y a assez de point
        non doublonner pour realiser une triangulation
        Si c'est le cas, renvoie une matrix de point.
        sinon, renvoie None.

        Parameters
        ----------
        listPoint : tableau de Point
            Liste des points à trianguler.

        Returns
        -------
        liste de Point
            si tout les test sont bon
        None
            sinon

        """
        if(len(listPoint) < 3):
            print("ValueErreur: on atteint une liste de 3 point minimum")
            return None
        else:
            listSansDoublant = set(listPoint)
            #si le nombre de point identique est inferieur a de qui est tolérer 
            # on peut continuer sinon erreur
            if(len(listPoint) -len(listSansDoublant) <= len(listPoint) -3):
                #-3 car on attent au moins 3 point identique
                #on peut faire les triangle
                toutLesTriangle = self.getResultFromAPI(listPoint)
                if(toutLesTriangle is not None):
                    return toutLesTriangle
                else:
                    print("Erreur API:une erreur est survenue lors de l'appel de l'api")
                    return None
            else:
                print("ValueErreur: on doit avoir 3 point différent minimum")
                return None

    def recuperePointBDD(self, pointId):
        """Appel la class PointSetManage, get donner de la BDD.

        Cette fonction fait juste un appel.

        Parameters
        ----------
        pointId : int
            Identifiant du point à récupérer.

        Returns
        -------
        tableau de Point

        """
        appelBdd = PointSetManage()
        return appelBdd.recupéreListePoint(pointId)
        
    def dessigneResulta(self, resulta):
        """Designe dans un svg, notre figure.

        Cette fonction nous permetra de designer
        tout nos triangle.

        Parameters
        ----------
        resulta : liste de Point
            Liste des triangles à dessiner.

        Returns
        -------
        bool

        """
        filename="triangulation.svg"
        width, height = 800, 800
        minx, maxx = -10, 10
        miny, maxy = -10, 10
        svg=[f'<svg xmlns="http://www.w3.org/2000/svg"width="{width}"height="{height}">']

        def scale(p):
            x = (p[0] - minx) / (maxx - minx) * (width - 40) + 20
            y = (p[1] - miny) / (maxy - miny) * (height - 40) + 20
            return x, height - y
        # Dessiner triangles
        for tri in resulta:
            pts = [scale(p) for p in tri]
            points_str = " ".join(f"{x},{y}" for x, y in pts)
            svg.append(
                f'<polygon points="{points_str}" fill="none" stroke="blue" '
                'stroke-width="2"/>'
            )
        points_set = set()
        for tri in resulta:
            for p in tri:
                points_set.add(p)

        for p in points_set:
            x, y = scale(p)
            svg.append(f'<circle cx="{x}" cy="{y}" r="5" fill="red"/>')
        svg.append("</svg>")

        with open(filename, "w") as f:
            f.write("\n".join(svg))

        print(f"SVG généré : {filename}")
        return True #tout c'est bien passer
    

#pour tester
#triangle = Triangulation()


#print(triangle.calculeTriangulation([(0, 0),(1, 0),(0, 1)]))
#triangle.dessigneResulta(
#    triangle.calculeTriangulation(
#        [(0, 0),(1, -1),(1, 1),(1, 0),(2, 0),(2, -1),(2, 1),(3, 0)]))