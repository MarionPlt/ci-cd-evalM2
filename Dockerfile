# Utilise une image officielle de Python
FROM python:3.9-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers du projet dans le conteneur
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définit la commande par défaut pour démarrer l'application
CMD ["python", "src/main.py"]