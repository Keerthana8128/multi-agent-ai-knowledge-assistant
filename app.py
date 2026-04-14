# app.py

import streamlit as st

from core.orchestrator import MultiAgentOrchestrator


st.set_page_config(
    page_title="Multi-Agent AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)


def main():
    st.title("🤖 Multi-Agent AI Knowledge Assistant")
    st.write("Ask questions from pasted text or a sample knowledge file.")

    orchestrator = MultiAgentOrchestrator()

    input_mode = st.radio(
        "Choose input type:",
        ["Paste Text", "Use Sample File"]
    )

    pasted_text = ""
    sample_file_path = "data/sample.txt"

    if input_mode == "Paste Text":
        pasted_text = st.text_area(
            "Paste your text here:",
            height=250,
            placeholder="Paste document content here..."
        )
    else:
        st.info("Using sample file: data/sample.txt")

    user_question = st.text_input(
        "Enter your question:",
        placeholder="Example: What are the main goals of this project?"
    )

    run_button = st.button("Run Assistant")

    if run_button:
        try:
            if not user_question.strip():
                st.error("Please enter a question.")
                return

            with st.spinner("Running multi-agent workflow..."):
                if input_mode == "Paste Text":
                    if not pasted_text.strip():
                        st.error("Please paste some text.")
                        return

                    results = orchestrator.process_text(
                        input_text=pasted_text,
                        user_question=user_question
                    )
                else:
                    results = orchestrator.process_file(
                        file_path=sample_file_path,
                        user_question=user_question
                    )

            st.success("Processing completed.")

            st.subheader("Retrieved Context")
            st.text_area(
                "Relevant Context",
                results["retrieved_context"],
                height=250
            )

            st.subheader("Summary")
            st.write(results["summary"])

            st.subheader("Answer")
            st.write(results["answer"])

            st.subheader("Recommended Next Actions")
            st.write(results["recommendations"])

            with st.expander("View Retrieved Chunks"):
                for index, chunk in enumerate(results["retrieved_chunks"], start=1):
                    st.markdown(f"**Chunk {index}:**")
                    st.write(chunk)

            with st.expander("View All Chunks"):
                for index, chunk in enumerate(results["chunks"], start=1):
                    st.markdown(f"**Chunk {index}:**")
                    st.write(chunk)

        except Exception as error:
            st.error(f"Error: {str(error)}")


if __name__ == "__main__":
    main()