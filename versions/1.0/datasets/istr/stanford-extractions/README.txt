MEMEX EXTRACTION DUMP - NOVEMBER 2014
=====================================

This archive contains the extractions and the error analysis for the following
attributes: 
  - service locations (the minimum level of granularity is 'neighborhood', the
	maximum is 'country'), with no distinction between the type of service
  - person names
  - phone numbers
  - email addresses
The extractions are obtained from the advertisements in the "ads" table of the
large IST corpus.

# Directory Structure 
- The "extractions" directory contains one TSV file for each attribute, with the
extractions for that attribute (see below for details on format)
The "error_analysis" directory contains one PDF file for each attribute, with
the error analysis for that attribute. The error analysis is mostly useful to
developers to understand the performance of the extractors and decide how to
improve them

# Format
Each file in the "extractions" directory is a TSV (TAB-separated values) file
with two columns:
 - The first column is the value of the column "id" in the "ads" table of the
   original MySQL database.
 - The second column is the extraction. 
There can be multiple rows per document, one per extraction from that document.

For service locations, person names, and email addresses, the extraction appears
exactly as it was in the text (e.g., no case change). The format of phone
numbers is (xxx) yyy-www-zzzz, unless an international
country code was explicitly specified in the text, in which case the format is
+xxxxxxxxxxxx.

The error_analysis directory contains error analysis for each extractor, in PDF
format.

# MD5 Checksums
The MD5 checksums for each file in the "extractions" directory are:
MD5 (locations.tsv) = 4e95c91ee11707a1dcc68bc11803788e
MD5 (names.tsv) = 88ebeb374d32bb52a2dc40563dac855c
MD5 (phone_numbers.tsv) = 5ffa7c4301cec3d769e0973a3ce366d3
MD5 (email_addresses.tsv) = 83e72088f1a72f0fc89d31eb3968e9f9

# Technical details
The extractions where obtained using DeepDive and the extractors we wrote
(git commit: 580132d67fe440a5e744cbc5bbc9955b16325d50).

