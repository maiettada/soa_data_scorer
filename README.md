# Extraction of public administration data from official document

The following modules were used to perform a Named Entity Recognition of data from documents(mostly tenders) of the Public Administration.
Those data describe the certifications that a company is required to have to apply for a tender; those certification in Italy are called SOA-certifications(S.O.A.: in Italian "Società degli Organismi di Attestazione", in English "Society of Certification Organizations").
The modules of this repository were built and used to extract  certifications data from documents.

**Modules**: 
1. NER regex: python script that extracts SOA data with the usage of regular expressions;
2. dataset splitter: takes a gold.json1 file describing the ground truth; divides it into many labelled sentences, distributing them to the train/dev/test bins;
It's a necessary step for the setup of a NER task in spacy;
3. NER SpaCy: bash scripts to initialize, train, debug and evaluate the neural network with the usage of the Spacy library;
4. scorer for regex-extracted data: takes in input some regex-extracted soa data (v1, v2 or v3, retrieved by using different regex) and scores them by comparing them to the ground truth;


5. json to csv: helper script to convert Spacy-scores from json format to csv format;

documented_outputs: results of the modules with the real data.

**Commands.txt**:
 
Contains the two usages:
1. Regex VS Spacy evaluation: usage and evaluation of regex and spaCy NER
2. Human In the Loop evaluation: runs a HITL framework, by combining regex-system annotations and human gold-annotations in an iterative way.

[![flow chart](https://github.com/maiettada/soa_data_extraction/blob/main/flow_chart.pdf)]

