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

- **Nom 1** (vous)
- **Nom 2** (coéquipier)
- **Nom 3** (coéquipier, si applicable)

> Mettez à jour cette liste avec les noms des membres de votre groupe.

---

## 2. URL du dépôt

Le projet est disponible sur GitHub :  
[**GitHub - Guess The Word**](https://github.com/VotreCompte/guess-the-word)

> Remplacez l’URL ci-dessus par l’URL réelle de votre dépôt public GitHub.

---

## 3. Description du projet

**Guess the Word** est un mini-jeu en Python. Son but est simple : l’utilisateur doit deviner le mot secret.  
- Le mot par défaut est `angular`.  
- Si l’utilisateur entre `angular`, le jeu confirme que la réponse est correcte.  
- Pour toute autre réponse, le jeu indique que la réponse est incorrecte.

### Arborescence principale

- `src/main.py` : contient la fonction principale `guess_the_word` et le code d’exécution.  
- `tests/test_main.py` : contient les tests unitaires pour valider la fonction `guess_the_word`.  
- `requirements.txt` : liste les dépendances (flake8 et pytest).  
- `Dockerfile` : fichier de configuration pour la création de l’image Docker.  
- `setup.py` (optionnel) : un script d’installation (si besoin).  
- `.github/workflows/CI-CD.yml` : le fichier GitHub Actions définissant notre pipeline CI/CD.  

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
# 1. Créer et activer un environnement virtuel (optionnel, mais recommandé)
python3 -m venv venv
source venv/bin/activate

# 2. Mettre à jour pip et installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt

# 3. Lint
flake8 .

# 4. Build (compile check)
python -m compileall .

# 5. Tests
pytest tests
```
Si toutes ces étapes réussissent en local, alors votre PR devrait passer le CI sans problème.
