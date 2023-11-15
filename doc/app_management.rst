Déploiement et gestion de l'application
=======================================
Déploiement
-----------

Le déploiement est le processus qui va s'occuper de mettre le site en 
production de façon automatisée à chaque commit sur la branche master du repository. 
Lors de chaque commit sur la branche master, les étapes suivantes se réalisent 
automatiquement à l'aide d'une pipeline CI / CD :

- Reproduction de l'environnement de développement local.
- Vérification du formatage du code (Linting).
- Déclenchement de la suite de tests implantée avec le code.
- Vérification de la couverture de test (doit supérieure à 80%).
- Conteneurisation de l'application via Docker. Image générée, pushée sur Docker Hub.
- Mise en service du site chez l'hébergeur AWS.

Pré-requis
++++++++++

- Compte GitHub avec accès en lecture à ce repository.

- Compte Docker Hub.

- Compte Sentry avec un projet déjà configuré.

- Compte AWS avec possibilité de lancer des instances EC2.

Configurer le déploiement
+++++++++++++++++++++++++

- Sur AWS, créer une instance EC2 sous Amazon Linux. 
  Durant cette étape, il faut bien veiller à créer une paire de clés 
  puis télécharger et stocker le fichier .pem généré dans un endroit 
  sécurisé sur votre disque dur local.

- Toujours sur AWS, ajouter la règle entrante suivante dans le groupe 
  de sécurité par défaut (launch-wizard-1) de l'EC2 fraîchement créé :
  ``Version IP : IPv4 | Type : TCP personnalisé | 
  Protocole : TCP | Plage de ports : 8000 | Source : 0.0.0.0/0``

- Lancer l'instance EC2.

- Sur GitHub, ajouter les variables d'environnement (secrets) suivants 
  en allant dans la section ``Settings > Secrets and variables > Actions`` 
  et en cliquant sur ``New repository secret``:
  
  - ``APP_SECRET_KEY`` : Clé secrète de l'application Django.
  - ``DOCKERHUB_USERNAME`` : Identifiant du compte Docker Hub.
  - ``DOCKERHUB_PASSWORD`` : Mot de passe du compte Docker Hub.
  - ``SENTRY_DSN`` : Lien de rattachement DSN à la journalisation Sentry.
  - ``EC2_HOST`` : DNS IPv4 public obtenue après lancement de l'instance EC2 
    (exemple : ec2-54-159-98-184.compute-1.amazonaws.com).
  - ``EC2_USERNAME`` : ec2-user
  - ``EC2_SECRET_KEY`` : Contenu du fichier .pem généré lors de la création 
    de l'instance EC2.

- Tester le bon déploiement du site après avoir réalisé un commit sur 
  la branche principale du repository.

Gestion de l'application
------------------------

Accès à l'interface d'administration
++++++++++++++++++++++++++++++++++++

Veuillez vous rendre sur l'URL suivant :

- ``http://<adresse-ip-publique-fournie-par-l'hébergeur>:8000/admin/``

  - Exemple : `http://54.159.98.184:8000/admin/ 
    <http://54.159.98.184:8000/admin/>`_

Connectez-vous avec les informations suivantes :

- Login : admin
- Mot de passe : Abc1234!

Ajout d'un objet
::::::::::::::::

- Une fois connecté sur l'interface d'administration, veuillez cliquer 
  sur le bouton ``Add`` en face du type de modèle que vous souhaitez ajouter.
- Remplissez le formulaire.
- Cliquez sur le bouton ``SAVE``.

Modification d'un objet
:::::::::::::::::::::::

- Une fois connecté sur l'interface d'administration, veuillez cliquer 
  sur le bouton ``Change`` en face du type de modèle que vous souhaitez modifier.
- Cliquez sur l'objet à modifier.
- Remplissez le formulaire.
- Cliquez sur le bouton ``SAVE``.

Suppression d'un objet
::::::::::::::::::::::

- Une fois connecté sur l'interface d'administration, veuillez cliquer 
  sur le bouton ``Change`` en face du type de modèle que vous souhaitez supprimer.
- Cliquez sur l'objet à supprimer.
- Cliquez sur le bouton ``Delete``.
- Confirmez votre choix en cliquant sur le bouton ``Yes, I'm sure``.

Journalisation
--------------

Une journalisation a été mise en place en utilisant Sentry. Celle-ci renvoie 
les erreurs et exceptions levées (erreurs 404 & 500, …) lors de l'utilisation 
du site par un utilisateur.

Base de données
---------------

Les données du site sont stockées sur un fichier SQLite nommé 
``oc-lettings-site.sqlite3``. Il s'agit d'une solution temporaire en attendant 
une utilisation plus accrue du site qui justifierait l'adoption d'une technologie 
plus adaptée.