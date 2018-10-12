# GDPR mareridt? - N(L)P!

En simpel data scrubber til at fjerne alle navne i en given tekst med NLP (Natural Language Processing), idéen ville være hvis du finder dig i en situation med tusindvis af dokumenter med tilfældige navne og måske også trykfejl der gør det svært bare at lave en "search-and-replace"

## Hvordan fungerer NLP i dette eksempel?

Der mange skridt der indgår i en NLP Pipeline og de kan være forskellige alt efter hvad formålet er, dette er stukturen jeg har brugt:

![alt text](https://cdn-images-1.medium.com/max/1000/1*zHLs87sp8R61ehUoXepWHA.png)

Ovenstående er fra Medium artiklen: *Natural Language Processing is Fun! af Adam Geitgey*

I mit eksempel er det kun navne der bliver fjernet men man kunne meget nemt inkluderer byer og lande med ent_type_ == "GPE" samt nationalitet / religioner eller kendte bygninger / lufthavne / broer eller andet med henholdsvis "NORP" og "FAC"

### Input:

> **Shakespeare** was born and raised in Stratford-upon-Avon, Warwickshire.
> At the age of 18, he married **Anne Hathaway**, with whom he had three children: **Susanna** and twins **Hamnet** and **Judith**.

### Output:

> *[REDACTED]* was born and raised in Stratford-upon-Avon, Warwickshire.
> At the age of 18, he married *[REDACTED]*, with whom he had three children: *[REDACTED]* and twins *[REDACTED]* and *[REDACTED]*.
