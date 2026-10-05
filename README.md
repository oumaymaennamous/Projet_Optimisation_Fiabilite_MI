# Optimisation et fiabilité des installations industrielles

Projet de machine learning pour explorer les données de capteurs industriels, étudier les causes de panne et estimer le risque de défaillance d'une machine.

Le travail est présenté dans un notebook Jupyter. Il comprend l'analyse exploratoire, l'entraînement et l'évaluation de modèles, ainsi qu'une proposition de maintenance préventive. Une API FastAPI de prédiction est également définie dans le notebook.

## Contenu du dépôt

| Fichier | Description |
| --- | --- |
| `Projet_Optimisation_Fiabilité_ML.ipynb` | Analyse, modélisation et code de l'API FastAPI |
| `dataset.csv` | Données de surveillance des machines |
| `model_random_forest.joblib` | Modèle Random Forest entraîné |
| `preprocessing_pipeline.joblib` | Prétraitement utilisé par le modèle |
| `test.py` | Client de test qui appelle `POST /predict` sur `127.0.0.1:8000` |
| `requirements.txt` | Dépendances Python du projet |

Le jeu de données est associé à la compétition Kaggle [Binary Classification of Machine Failures](https://www.kaggle.com/competitions/playground-series-s3e17/data).

## Installation

Depuis le dossier du projet, créez et activez un environnement virtuel :

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Si PowerShell bloque l'activation, ouvrez une nouvelle invite de commandes et utilisez `.venv\Scripts\activate.bat`.

## Utilisation

Ouvrez `Projet_Optimisation_Fiabilité_ML.ipynb` dans VS Code ou Jupyter, sélectionnez l'environnement virtuel comme noyau, puis exécutez les cellules dans l'ordre. Le notebook lit `dataset.csv` et charge les deux fichiers `.joblib` depuis le dossier courant.

Pour tester l'API, démarrez d'abord le serveur en exécutant la cellule de lancement FastAPI à la fin du notebook. L'API écoute sur `http://127.0.0.1:8000`; la documentation interactive est disponible sur `http://127.0.0.1:8000/docs`. Dans un second terminal, lancez :

```powershell
python test.py
```

`test.py` envoie un exemple de données au point d'entrée `POST /predict`. Le serveur doit donc déjà être actif.

## Alertes e-mail (facultatives)

Les alertes SMTP sont désactivées tant que les variables de configuration ne sont pas définies. Renseignez-les dans l'environnement avant de lancer le serveur :

```powershell
$env:SMTP_HOST = "sandbox.smtp.mailtrap.io"
$env:SMTP_PORT = "2525"
$env:SMTP_USER = "votre_utilisateur"
$env:SMTP_PASSWORD = "votre_mot_de_passe"
$env:SMTP_FROM_EMAIL = "expediteur@example.com"
$env:ALERT_EMAIL = "destinataire@example.com"
```

Ne commitez jamais de secrets ni de fichier `.env` contenant des identifiants. Les anciens identifiants présents dans le notebook ont été retirés; s'ils étaient réels, révoquez-les et générez-en de nouveaux.

## Données et artefacts

Le CSV contient des identifiants de produit, le type de machine, des mesures de température, de vitesse, de couple et d'usure, ainsi que des indicateurs de panne. Les fichiers `.joblib` sont nécessaires pour réutiliser le modèle sans le réentraîner. Ne chargez pas de fichiers `.joblib` provenant d'une source non fiable.

