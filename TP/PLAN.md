# TODO
Dans le projet il nous decrit que nous avant 2 class PointSetManager et Triangulator. Nous avant aussi 2 autre classe PointSet et Triangle mais pour elles, je comprend pas pourquoi PointSet n'est pas juste un PointSetManager et donc lui laisser de gerer la même chose que PointSet. De plus, ces 2 classe je ne voie pas de test à faire car pour moi il y a que un setter et getter dans ces classe. Et enfin, nous avant une base de donner pour stocker les points

Les Test que je voie a réaliser seront:
- de tester la connection a la BDD
- tester si on recupére bien la requête API
- si on a une interface faudra tester l'envoie de requete du client
- Pour la classe PointSetManager:
  - tester l'enregistrement du nouveau ensemble de point ?(pas sur pour celle là)
- pour la Classe Triangulation:
- - tester le calcule de la triangulation des ensembles de point
  - tester la recupération des ensemble de point au près du PointSetManager
  - tester si la classe Triangulation et PointSetManager si elle sont dépendante

# Pourquoi ces tests
Comme dit précèdament, même si dans le sujet on parle de classe PointSet et Triangle, j'ai pas besoin de tester si c'est que des getter/setter.

La connection a la BDD est obligatoire vue que on doit la manipuler.

Faut tester aussi si la requête API fonction car c'est grâce a cette API que on va calculer la triangulation.

Je ne sais pas si il faut tester l'envoie de la requete du client car j'ignore si elle se fera via un terminale, donc pas besoin de tester, ou via une interface, dans le quelle cas faudra tester si la requete s'envoie bien pour ne pas perdre des donné.

la Class PointSetManager aura 1 tests peut-être, car tester l'envoie du pointId pour la classe Traingulation c'est triangulation qui va tester ça et pour le client c'est visuelle donc on n'a pas besoin, mais je ne suis pas sur si je doit tester si l'enrigistement dans la BDD est utille car sa risque de créer des donnés, non souhaité, dans la BDD.

La Class Triangulation aura plusieur tests. Il aura un test de calcule de triangulation pour voir si la fonction qui calcule ça marche convenablement, puis, on doit tester si on récupére bien le PointId que PointSetManager doit donner. Et enfin, on doit tester si les classe Triangulation et pointSetManager on une dépendance, pour être sur qu'elle fonctionne entre elle.
