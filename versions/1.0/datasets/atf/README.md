# Karma workflow for atf domain

## Process

* process-atf-evolution-forums 
 * reads from /ingest/evolution-forums
 * writes to:
  * /process/$DATASET/$TRIAL/evolution-forums/main
  * /process/$DATASET/$TRIAL/evolution-forums/provider
  * /process/$DATASET/$TRIAL/evolution-forums/user
  * /process/$DATASET/$TRIAL/evolution-forums/weapons
* process-atf-j28json
 * reads from /ingest/j28json
 * writes to:
  * /process/$DATASET/$TRIAL/j28json/location
  * /process/$DATASET/$TRIAL/j28json/provider
  * /process/$DATASET/$TRIAL/j28json/user
  * /process/$DATASET/$TRIAL/j28json/weapons
  * /preprocess/$DATASET/$TRIAL/j28json/main
* process-atf-j28xml
 * reads from /ingest/j28xml
 * writes to:
  * /preprocess/$DATASET/$TRIAL/j28xml/feature
* hivejoin-atf-j28 treated as part of the Process phase 
 * "source" (post) table resides at /preprocess/$DATASET/$TRIAL/j28xml/feature
 * "target" (thread) table resides at /preprocess/$DATASET/$TRIAL/j28json/main
 * writes to:
  * /process/$DATASET/$TRIAL/main-j28xml/

## Coordinate

* coordinate-atf
 * reads recursively from /process/$DATASET/$TRIAL
 * writes to /coordinate/$DATASET/$TRIAL

## Aggregate

* aggregate-atf
 * reads from /coordinate/$DATASET/$TRIAL
 * writes to /aggregate/$DATASET/$TRIAL

## Publish

* publish_es
 * read from /aggregate/$DATASET/$TRIAL
 * write to elastic search

## NOTES/AGP
See z-attic/ for obsolete sources examined in April2015 QPR
