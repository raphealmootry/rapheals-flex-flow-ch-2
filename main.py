import streamlit as st
import pandas as pd

def run_unit_5_flexflow():
    st.set_page_config(layout="wide")
    st.title("Unit 5: Real Estate Ownership FlexFlow")

    # --- SECTION 1: EXACT OWNERSHIP STRUCTURE FLOW ---
    st.header("1. Ownership Structure Flow")
    
    # Replicating the exact layout from your visual reference
    ownership_chart = """
    digraph G {
        node [shape=box, style=filled, color="#ADD8E6", fontname="Helvetica", margin=0.2]
        edge [color="#333333", penwidth=1.5]

        # Top Level
        Top [label="Real Estate Ownership", fillcolor="#FFD700", shape=rect]

        # Middle Level - Peer nodes
        Severalty [label="Ownership in Severalty\\n(Single Entity/Person)"]
        CoOwnership [label="Co-Ownership\\n(Two or more)"]
        Trusts [label="Trusts\\n(Held for Beneficiary)"]

        # Sub-level for Co-Ownership
        TIC [label="Tenancy in Common\\n(Inheritable share)"]
        JT [label="Joint Tenancy\\n(Right of Survivorship)"]
        TE [label="Tenancy by the Entirety\\n(Married Couples)"]

        # Final Level
        PITT [label="PITT Requirements:\\nPossession, Interest, Time, Title", fillcolor="#90EE90", shape=ellipse]

        # Connections
        Top -> {Severalty CoOwnership Trusts}
        CoOwnership -> {TIC JT TE}
        JT -> PITT

        # Force horizontal alignment for the middle rows
        {rank=same; Severalty; CoOwnership; Trusts;}
        {rank=same; TIC; JT; TE;}
    }
    """
    st.graphviz_chart(ownership_chart)

    st.info("💡 Tip: Use this chart to visualize how 'Right of Survivorship' and 'PITT' sit between Joint Tenancy and Tenancy in Common.")

    # --- SECTION 2: ACTIVE STRATEGY DATA MATRIX ---
    st.header("2. Active Strategy Data Matrix")
    st.write("Use this data chart to differentiate the legal 'PITT' requirements and transferability.")

    strategy_data = {
        "Ownership Type": ["Severalty", "Tenancy in Common", "Joint Tenancy", "Tenancy by the Entirety"],
        "Number of Owners": ["One", "Two or More", "Two or More", "Spouses Only"],
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
            ✅ Strategy Note: If you see a question about heirs getting the property, it's Tenancy in Common. 
            If the partner gets it automatically, it's Joint Tenancy.
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_unit_5_flexflow()
