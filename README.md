dig-alignment
=============

Code to do feature alignment in DIG where we map data extracted from sources (mostly Web pages) to JSON files structured accourding to our DIG ontology.

## datasets
Contains sample data, including both external datasets and feature extractions, karma models to align the features to the DIG ontology, and samples of JSON files containing aligned features. 

There is a separate folder for each dataset, typically containing the following files:

- `*-sample.*` are sample files that we load in Karma to define the alignment models.
- `*-model.ttl` are Karma model files to align features.
- `*-model.md` a model report.
- `*-model.png` image of the model.
- `*-jsonld.json` are samples of aligned features (output of Karma)

Larger versions of the files are in Data Tactics (need to document where)

The following files contain data that we will join with the backpage data to add additional information:

- `x-airports-aligned.*` contains place information based on the airport iata codes. After joining, the backpage data gets extended with address and geo-coordinates for the ads that contain airport codes.
- `x-exchange-aligned.*` contains place information based on phone exchange (the first 6 digits of the phone). After joining, the backpage data gets extended with address and geo-coordinates for each extracted phone number.

## karma
The home directory of karma so that others can easily replicate the Karma environment on their machines. The interesting files are in the preloaded-ontologies
