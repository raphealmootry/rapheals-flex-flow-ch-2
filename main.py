import streamlit as st
import pandas as pd

def run_unit_5_flexflow():
    st.set_page_config(layout="wide")
    st.title("📂 Unit 5: Real Estate Ownership FlexFlow")
    
    # --- SECTION 1: VISUAL FLOW CHART ---
    st.header("1. Ownership Structure Flow")
    ownership_chart = """
    digraph G {
        node [shape=box, style=filled, color=honeydew, fontname="Helvetica", penwidth=2]
        edge [color=gray, penwidth=1.5]
        
        Start [label="Real Estate Title", fillcolor=gold]
        Severalty [label="Severalty\\n(Single Entity)"]
        CoOwnership [label="Co-Ownership\\n(Multiple Persons)"]
        
        Start -> Severalty
        Start -> CoOwnership
        
        TIC [label="Tenancy in Common\\n(Default/Inheritable)"]
        JT [label="Joint Tenancy\\n(Survivorship)"]
        TE [label="Tenancy by the Entirety\\n(Married)"]
        
        CoOwnership -> TIC
        CoOwnership -> JT
        CoOwnership -> TE
    }
    """
    st.graphviz_chart(ownership_chart)

    # --- SECTION 2: ACTIVE STRATEGY DATA CHART ---
    st.header("2. Active Strategy Data Matrix")
    st.write("Use this chart to differentiate the legal 'PITT' requirements and transferability.")

    strategy_data = {
        "Ownership Type": ["Severalty", "Tenancy in Common", "Joint Tenancy", "Tenancy by the Entirety"],
        "Number of Owners": ["One", "Two or More", "Two or More", "Spouses Only"],
        "Rights of Survivorship": ["No", "No", "Yes", "Yes"],
        "PITT Required?": ["N/A", "Possession only", "P-I-T-T required", "P-I-T-T + Marriage"],
        "Transferability": ["Full control", "Can sell share without consent", "Can sell share (breaks JT)", "Need spouse consent"]
    }

    df = pd.DataFrame(strategy_data)
    
    # Displaying as a styled table for that 'Active Chart' feel
    st.table(df)

    st.success("🎯 Strategy Note: If you see a question about heirs getting the property, look for 'Tenancy in Common'. If the partner gets it automatically, it's 'Joint Tenancy'.")

if __name__ == "__main__":
    run_unit_5_flexflow()
