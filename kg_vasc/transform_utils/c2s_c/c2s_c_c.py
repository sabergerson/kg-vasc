"""
Cell type nodes and associations to genes
"""

import uuid
from biolink_model.datamodel.model import AnatomicalEntity, QuantityValue, Attribute, Association
from koza.cli_utils import get_koza_app

# Fetch data rows
source_name = "c2s_c_c"
koza_app = get_koza_app(source_name)
row = koza_app.get_row()

# Track seen cell types
try:
    seen_cs
except NameError:
    seen_cs = set()

# Format resused data
c_name = row["cell_type"]
provider = ["KIBR; Stanford University"]
rank_name = "Expression level rank " + row["rank"]

if c_name not in seen_cs:

    # Mark cell type as seen
    seen_cs.add(c_name)

    # Define AnatomicalEntity node
    c_node = AnatomicalEntity(
        id="uuid:" + str(uuid.uuid5(uuid.NAMESPACE_DNS, c_name)),
        name=c_name,
        category="biolink:AnatomicalEntity",
        description=c_name + " across tissues",
        provided_by=provider
    )

    # Write AnatomicalEntity node
    koza_app.write(c_node)

# Define QuantityValue for rank
rank_quantity = QuantityValue(
    has_numeric_value=int(row["rank"])
)

# Define Attribute for rank
rank_attribute = Attribute(
    id=rank_name,
    name=rank_name,
    category="biolink:Attribute",
    has_attribute_type="EDAM:data_3754",
    has_quantitative_value=rank_quantity,
    provided_by=provider
)

# Define the Association for cell type to gene
association = Association(
    id="uuid:" + str(uuid.uuid1()),
    subject=c_name,
    predicate="biolink:expresses",
    object=row["gene"],
    category="biolink:Association",
    has_attribute=rank_attribute,
    knowledge_level="observation",
    agent_type="data_analysis_pipeline"
)

# Reformat for compatibility with KozaApp
association.knowledge_level = str(association.knowledge_level)
association.agent_type = str(association.agent_type)

# Write Association edge
koza_app.write(association)