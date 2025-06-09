"""
Gene nodes
"""

import uuid
from biolink_model.datamodel.model import Gene
from koza.cli_utils import get_koza_app

# Fetch data rows
source_name = "c2s_t_g"
koza_app = get_koza_app(source_name)
row = koza_app.get_row()

# Track seen genes
try:
    seen_genes
except NameError:
    seen_genes = set()

# Format resused data
gene_name = row["gene"]

if gene_name not in seen_genes:

    # Mark gene as seen
    seen_genes.add(gene_name)
    
    # Define Gene node
    gene_node = Gene(
        id="uuid:" + str(uuid.uuid5(uuid.NAMESPACE_DNS, gene_name)),
        name=gene_name,
        category="biolink:Gene",
        provided_by=["KIBR; Stanford University"]
    )
    
    # Write Gene node
    koza_app.write(gene_node)