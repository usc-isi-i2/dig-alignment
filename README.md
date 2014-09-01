dig-alignment
=============

Code to do feature alignment in DIG where we map data extracted from sources (mostly Web pages) to JSON files structured accourding to our DIG ontology.

## datasets
Contains sample data, including both external datasets and feature extractions, karma models to align the features to the DIG ontology, and samples of JSON files containing aligned features. 

There is a separate folder for each dataset, typically containing the following files:

- `*-sample.*` are sample files that we load in Karma to define the alignment models.
- `x-*.zip` are slightly larger sample datasets.
- `*-model-*.ttl` are Karma model files to align features.
- `*-aligned.json` are samples of aligned features. 

## karma
The home directory of karma so that others can easily replicate the Karma environment on their machines. The interesting files are in the preloaded-ontologies
