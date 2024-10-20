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


Pour lancer l'application après avoir activé votre environnement virtuel, depuis VSCode :
### Lancer l'application
> Vous pouvez lancer l'application avec **flask run**
> Ouvrir depuis le lien donné

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
