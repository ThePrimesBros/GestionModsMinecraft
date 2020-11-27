# GestionModsMinecraft

Ceci est une application Django qui permet de récupérer une liste de mods du jeux Minecraft.

Pour ce faire, ils nous a fallu en premier temps savoir ce que nous voulions récupérer et faire entrer dans la base de données.
Nou savons alors repérer les élément suivant :

- Le nom de mods
- Le créateur
- La version du mods
- La description du mods
- Le liens de téléchargement
- L'image du mods

Avec ces informations, il était ainsi possible d'afficher correctement les mods. En effet, un mods possède un nom, un créateur, une version unique, une description, et enfin pour l'affichage général, une image pour illustrer le mod.
Cependant, un créateur de mods peut en avoir crée plusieur, et une version peut avoir plusieur mods aussi.
Nous avons pas la suite donc décider des trié les mods par version, ils est alors possible de voir l'intégralité des mods, en ordre alphabétique, mais aussi de les trié par version de jeux que l'on souhaite.


Pour ce qui est de l'environement global du site, nous avons les pages suivantes :

- La page d'accueil, qui répertorie tous les mods, avec pour chaque mods, une card. Sur cette même pages, il est possible de lancer un scrappe pour récupérer les données des mods, et ainsi mettre à jour les mods déjà en base. On peut aussi à partir de cette page, choisir les mods à afficher en fonction de la version.

- La page d'ajout, qui permet d'ajouter un mods manuellement, si le site en question ne le possèdent pas.

- La page de modification, qui permet de modifier les données d'un mods, même si avec le scrap, celle-ci se mettent à jour automatiquement.

Voila pour ce qui est de l'interface en général.

Installation:
Django version 3.1.3

pip install -r requirements.txt
npm install

Mettre le dossier nodes_modules dans le dossier static

Test:
Les fichiers se trouvent dans le dossier mods/tests
python testNewMod.py | testRoutes.py | testServer.py 