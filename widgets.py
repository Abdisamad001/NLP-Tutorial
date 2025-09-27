import nbformat
import glob

# Find all notebooks in the workspace
notebook_paths = glob.glob('**/*.ipynb', recursive=True)

for notebook_path in notebook_paths:
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

    if "widgets" in nb.metadata:
        del nb.metadata["widgets"]

    for cell in nb.cells:
        if "widgets" in cell.get("metadata", {}):
            del cell["metadata"]["widgets"]

    with open(notebook_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    print(f"Notebook cleaned: {notebook_path}")

print("All notebooks cleaned. Try opening them in GitHub!")
