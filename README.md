dig-alignment
=============

Code to do feature alignment in DIG where we map data extracted from sources (mostly Web pages) to JSON files structured accourding to our DIG ontology.

## datasets
Contains sample data, including both external datasets and feature extractions, karma models to align the features to the DIG ontology, and samples of JSON files containing aligned features. 

There is a separate folder for each dataset, typically containing the following files:

- `*-sample.*` are sample files that we load in Karma to define the alignment models.
- `*-model-*.ttl` are Karma model files to align features.
- `*-aligned.json` are samples of aligned features. 

Larger versions of the files are in the Azure file system at http://karma-dig-service.cloudapp.net:55320/filebrowser/view/user/szeke/alignments: there you will find datasets containing 3,000 ads. For each dataset there is a `json` file and a `n3` file containing RDF triples. We will combine these `json` files into a consolidated `json` file using the `@id` fields as keys. We expect to have this done by Monday Sept 8.

- `x-inlandempire-lasvegas-losangeles-sandiego.json` is the `json` output from the HTML extractor, and it is the input to other extractors and to our feature alignment process.
- `x-inlandempire-lasvegas-losangeles-sandiego+backpage-basic.*` is the result of aligning `x-inlandempire-lasvegas-losangeles-sandiego.json` to the DIG ontologies. It defines the basic structure for all the aligned files we produce for the different extractors that we run on the file.
- `x-inlandempire-lasvegas-losangeles-sandiego+backpage-phones.*` contains the aligned features after we run the phone extractor.
- `x-inlandempire-lasvegas-losangeles-sandiego+backpage-workingname.*` contains the aligned features after we run the person name extractor.

The following files contain data that we will join with the backpage data to add additional information:

- `x-airports-aligned.*` contains place information based on the airport iata codes. After joining, the backpage data gets extended with address and geo-coordinates for the ads that contain airport codes.
- `x-exchange-aligned.*` contains place information based on phone exchange (the first 6 digits of the phone). After joining, the backpage data gets extended with address and geo-coordinates for each extracted phone number.

## karma
The home directory of karma so that others can easily replicate the Karma environment on their machines. The interesting files are in the preloaded-ontologies
