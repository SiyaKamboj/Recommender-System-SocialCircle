import nbformat as nbf
from pathlib import Path

# Notebooks to merge, in the order you want
NOTEBOOKS = [
    "EDA/eda.ipynb",
    "Graph_Features/features.ipynb",
    "Modeling/model.ipynb",
    "Evaluation/evaluation.ipynb",  # change name here if needed
]

merged = nbf.v4.new_notebook()
merged_cells = []

for nb_path in NOTEBOOKS:
    nb_path = Path(nb_path)
    print(f"Merging {nb_path}...")

    if not nb_path.exists():
        raise FileNotFoundError(f"Notebook not found: {nb_path}")

    nb = nbf.read(nb_path, as_version=4)

    # Optional: add a header before each notebook’s content
    section_title = f"# {nb_path.parts[0]} – {nb_path.name}"
    merged_cells.append(nbf.v4.new_markdown_cell(section_title))

    merged_cells.extend(nb.cells)

merged.cells = merged_cells

output_path = Path("project_full.ipynb")
nbf.write(merged, output_path)
print(f"Written merged notebook to {output_path}")
