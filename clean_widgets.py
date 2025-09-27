import nbformat

# Path to your notebook
notebook_path = "03-Fine_Tuning_BERT_for_Sentiment/Fine_Tuning_BERT_for_Multi_Class_Sentiment_Classification_for_Twitter_Tweets.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)


if "widgets" in nb.metadata:
    del nb.metadata["widgets"]


for cell in nb.cells:
    if "widgets" in cell.get("metadata", {}):
        del cell["metadata"]["widgets"]

with open(notebook_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Success")