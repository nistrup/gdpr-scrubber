import spacy

NLP_MODEL = spacy.load('en_core_web_lg') # læser den engelske NLP model fra 'spacy'

# vores 'classification' funktion
def scrub_names(token):
    if token.ent_type_ == "PERSON": # tjekker om den specifikke 'token' er markeret som "PERSON" under NER processen (Named Entity Recognition)
        return "[REDACTED] "
    else:
        return token.string

# Selve scrubber funktionen looper igennem hele dokumentet og
def scrub(text):
    doc = NLP_MODEL(text)
    for ent in doc.ents: # dette loop danner tokens ud fra de entities der bliver dannet ud fra NLP modellen
        ent.merge()
    tokens = map(scrub_names, doc) # alle tokens bliver mappet gennem classification funktionen
    return "".join(tokens) # Sætter alle tokens sammen til en samlet sætning igen


s = """Shakespeare was born and raised in Stratford-upon-Avon, Warwickshire.
At the age of 18, he married Anne Hathaway, with whom he had three children: Susanna and twins Hamnet and Judith."""

print(scrub(s))

### OUTPUT ###
#
# [REDACTED] was born and raised in Stratford-upon-Avon, Warwickshire.
# At the age of 18, he married [REDACTED], with whom he had three children: [REDACTED] and twins [REDACTED] and [REDACTED].
#
