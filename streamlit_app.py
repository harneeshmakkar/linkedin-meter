
import streamlit as st

from analyzer import analyze_post


st.set_page_config(
    page_title="LinkedIn Bullshit Meter",
    page_icon="🎯",
    layout="centered",
)

st.title("🎯 LinkedIn Bullshit Meter")

st.write(
    "Paste a LinkedIn post to analyze its vagueness, "
    "exaggeration, corporate jargon, evidence gaps, and filler."
)

st.caption(
    "This tool evaluates rhetorical style, not whether someone "
    "is genuinely lying."
)

post = st.text_area(
    "Your LinkedIn post",
    height=250,
    placeholder="Paste the entire LinkedIn post here...",
)

if st.button("Analyze post", type="primary"):
    if not post.strip():
        st.warning("Please paste a LinkedIn post first.")

    else:
        with st.spinner("Analyzing your post..."):
            analysis = analyze_post(post)

        if analysis is None:
            st.error("Analysis failed. Please try again.")

        else:
            result, score, category = analysis

            st.divider()
            st.subheader("Your results")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Bullshit score", f"{score}/100")

            with col2:
                st.metric("Classification", category)

            st.progress(score / 100)

            st.subheader("Dimension scores")

            dimensions = [
                ("Vagueness", result.vagueness),
                ("Exaggeration", result.exaggeration),
                ("Jargon", result.jargon),
                ("Evidence gap", result.evidence_gap),
                ("Filler", result.filler),
            ]

            for name, value in dimensions:
                st.write(f"**{name}: {value}/20**")
                st.progress(value / 20)

            st.subheader("Why this score?")

            for reason in result.reasons:
                st.markdown(f"- {reason}")

            st.subheader("Suspicious phrases")

            if result.suspicious_phrases:
                for phrase in result.suspicious_phrases:
                    st.markdown(f"- {phrase}")
            else:
                st.write("No suspicious phrases identified.")
