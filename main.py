import os
from flask import Flask, jsonify
from owlready2 import *

app = Flask(__name__)

# Chemin vers l'ancienne et la nouvelle ontologie
ontology_path = "irrigation_maize.owl"

# Charger l'ontologie
onto = get_ontology(ontology_path).load()

# Extraire les annotations associées à une entité (classe, individu, propriété)
def extract_annotations(entity):
    annotations = {
        "label": entity.label.first() if hasattr(entity, 'label') else None,
        "comment": entity.comment.first() if hasattr(entity, 'comment') else None,
        "versionInfo": entity.versionInfo.first() if hasattr(entity, 'versionInfo') else None,
        "isRuleEnabled": entity.isRuleEnabled.first() if hasattr(entity, 'isRuleEnabled') else None,
        "author": entity.author.first() if hasattr(entity, 'author') else None,
        "isDefinedBy": entity.isDefinedBy.first() if hasattr(entity, 'isDefinedBy') else None,
        "seeAlso": entity.seeAlso.first() if hasattr(entity, 'seeAlso') else None,
    }
    return {k: v for k, v in annotations.items() if v is not None}  # Supprimer les entrées None

# Fonction pour obtenir le type de la portée sous forme lisible
def get_readable_range(r):
    if isinstance(r, type):
        return r.__name__  # Retourne le nom du type, par exemple 'bool', 'float'
    else:
        return str(r)

# Charger les données de l'ontologie avec les relations et annotations
def get_ontology_data():
    classes = []
    object_properties = []
    data_properties = []
    individuals = []

    # Relations entre les propriétés d'objet
    for prop in onto.object_properties():
        domain = prop.domain
        range_ = prop.range
        for d in domain:
            for r in range_:
                object_properties.append({
                    "name": prop.name,
                    "domain": d.name,
                    "range": r.name,
                    "annotations": extract_annotations(prop)
                })

    # Relations entre les propriétés de données
    for prop in onto.data_properties():
        domain = prop.domain
        range_ = prop.range
        for d in domain:
            for r in range_:
                data_properties.append({
                    "name": prop.name,
                    "domain": d.name,
                    "range": get_readable_range(r),  # Utilise la fonction pour rendre le type lisible
                    "annotations": extract_annotations(prop)
                })

    # Relations entre individus et leurs classes/propriétés
    for ind in onto.individuals():
        relations = []

        # Propriétés d'objet et de données
        for prop in ind.get_properties():
            value = list(getattr(ind, prop.python_name))
            value_str = [str(v) for v in value]
            if value_str:
                relations.append({
                    "property": prop.name,
                    "assertionValue": value_str
                })

        # Ajouter l'individu avec ses relations et annotations
        individuals.append({
            "name": ind.name,
            "class": ind.is_a[0].name if ind.is_a else "None",
            "annotations": extract_annotations(ind),
            "relations": relations
        })

    # Ajouter les classes avec leurs annotations
    for cls in onto.classes():
        classes.append({
            "name": cls.name,
            "annotations": extract_annotations(cls)
        })

    return {
        "iri": onto.base_iri,  # Utiliser l'IRI actuel
        "classes": classes,
        "object_properties": object_properties,
        "data_properties": data_properties,
        "individuals": individuals
    }

ontology_data = get_ontology_data()

# Routes Flask pour obtenir les données de l'ontologie
@app.route('/ontology', methods=['GET'])
def get_ontology():
    return jsonify(ontology_data)

@app.route('/ontology/classes', methods=['GET'])
def get_classes():
    return jsonify(ontology_data['classes'])

@app.route('/ontology/object_properties', methods=['GET'])
def get_object_properties():
    return jsonify(ontology_data['object_properties'])

@app.route('/ontology/data_properties', methods=['GET'])
def get_data_properties():
    return jsonify(ontology_data['data_properties'])

@app.route('/ontology/individuals', methods=['GET'])
def get_individuals():
    return jsonify(ontology_data['individuals'])

# Démarrage de l'application avec port personnalisé
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8087))  # Définit le port via une variable d'environnement
    app.run(debug=True, port=port)
