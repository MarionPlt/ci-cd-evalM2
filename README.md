# Projet : Guess the Word

Bienvenue dans notre projet **Guess the Word** ! Ce document (README) décrit :

- Les noms des membres de l’équipe.
- L’objectif du projet et son fonctionnement.
- Le fonctionnement de notre pipeline d’Intégration Continue (CI).
- Le fonctionnement de notre pipeline de Déploiement Continu (CD sur la branche principale).
- Le fonctionnement de notre pipeline de Livraison Continue (CD lors de la création d’un tag Git).
- Le livrable généré (image Docker).
- Les étapes pour **Damien Duportal** et **Marion Playout** afin de déployer une nouvelle version pendant notre absence.

---

## 1. Équipe

- **Nom 1** Bastien OEUVRARD
- **Nom 2** Jérémy ROSSI

---

## 2. URL du dépôt

Le projet est disponible sur GitHub :  
[**GitHub - Guess The Word**](https://github.com/Sairkko/ci-cd-evalM2/tree/main)

---

## 3. Description du projet

**Guess the Word** est un mini-jeu en Python. Son but est simple : l’utilisateur doit deviner le mot secret.  
- Le mot par défaut est `angular`.  
- Si l’utilisateur entre `angular`, le jeu confirme que la réponse est correcte.  
- Pour toute autre réponse, le jeu indique que la réponse est incorrecte.

---

## 4. Intégration Continue (CI)

Notre pipeline d’Intégration Continue s’exécute **à chaque pull request** (PR) ouverte sur le dépôt.

### 4.1 Étapes du CI

1. **Checkout** : Récupération du code du dépôt GitHub.  
2. **Configuration de Python 3.9** : Installation de la version Python nécessaire.  
3. **Installation des dépendances** : `pip install -r requirements.txt`.  
4. **Lint** : Lancement de la commande `flake8 .` pour s’assurer que le code respecte les standards (PEP8).  
5. **Build (compile check)** : `python -m compileall .` pour vérifier que le code est compilable.  
6. **Tests unitaires** : `pytest tests` pour lancer tous les tests dans le répertoire `tests/`.

### 4.2 Vérification manuelle (pour l’auteur d’une PR)

Pour reproduire localement les étapes du CI avant de pousser votre code :

```bash
# 1. Mettre à jour pip et installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt

# 2. Lint
flake8 .

# 3. Build (compile check)
python -m compileall .

# 4. Tests
export PYTHONPATH=.
pytest tests
```
Si toutes ces étapes réussissent en local, alors votre PR devrait passer le CI sans problème.

---

## 5. Déploiement Continu (sur `main`)

Dès qu’un commit est poussé sur la branche `main` (via merge d’une PR approuvée), un **Déploiement Continu** est déclenché :

1. Le pipeline relance les **mêmes étapes que le CI** (lint, build, tests).  
2. **Construction de l’image Docker** avec la balise `latest`.  
3. **Push de l’image Docker** vers Docker Hub :  
   - Repository : [`sairkko/guess-the-word`](https://hub.docker.com/r/sairkko/guess-the-word)  
   - Tag : `latest`  

Ainsi, la version `latest` est toujours à jour avec l’état actuel de la branche `main`.

### 5.1 Exécuter l’image Docker

Pour exécuter l’application depuis l’image Docker la plus récente (tag `latest`) :

```bash
docker pull sairkko/guess-the-word:latest
docker run -it --rm sairkko/guess-the-word:latest
```
Le jeu se lancera alors dans votre terminal.

## 6. Livraison Continue (avec les tags)

Lorsqu’on crée **manuellement un tag** (par exemple `v2.0.3`) et qu’on le pousse sur GitHub, le pipeline de **Livraison Continue** se déclenche :

1. Le pipeline exécute encore une fois les étapes de CI (lint, build, tests).  
2. Construit l’image Docker en utilisant le tag Git (ex. `v2.0.3`).  
3. Publie cette image Docker avec la balise `v2.0.3` sur Docker Hub.  
4. (Bonus) Crée automatiquement une **release GitHub** (notes de release) associée au tag.

### 6.1 Exemple de création de tag et de push

```bash
# Création du tag
git tag v2.0.3

# Envoi du tag vers GitHub
git push origin v2.0.3
```

Après quelques minutes, votre pipeline GitHub Actions va :

- Construire et tester le projet.
- Construire l’image Docker sairkko/guess-the-word:v2.0.3.
- Pousser cette image sur Docker Hub.
- Créer une release GitHub visible sur la page “Releases” du dépôt [Release GitHub](https://github.com/Sairkko/ci-cd-evalM2/releases/tag/v2.0.3).

- ## 7. Procédure de déploiement pour Damien Duportal et Marion Playout ou autres stagiaires

Lorsque vous souhaitez mettre en production une nouvelle version, voici les **deux scénarios** possibles :

### 7.1 Scénario 1 : Déploiement continu sur `main` (version *latest*)

1. **S’assurer que la PR est prête** :  
   - Vérifiez que le CI passe et que la PR est approuvée.  
   - Mergez la PR vers `main`.  
2. **Attendre le déploiement** :  
   - GitHub Actions va lancer automatiquement la construction de l’image Docker avec le tag `latest`.  
   - Vous pouvez suivre la progression dans l’onglet “Actions” du dépôt.  
3. **Récupérer l’image (si besoin)** :  
   - `docker pull sairkko/guess-the-word:latest`

Aucune action manuelle supplémentaire n’est nécessaire. L’image `latest` est prête à être utilisée.

### 7.2 Scénario 2 : Livraison continue via un tag (version versionnée)

1. **Décider d’une nouvelle version** (ex. `v2.0.4`).  
2. **Créer et pousser le tag** depuis votre machine :  
 ```bash
   git tag v2.0.4
   git push origin v2.0.4
```
3. **Suivre la pipeline** dans l’onglet “Actions” :
La construction de l’image Docker avec le tag v2.0.4 sera lancée.
La release GitHub “v2.0.4” sera créée.

## 8. Dockerfile et Hadolint (bonus)

Nous avons fourni un [`Dockerfile`](./Dockerfile) simple qui :

1. Part de l’image `python:3.9-slim`.  
2. Installe les dépendances depuis `requirements.txt`.  
3. Définit la commande de lancement de l’application : `python src/main.py`.  

Pour valider ce `Dockerfile` via [Hadolint](https://github.com/hadolint/hadolint), exécutez :

```bash
hadolint Dockerfile
```
