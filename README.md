## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Le déploiement est le processus qui va s'occuper de mettre le site en production de façon automatisée à chaque commit sur la branche master du repository.
Lors de chaque commit sur la branche master, les étapes suivantes se réalisent automatiquement à l'aide d'une pipeline CI /CD :

- Reproduction de l'environnement de développement local.
- Vérification du formattage du code (Linting).
- Déclenchement de la suite de tests implantée avec le code.
- Vérification que la couverture de test est bien supérieure à 80%.
- Conteneurisation de l'application via Docker. Image générée, pushée sur Docker Hub.
- Mise en service du site chez l'hébergeur AWS.

### Prérequis

- Compte GitHub avec accès en lecture à ce repository.
- Compte Docker Hub.
- Compte Sentry avec un projet déjà configuré.
- Compte AWS avec possibilité de lancer des instances EC2.

### Configurer le déploiement

- Sur AWS, créer une instance EC2 sous Amazon Linux. Durant cette étape, il faut bien veiller à créer une paire de clés puis télécharger et stocker le fichier .pem généré dans un endroit sécurisé sur votre disque dur local.
- Toujours sur AWS, ajouter la règle entrante suivante dans le groupe de sécurité par défaut (launch-wizard-1) de l'EC2 fraîchement créé :
```Version IP : IPv4 | Type : TCP personnalisé | Protocole : TCP | Plage de ports : 8000 | Source : 0.0.0.0/0```
- Lancer l'instance EC2.
- Sur GitHub, ajouter les variables d'environnement (secrets) suivants en allant dans la section ```Settings > Secrets and variables > Actions``` et en cliquant sur ```New repository secret```:
```
APP_SECRET_KEY >> Clé secrète de l'application Django.
DOCKERHUB_USERNAME >> Identifiant du compte Docker Hub.
DOCKERHUB_PASSWORD >> Mot de passe du compte Docker Hub.
SENTRY_DSN >> Lien de rattachement DSN à la journalisation Sentry.
EC2_HOST >> DNS IPv4 public obtenue après lancement de l'instance EC2 (exemple : ec2-54-159-98-184.compute-1.amazonaws.com).
EC2_USERNAME >> ec2-user
EC2_SECRET_KEY >> Contenu du fichier .pem généré lors de la création de l'instance EC2.
```
- Tester le bon déploiement du site après avoir réalisé un commit sur la branche principale du repository.
