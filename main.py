import streamlit as st
from graphviz import Digraph
import pandas as pd

st.set_page_config(page_title="Ohio Real Estate Chapter 2 Study", layout="wide")

# Chapter 2 concepts and terms in chronological order
data = [
    {"Phase": 1, "Category": "Foundations", "Term": "Land, Real Estate, and Real Property"},
    {"Phase": 1, "Category": "Foundations", "Term": "Physical Characteristics (Immobility, Indestructibility, Uniqueness)"},
    {"Phase": 2, "Category": "Ownership Rights", "Term": "Bundle of Legal Rights"},
    {"Phase": 2, "Category": "Ownership Rights", "Term": "Surface, Subsurface, and Air Rights"},
    {"Phase": 2, "Category": "Ownership Rights", "Term": "Water Rights (Riparian and Littoral)"},
    {"Phase": 3, "Category": "Property Types", "Term": "Personal Property vs. Real Property"},
    {"Phase": 3, "Category": "Property Types", "Term": "Fixtures and Trade Fixtures"},
    {"Phase": 3, "Category": "Property Types", "Term": "Emblements (Fructus Industriales)"},
    {"Phase": 4, "Category": "Economic Factors", "Term": "Economic Characteristics (Scarcity, Improvements, Permanence)"},
    {"Phase": 4, "Category": "Economic Factors", "Term": "Area Preference (Situs)"},
    {"Phase": 5, "Category": "Industry Standards", "Term": "Ohio Real Estate Licensing Law"},
    {"Phase": 5, "Category": "Industry Standards", "Term": "Professional Organizations (NAR, OAR, Local Boards)"}
]
df = pd.DataFrame(data)

st.title("📚 Chapter 2: Modern Real Estate Practice in Ohio")
st.write("### Conceptual Roadmap & Term Relationships")

# Visual Roadmap of Chapter 2
dot = Digraph()
dot.attr(rankdir='TB', size='10,10')

# Create visual clusters for each phase of study
for phase in sorted(df['Phase'].unique()):
    with dot.subgraph(name=f'cluster_{phase}') as c:
        category_name = df[df['Phase'] == phase]['Category'].iloc[0]
        c.attr(label=f'SECTION {phase}: {category_name}', style='dashed', color='lightgrey')
        
        phase_items = df[df['Phase'] == phase]
        for _, row in phase_items.iterrows():
            # Color coding the study phases
            colors = {1: "#e1f5fe", 2: "#fff9c4", 3: "#f1f8e9", 4: "#fce4ec", 5: "#f3e5f5"}
            c.node(row['Term'], row['Term'], shape='box', style='filled', fillcolor=colors.get(phase, "#ffffff"))

# Establish chronological connections between concepts
dot.edge("Land, Real Estate, and Real Property", "Bundle of Legal Rights")
dot.edge("Bundle of Legal Rights", "Surface, Subsurface, and Air Rights")
dot.edge("Surface, Subsurface, and Air Rights", "Personal Property vs. Real Property")
dot.edge("Personal Property vs. Real Property", "Fixtures and Trade Fixtures")
dot.edge("Fixtures and Trade Fixtures", "Economic Characteristics (Scarcity, Improvements, Permanence)")
dot.edge("Economic Characteristics (Scarcity, Improvements, Permanence)", "Ohio Real Estate Licensing Law")

st.graphviz_chart(dot, width="stretch")
st.table(df)
