# Se que j'ai mal fait
J'ai mal comprit à quoi server les fichier '.yaml'. Je pensais que c'était un fichier qui faisait office d'api mais il servais juste a décrire les résultats possible. Donc je les ai mock comme il faut, il fallait les utiliser comme une simulation de connection api qui peut sortir une des erreur (200, 502, etc).
Ensuite, dans mon plan d'action, j'ai donné les cas général de se qui fallait tester, alors que le mieux serai de décrire tout les test à réaliser donc les unitest, test integration, test performance, test avec erreur, sans erreur avec plusieurs model de sortie.
Et enfin, j'ai eux du mal à écrire la docstring, même si j'ai regarder un model pour le faire, je savais pas que pour ruff check si il manque une ponctuation c'est une erreur pour lui et j'ai eux du mal a trouver une telle erreur car pour moi tout était bon

# Se que j'ai bien fait
Malgré que j'ai pas bien décrit tout les test que je devais réaliser, je trouve que j'ai bien réaliser tout les teste que je pouvais faire, pour tester le bon fonctionnement du code.

# Se que je ferait à l'avenir
A l'avenir, je décrirai mieux ma stratégie de test, je consacrerais plus de temps pour savoir si des mock sont possible et je commencerai directement a écrire la docstring, pour gagner du temps. Et enfin, je ferais attention a la longueur de mon code pour satisfaire le ruff check et pour que sa soit plus visible

# Retour sur le projet
Je trouve que l'exercice est plutôt compliqué, car c'est difficile de savoir quelle fonction il y aura dans ta class et se quelle va sortir. Généralement je préfère écrire mes class avec se quelle vont sortie puis tester avec la méthode Green, red et Refactor.
Mais se qui est intéressant, c'est que une fois que tes test sont fait, tu sais se que tu doit faire et donc tu avance un peu plus vite.
Donc si tu arrive a faire ta boite noir sur le projet, il est plus préférable de commencer par les tests pour avancer plus vite sur le code et faire le contraire si c'est pas le cas.