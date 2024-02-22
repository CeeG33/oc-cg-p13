- ![Static Badge](https://img.shields.io/badge/P13%20Mettez%20%C3%A0%20l'%C3%A9chelle%20une%20application%20Django%20en%20utilisant%20une%20architecture%20modulaire-blue?label=Projet)
- ![Static Badge](https://img.shields.io/badge/Ciran_G%C3%9CRB%C3%9CZ-darkgreen?label=Auteur)

## Orange County Lettings : site web de location de biens immobiliers (English version down below)

Site web d'Orange County Lettings.

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
- `python -m venv env`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source env/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source env/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source env/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source env/bin/activate`
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

- Pour activer l'environnement virtuel, `.\env\Scripts\Activate.ps1` 
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

## Documentation

Vous pouvez consulter la documentation du site en vous rendant sur le lien suivant : [https://oc-cg-p13.readthedocs.io/](https://oc-cg-p13.readthedocs.io/)

______________________________________

## Orange County Lettings : Real Estate Rental Website

Orange County Lettings' website.

## Local Development

### Prerequisites

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

Throughout the documentation for local development, it is assumed that the python command in your OS shell runs the Python interpreter mentioned above (unless a virtual environment is activated).

### macOS / Linux

#### Clone the repository

- `cd /path/to/put/project/in`.
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`.

#### Create a virtual environment

- `cd /path/to/Python-OC-Lettings-FR`.
- `python -m venv env`.
- `apt-get install python3-venv` (If the previous step encounters errors with a package not found on Ubuntu).
- Activate the environment with `source env/bin/activate`.
- Confirm that the `python` command runs the Python interpreter in the virtual environment with 
`which python`.
- Confirm that the version of the Python interpreter is 3.6 or higher with `python --version`.
- Confirm that the `pip` command runs the pip executable in the virtual environment with `which pip`.
- To deactivate the environment, use the `deactivate` command.

#### Run the site

- `cd /path/to/Python-OC-Lettings-FR`
- `source env/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000` in a browser.
- Confirm that the site is working, and navigation is possible (you should see several profiles and lettings).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source env/bin/activate`
- `flake8`

#### Unit Tests

- `cd /path/to/Python-OC-Lettings-FR`
- `source env/bin/activate`
- `pytest`

#### Database

- `cd /path/to/Python-OC-Lettings-FR`
- Open a shell session with `sqlite3`
- Connect to the database `.open oc-lettings-site.sqlite3`
- Display tables in the database `.tables`
- Display columns in the profiles table, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Run a query on the profiles table, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` to exit

#### Site Administration Interface

- Go to `http://localhost:8000/admin`
- Log in with the user `admin`, password `Abc1234!`

### Windows

Use PowerShell, as above except:

- To activate the virtual environment, `.\env\Scripts\Activate.ps1` 
- Replace `which <my-command>` with `(Get-Command <my-command>).Path`

## Deployment

Deployment is the process that will automate putting the site into production with each commit to the master branch of the repository. 
With each commit to the master branch, the following steps are automatically performed using a CI/CD pipeline:

- Recreation of the local development environment.
- Code formatting check (Linting).
- Execution of the test suite implemented with the code.
- Verification that the test coverage is above 80%.
- Containerization of the application via Docker. Image generated, pushed to Docker Hub.
- Deployment of the site to the AWS hosting provider.

### Prerequisites

- GitHub account with read access to this repository.
- Docker Hub account.
- Sentry account with a pre-configured project.
- AWS account with the ability to launch EC2 instances.

### Configure Deployment

- On AWS, create an EC2 instance under Amazon Linux. During this step, be sure to create a key pair and download and store the generated .pem file on your local hard drive in a safe location.
- Still on AWS, add the following incoming rule to the default security group (launch-wizard-1) of the newly created EC2:
```Version IP : IPv4 | Type : TCP personnalisé | Protocole : TCP | Plage de ports : 8000 | Source : 0.0.0.0/0```
- Launch the EC2 instance.
- On GitHub, add the following environment variables (secrets) by going to ```Settings > Secrets and variables > Actions``` and clicking ```New repository secret```:
```
APP_SECRET_KEY >> Secret key of the Django application.
DOCKERHUB_USERNAME >> Docker Hub account username.
DOCKERHUB_PASSWORD >> Docker Hub account password.
SENTRY_DSN >> Sentry logging DSN link.
EC2_HOST >> Public IPv4 DNS obtained after launching the EC2 instance (example: ec2-54-159-98-184.compute-1.amazonaws.com).
EC2_USERNAME >> ec2-user
EC2_SECRET_KEY >> Contents of the .pem file generated during EC2 instance creation.
```
- Test the successful deployment of the site after committing to the main branch of the repository.

## Documentation

You can view the site's documentation by visiting the following link: [https://oc-cg-p13.readthedocs.io/](https://oc-cg-p13.readthedocs.io/)
