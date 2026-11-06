
import streamlit as st

# Website heading
st.title("🧬 DNA Sequence Analyzer")
st.caption("Developed by Amir Raza | Bioinformatics Project")

st.write("Welcome to my Bioinformatics Project!")
st.write("Analyze your DNA sequence using Python.")

# DNA input
dna = st.text_area(
    "Enter your DNA sequence:",
    placeholder="Example: ATGCGATCGTAGCTAG"
)

# Analyze button
if st.button("Analyze DNA"):

    # Clean sequence
    dna = dna.strip().upper()

    # Check empty sequence
    if not dna:
        st.warning("Please enter a DNA sequence.")

    # Validate DNA
    elif any(base not in "ATGC" for base in dna):
        st.error("Invalid DNA sequence! Use only A, T, G and C.")

    else:
        # Calculate sequence length
        length = len(dna)

        # Count nucleotides
        a = dna.count("A")
        t = dna.count("T")
        g = dna.count("G")
        c = dna.count("C")

        # Calculate GC and AT content
        gc_content = ((g + c) / length) * 100
        at_content = ((a + t) / length) * 100

        # Complementary DNA
        table = str.maketrans("ATGC", "TACG")
        complement = dna.translate(table)

        # DNA to RNA transcription
        rna = dna.replace("T", "U")

        # Display report
        st.success("DNA analysis completed successfully!")

        st.subheader("📊 DNA Analysis Report")

        st.metric("Sequence Length", length)

        # Nucleotide counts
        st.subheader("Nucleotide Count")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Adenine (A)", a)
        col2.metric("Thymine (T)", t)
        col3.metric("Guanine (G)", g)
        col4.metric("Cytosine (C)", c)

        # GC and AT content
        st.subheader("Composition Analysis")

        col5, col6 = st.columns(2)

        col5.metric("GC Content", f"{gc_content:.2f}%")
        col6.metric("AT Content", f"{at_content:.2f}%")

        # Complementary DNA
        st.subheader("🧬 Complementary DNA")

        st.code(complement)

        # RNA transcription
        st.subheader("🧪 RNA Transcription")

        st.code(rna)

        st.success("All analysis results generated!")
