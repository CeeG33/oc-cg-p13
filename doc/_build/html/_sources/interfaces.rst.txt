Interfaces de programmation
===========================

URLs de l'application
---------------------

Les différents URLs du site sont les suivantes :

- ``/`` : Page d'accueil du site.
- ``lettings/`` : Liste des locations.
- ``lettings/<letting_id>/`` : Page détaillée d'une location.
- ``profiles/`` : Liste des profils utilisateurs.
- ``profiles/<username>/`` : Page détaillée d'un profil utilisateur.
- ``admin/`` : Interface de gestion administrateur du site.

Architecture de développement
-----------------------------

Le code source est divisé en trois applications distinctes :

- **oc_lettings_site** : Dossier de configuration globale. Centralise les URLs.
- **profiles** : Dossier de développement du modèle Profile.
- **lettings** : Dossier de développement du modèle Letting.
