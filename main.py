import streamlit as st
import pandas as pd

def run_unit_5_venn_flow():
    st.set_page_config(layout="wide")
    st.title("Unit 5: Tenancy Relationship Venn Flow")
    st.subheader("Visualizing Overlaps in Co-Ownership")

    # --- SECTION 1: VENN-STYLE RELATIONSHIP DIAGRAM ---
    # This uses clusters to show how attributes like 'Survivorship' and 'Multi-Owner' overlap
    venn_chart = """
    digraph G {
        compound=true;
        node [fontname="Helvetica", fontsize=10];
        rankdir=LR;

        # The 'Two or More Owners' Group (All three sit in here)
        subgraph cluster_multi {
            label = "TWO OR MORE OWNERS";
            style=filled;
            color="#E8F4F8";
            
            # The 'Survivorship' Group (Only JT and TE overlap here)
            subgraph cluster_survivor {
                label = "RIGHT OF SURVIVORSHIP (PITT REQUIRED)";
                style=filled;
                color="#FFFACD";
                
                # The 'Married' Group (The innermost circle)
                subgraph cluster_married {
                    label = "MARRIED COUPLES ONLY";
                    style=filled;
                    color="#D4EDDA";
                    TE [label="Tenancy by\\nthe Entirety", shape=doublecircle, fillcolor=white]
                }
                
                JT [label="Joint Tenancy", shape=circle, fillcolor=white]
            }
            
            TIC [label="Tenancy\\nin Common", shape=circle, fillcolor=white]
        }

        # Shared Logic Connections
        TIC -> JT [label="Add Survivorship", style=dashed, color=gray]
        JT -> TE [label="Add Marriage", style=dashed, color=gray]
    }
    """
    st.graphviz_chart(venn_chart)
    
    

    # --- SECTION 2: ATTRIBUTE COMPARISON TABLE ---
    st.header("Relationship Intersection Matrix")
    
    # This table aligns with the 'overlaps' in the diagram above
    comparison_data = {
        "Feature": ["Two or more owners", "Undivided Interest", "Inheritable (to heirs)", "Survivorship (to partners)", "Requires PITT", "Married Couples Only"],
        "Tenancy in Common": ["✅ Yes", "✅ Yes", "✅ Yes", "❌ No", "❌ No", "❌ No"],
        "Joint Tenancy": ["✅ Yes", "✅ Yes", "❌ No", "✅ Yes", "✅ Yes", "❌ No"],
        "Tenancy by Entirety": ["✅ Yes", "✅ Yes", "❌ No", "✅ Yes", "✅ Yes", "✅ Yes"]
    }

    df = pd.DataFrame(comparison_data)
    st.table(df)

    # --- SECTION 3: STRATEGY NOTE ---
    st.markdown("""
    <div style="background-color:#D4EDDA; padding:15px; border-radius:10px; border-left: 5px solid #28A745;">
        <p style="color:#006400; margin:0; font-weight:bold;">
            ✅ Strategy Note: In the diagram above, notice how Tenancy by the Entirety is 'nested' inside 
            Survivorship and Multi-Ownership. It has the most requirements (PITT + Marriage) but the 
            strongest protection!
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_unit_5_venn_flow()
