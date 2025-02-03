# Guess the Word

Ce projet consiste en un jeu minimaliste "Guess the Word". Il intègre une chaîne d'intégration continue (CI) via GitHub Actions qui :
- Lint le code (avec flake8)
- Effectue une étape de « construction » (vérification de compilation)
- Lance les tests unitaires (avec pytest)

Le projet est structuré ainsi :
- `src/` : contient le code source.
- `tests/` : contient les tests unitaires.
- `.github/workflows/ci.yml` : définit le workflow GitHub Actions.
