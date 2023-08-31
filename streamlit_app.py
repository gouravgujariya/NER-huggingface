import streamlit as st
import spacy

nlp = spacy.load("en_core_web_sm")

def get_ner(text):
  doc = nlp(text)
  entities = []
  for ent in doc.ents:
    entities.append((ent.text, ent.label_))
  return entities

st.title("Name Entity Recognition")

text = st.text_input("Enter a text:")

if text:
  entities = get_ner(text)
  st.json(entities)
