import fitz  # PyMuPDF
import pandas as pd

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

# Extract summaries from PDFs
chatgpt_summary = extract_text_from_pdf("summary_chatgpt.pdf")
notebook_summary = extract_text_from_pdf("summary_notebook.pdf")

# Create a comparison table
df = pd.DataFrame({
    "Model": ["ChatGPT", "Notebook"],
    "Summary": [chatgpt_summary, notebook_summary]
})

# Save to Markdown and CSV
df.to_markdown("summary_comparison.md", index=False)
df.to_csv("summary_comparison.csv", index=False)

print("✅ Comparison table saved as 'summary_comparison.md' and 'summary_comparison.csv'")