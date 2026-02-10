import streamlit as st
import pandas as pd

def run_chapter_6_land_description():
    st.set_page_config(layout="wide")
    st.title("Chapter 6: Land Description FlexFlow")

    # --- SECTION 1: LEGAL DESCRIPTION METHODS FLOW ---
    st.header("1. Methods of Legal Description (Attribute Linked)")
    
    # Diagram logic: Categorizing the 3 primary ways land is legally identified
    land_desc_chart = """
    digraph G {
        node [shape=box, style=filled, color="#F0FFF0", fontname="Helvetica", margin=0.2]
        edge [color="#333333", penwidth=1.5]

        # Root
        Top [label="Legal Descriptions\\n(Defining Boundaries)", fillcolor="#FFD700", shape=rect]

        # The Three Main Methods
        MetesBounds [label="Metes & Bounds\\n(Oldest Method)", shape=diamond, fillcolor="#E0FFFF"]
        GovSurvey [label="Government Survey\\n(Rectangular System)", shape=diamond, fillcolor="#E0FFFF"]
        LotBlock [label="Lot & Block\\n(Recorded Plat)", shape=diamond, fillcolor="#E0FFFF"]

        # Metes & Bounds Path
        Top -> MetesBounds
        MetesBounds -> POB [label="Starts/Ends At"]
        MetesBounds -> Monuments [label="Uses Markers"]
        
        # Government Survey Path
        Top -> GovSurvey
        GovSurvey -> PrincipalMeridians [label="North/South Lines"]
        GovSurvey -> BaseLines [label="East/West Lines"]
        GovSurvey -> Townships [label="6x6 Mile Grids"]
        Townships -> Sections [label="36 per Township"]

        # Lot & Block Path
        Top -> LotBlock
        LotBlock -> Subdivisions [label="Urban Areas"]
        LotBlock -> PlatMap [label="Recorded Document"]

        # Nodes
        POB [label="Point of Beginning", fillcolor="#FFFACD"]
        Monuments [label="Monuments\\n(Natural or Man-made)"]
        Sections [label="Sections\\n(1 sq mile / 640 acres)", fillcolor="#90EE90"]
        PlatMap [label="Plat Map\\n(Public Record)"]

        # Alignment
        {rank=same; MetesBounds; GovSurvey; LotBlock;}
    }
    """
    st.graphviz_chart(land_desc_chart)

    # --- SECTION 2: LAND MEASUREMENT MATRIX ---
    st.header("2. Land Measurement & Conversion Matrix")
    st.write("Essential 'Math of Real Estate' for Chapter 6.")
    
    measurement_data = {
        "Unit": ["1 Section", "1 Quarter Section", "1 Acre", "1 Mile (Linear)", "1 Township"],
        "Contains": ["640 Acres", "160 Acres", "43,560 Sq Ft", "5,280 Feet", "36 Sections"],
        "Description": ["1 x 1 Mile Square", "Used in Gov Survey", "7-11 Math: 4+3=7, 5+6=11", "Linear Measurement", "6 x 6 Mile Square"],
        "Key Attribute": ["1 Square Mile", "Basis for Farmland", "Primary Unit for Lots", "Boundary Length", "Primary Survey Unit"]
    }

    df = pd.DataFrame(measurement_data)
    st.table(df)

    # --- SECTION 3: STRATEGY NOTE WITH DARK GREEN TEXT ---
    st.markdown("""
    <div style="background-color:#D4EDDA; padding:15px; border-radius:10px; border-left: 5px solid #28A745;">
        <p style="color:#006400; margin:0; font-weight:bold;">
            ✅ Negotiation Strategy: For your 44105 market, you will almost exclusively see "Lot & Block" descriptions 
            on your Farringdon property deeds. However, keep the "43,560" number memorized—investors will always 
            ask about the acreage vs. square footage when calculating buildable density!
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_chapter_6_land_description()
