import streamlit as st
import pandas as pd

def run_unit_5_flexflow():
    st.set_page_config(layout="wide")
    st.title("Unit 5: Real Estate Ownership FlexFlow")

    # --- SECTION 1: RELATIONSHIP-BASED OWNERSHIP FLOW ---
    st.header("1. Ownership Structure Flow (Attribute Linked)")
    
    # Diagram logic: Lines now reflect the relationship similarities in the matrix
    ownership_chart = """
    digraph G {
        node [shape=box, style=filled, color="#ADD8E6", fontname="Helvetica", margin=0.2]
        edge [color="#333333", penwidth=1.5]

        # Root
        Top [label="Real Estate Ownership", fillcolor="#FFD700", shape=rect]

        # Similarity Hubs (Shared Matrix Attributes)
        SingleOwner [label="One Owner", shape=diamond, fillcolor="#F0F8FF"]
        MultiOwner [label="Two or More Owners", shape=diamond, fillcolor="#F0F8FF"]
        SurvivorshipHub [label="Right of Survivorship", shape=circle, fillcolor="#FFFACD", margin=0.1]

        # Top Level Branching
        Top -> SingleOwner
        Top -> MultiOwner
        Top -> Trusts

        # Relationship Mapping
        SingleOwner -> Severalty [label="Sole Control"]
        
        MultiOwner -> TIC [label="Inheritable"]
        MultiOwner -> JT [label="Survivorship Path"]
        MultiOwner -> TE [label="Married Path"]

        # Linking the 'Survivorship' relationship across the matrix
        JT -> SurvivorshipHub
        TE -> SurvivorshipHub
        SurvivorshipHub -> PITT [label="Requires 4 Unities"]

        # Nodes
        Severalty [label="Ownership in Severalty"]
        Trusts [label="Trusts\\n(Held for Beneficiary)"]
        TIC [label="Tenancy in Common"]
        JT [label="Joint Tenancy"]
        TE [label="Tenancy by the Entirety"]
        PITT [label="PITT Requirements:\\nPossession, Interest, Time, Title", fillcolor="#90EE90", shape=ellipse]

        # Alignment
        {rank=same; SingleOwner; MultiOwner; Trusts;}
        {rank=same; Severalty; TIC; JT; TE;}
    }
    """
    st.graphviz_chart(ownership_chart)
    

    # --- SECTION 2: ACTIVE STRATEGY DATA MATRIX ---
    st.header("2. Active Strategy Data Matrix")
    
    strategy_data = {
        "Ownership Type": ["Severalty", "Tenancy in Common", "Joint Tenancy", "Tenancy by the Entirety"],
        "Number of Owners": ["One", "Two or More", "Two or More", "Two or More (Spouses)"],
        "Rights of Survivorship": ["No", "No", "Yes", "Yes"],
        "PITT Required?": ["Full Control", "Possession Only", "P-I-T-T Required", "P-I-T-T + Marriage"],
        "Transferability": ["N/A", "Can sell share (No consent)", "Can sell share (Breaks JT)", "Need Spouse Consent"]
    }

    df = pd.DataFrame(strategy_data)
    st.table(df)

    # --- SECTION 3: STRATEGY NOTE WITH DARK GREEN TEXT ---
    st.markdown("""
    <div style="background-color:#D4EDDA; padding:15px; border-radius:10px; border-left: 5px solid #28A745;">
        <p style="color:#006400; margin:0; font-weight:bold;">
            ✅ Strategy Note: Notice how the diagram links "Two or More" to TIC, JT, and TE. 
            Only the paths leading to the yellow Survivorship hub require PITT!
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_unit_5_flexflow()
