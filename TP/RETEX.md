# Se que j'ai mal fait
J'ai mal comprit à quoi server les fichier '.yaml'. Je pensais que c'était un fichier qui faisait office d'api mais il servais juste a décrire les résultats possible. Donc je ne les ai pas mock comme il faut, il fallait les utiliser comme une simulation de connection api qui peut sortir une des erreur (200, 502, etc).
Ensuite, dans mon plan d'action, j'ai donné les cas général de se qui fallait tester, alors que le mieux serai de décrire tout les test à réaliser donc les unitest, test integration, test performance, test avec erreur, sans erreur avec plusieurs model de sortie.
Et enfin, j'ai eux du mal à écrire la docstring, même si j'ai regarder un model pour le faire, je savais pas que pour ruff check si il manque une ponctuation ou majuscule, pour lui c'est une erreur et j'ai eux du mal a trouver une telle erreur car pour moi tout était bon

# Se que j'ai bien fait
Malgré que j'ai pas bien décrit tout les test que je devais réaliser, je trouve que j'ai bien réaliser tout les teste que je pouvais faire, pour tester le bon fonctionnement du code.

# Se que je ferait à l'avenir
A l'avenir, je décrirai mieux ma stratégie de test, je consacrerais plus de temps pour savoir si des mock sont possible et je commencerai directement a écrire la docstring, pour gagner du temps. Et enfin, je ferais attention a la longueur de mon code pour satisfaire le ruff check et pour que sa soit plus visible

# Ruff check fichier 
Si je fait un ruff check sur le fichier des test, il me sort que les nom de mes fonction sont trop long et qui n'a pas de docsting.
Sauf que en ma apprit que un fichier test n'a pas besoin de commentaire tout doit être dit sur le nom de la fonction.
Donc je n'est pas rajouter de docstring et n'y changer de nom de ma fonction.  
De plus, quand je fait un ruff check sur le fichier triangulation.py, il me sort erreur "Import block is un-sorted or-formatted" sur l'import du PointSetManage.py, qui est fait car j'arrive pas a faire de bon mock. Mais je comprend pas comment corriger cela.

# Retour sur le projet
Je trouve que l'exercice est plutôt compliqué, car c'est difficile de savoir quelle fonction il y aura dans ta class et se quelle va sortir, surtout quand tu doit de concentré que sur une seul classe. Généralement je préfère écrire mes class avec se quelle vont sortie puis tester avec la méthode Green, red et Refactor.
Mais se qui est intéressant, c'est que une fois que tes test sont fait, tu sais se que tu doit faire et donc tu avance un peu plus vite.
Donc si tu arrive a visualiser ta boite noir sur le projet, il est plus préférable de commencer par les tests pour avancer plus vite sur le code et faire le contraire si c'est pas le cas, mais faudra directement écrire un test des que une fonction est écrite.