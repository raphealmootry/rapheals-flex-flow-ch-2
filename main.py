import streamlit as st

def run_unit_5_flow():
    st.title("Unit 5: Forms of Real Estate Ownership")
    st.subheader("Visual Breakdown of Ownership Paths")

    # Define the Flow Chart using DOT language
    ownership_chart = """
    digraph G {
        node [shape=box, style=filled, color=lightblue, fontname="Helvetica"]
        
        Start [label="Real Estate Ownership", fillcolor=gold]
        
        # Level 1
        Severalty [label="Ownership in Severalty\\n(Single Entity/Person)"]
        CoOwnership [label="Co-Ownership\\n(Two or more)"]
        Trust [label="Trusts\\n(Held for Beneficiary)"]
        
        Start -> Severalty
        Start -> CoOwnership
        Start -> Trust
        
        # Level 2 - Co-Ownership Branches
        TIC [label="Tenancy in Common\\n(Inheritable share)"]
        JT [label="Joint Tenancy\\n(Right of Survivorship)"]
        TE [label="Tenancy by the Entirety\\n(Married Couples)"]
        
        CoOwnership -> TIC
        CoOwnership -> JT
        CoOwnership -> TE
        
        # Level 3 - The PITT requirements
        PITT [label="PITT Requirements:\\nPossession, Interest, Time, Title", shape=ellipse, color=lightgreen]
        JT -> PITT
    }
    """

    # Display the chart in the Streamlit app
    st.graphviz_chart(ownership_chart)

    st.info("💡 Tip: Use this chart to visualize how 'Right of Survivorship' differs between Joint Tenancy and Tenancy in Common.")

if __name__ == "__main__":
    run_unit_5_flow()
