# IUT BUT 2 DEV WEB
# TPI Flask Dev web

Groupe : Nathan Randriantsoa et Clemence Bocquet *TD2B*

# Table des matières
- Lien GitHub
- Lancement application
- Fonctionnalités implémentées


## Lien GitHub
<https://github.com/Kyxtaka/IUTFlaskTp1>

## Lancement application
Pour lancer un environnement virtuel, vous devez, depuis VSCode : 
### Si un .venv/venv se trouve dans le projet 
> Ouvrir le projet à sa racine, lancer la commande **source venv/bin/activate**  
> Avant le prompt, un (.venv) doit être affiché affirmant que vous avez bien activé votre environnement virtuel  

### Si il n'y a pas de .venv/venv ou qu'il y a des difficultés à activer le venv
> Sur VSCode, ouvrir le projet à sa racine  
> Aller dans tuto>app.py  
> Sélectionner un interpréteur (en bas à droite à côté de "Python")  
> Cliquer sur "créer un environnement virtuel" puis "Venv", "supprimer et recreer" et choisir l'interpréteur python  
> Prendre requirement.txt pour les dépendances à  installer  

### Ou bien installation d'un venv via l'interpreteur de commandes (CMD)
> Ouvrez un un shell dans le repertoire racine du project
> Taper la commande `python3 -m venv /path/to/new/virtual/environment` si vous avez la version 3 de python sinon `python3 -m venv /path/to/new/virtual/environment`, une fois le venv de crée veillez l'activer (commande ci-dessus)

### Installation des dépendence 
> Dans le répertoire racine du projet il y a un fichier `requirements.txt`, tourjours dans le shell et avec le venv d'activé taper la commande `pip install -r path/to/requirements.txt`. Une fois les dépendences d'installées, vous pouvez lancez l'application.

Pour lancer l'application après avoir activé votre environnement virtuel, depuis VSCode :
### Lancer l'application
> Vous pouvez lancer l'application avec **flask run**  
> Ouvrir la page depuis le lien donné (Running on http://127.0...)

### Import données
> **flask loaddb tuto/data.yml**

### Création tables de la base de données
> **flask syncdb tuto/data.yml**

### Créer un utilisateur
> **flask newuser nomUser mdpUser**

### Modifier un mot de passe utilisateur
> **flask passwd nomUser nouveauMdpUser**

## Fonctionnalités implementées
- afficher les livres et leurs détails
- intégration à Bootstrap
- Edition/Ajout d'auteurs
- Recherche des livres par auteur
- commande d'import des données (loaddb)
- commande de création des tables (syncdb)
- login (commandes newuser, password) avec limitation des pages d’édition aux utilisateurs authentifiés.
- création d’une table Genres (non alimentée)
- ajout d’une relation ManyToMany et modification de la BD en conséquence avec les livres favoris par utilisateur
- possibilité d’avoir des favoris par utilisateur
- noter les livres et afficher la note moyenne sur le détail d’un livre
