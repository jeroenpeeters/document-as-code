Document-as-code
================

Simple self-contained example of using document-as-code to generate a 
structured document based on a document-specific domain model.

This example needs Python (2.7 or newer) and the Python yattag library, 
which can be installed with pip install yattag.

Document-as-code consists of four components: a domain model, the 
population of the domain model ("contents" in the example), a 
document ("example_document.py") and a way to transform the raw
document to output formats. This example uses yattag to create
a HTML output document.