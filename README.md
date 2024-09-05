
# API Ontologie Irrigation
<div style="display: flex; justify-content: center;gap: 10px;">
  <img src="https://w7.pngwing.com/pngs/348/734/png-transparent-ontology-logo-ontology-symbol-ontology-sign-ontology-crypto-ontology-coin-ontology-3d-icon-thumbnail.png" alt="Ontology Logo" width="100"/>
  <img src="https://w7.pngwing.com/pngs/593/15/png-transparent-python-others-text-logo-c-thumbnail.png" alt="Python Logo" width="342"/>
</div>

Ce projet est une API REST construite avec Flask qui permet d'extraire des données à partir d'une ontologie OWL et de les exposer sous forme de JSON. L'ontologie utilisée ici est liée à l'irrigation du maïs, et l'API permet d'obtenir des informations sur les classes, propriétés et individus définis dans l'ontologie.

## Fonctionnalités

- Charger une ontologie OWL à partir d'un fichier local.
- Extraire les annotations associées aux classes, propriétés et individus.
- Récupérer des informations sur les propriétés d'objet, les propriétés de données, et les individus.
- Exposer les données de l'ontologie via plusieurs routes API.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les dépendances suivantes :

- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Owlready2](https://owlready2.readthedocs.io/)

Pour installer Flask et Owlready2, exécutez la commande suivante :

```bash
pip install Flask owlready2
```

## Installation et Exécution

1. Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/Sherli7/IRRIGMAIZOnto.git
```

2. Naviguez dans le répertoire du projet :

```bash
cd IRRIGMAIZOnto
```

3. Placez votre fichier d'ontologie OWL dans le dossier IRRIGMAIZOnto :
   ```
   /IRRIGMAIZOnto/irrigation_maize.owl
   ```

4. Lancez l'application Flask :

```bash
python main.py
```

L'application sera disponible à l'adresse : `http://127.0.0.1:8087/`

## Endpoints

Voici les principaux points d'accès disponibles dans l'API :

### 1. Récupérer toutes les données de l'ontologie

- **Route** : `/ontology`
- **Méthode** : `GET`
- **Description** : Renvoie toutes les données extraites de l'ontologie (classes, propriétés, individus).

### 2. Récupérer les classes

- **Route** : `/ontology/classes`
- **Méthode** : `GET`
- **Description** : Renvoie la liste des classes définies dans l'ontologie.

### 3. Récupérer les propriétés d'objet

- **Route** : `/ontology/object_properties`
- **Méthode** : `GET`
- **Description** : Renvoie les propriétés d'objet avec leurs domaines et gammes.

### 4. Récupérer les propriétés de données

- **Route** : `/ontology/data_properties`
- **Méthode** : `GET`
- **Description** : Renvoie les propriétés de données avec leurs domaines et gammes.

### 5. Récupérer les individus

- **Route** : `/ontology/individuals`
- **Méthode** : `GET`
- **Description** : Renvoie la liste des individus et leurs relations.

## Structure du Projet

```
.
├── app.py                 # Code principal de l'application Flask
├── ontology_maize.owl     # Fichier OWL (ontologie)
└── README.md              # Ce fichier de documentation
└── requiments.md          # Regroupe les dépendances nécessaires
```

## Contribution

Les contributions sont les bienvenues. Si vous souhaitez contribuer, veuillez ouvrir une issue ou une pull request.

## Licence

Ce projet est sous licence [MIT License](LICENSE).
