"""Transform module"""

import logging
from pathlib import Path
from typing import List, Optional

# from kg_vasc.transform_utils.ontology import OntologyTransform
from kg_vasc.transform_utils.ontology.ontology_transform import ONTOLOGIES
from kg_vasc.transform_utils.c2s_ct import C2SCTTransform
from kg_vasc.transform_utils.c2s_c import C2SCTransform
from kg_vasc.transform_utils.c2s_t import C2STTransform
from kg_vasc.transform_utils.c2s_all import C2SALLTransform

DATA_SOURCES = {
    # "OntologyTransform": OntologyTransform,
    "C2SCTTransform": C2SCTTransform,
    "C2SCTransform": C2SCTransform,
    "C2STTransform": C2STTransform,
    "C2SALLTransform": C2SALLTransform
}


def transform(
    input_dir: Optional[Path], output_dir: Optional[Path], sources: List[str] = None
) -> None:
    """
    Transform based on resource and class declared in DATA_SOURCES.

    Call scripts in kg_vasc/transform/[source name]/ to
    transform each source into a graph format that
    KGX can ingest directly, in either TSV or JSON format:
    https://github.com/biolink/kgx/blob/master/data-preparation.md

    :param input_dir: A string pointing to the directory to import data from.
    :param output_dir: A string pointing to the directory to output data to.
    :param sources: A list of sources to transform.
    """
    if not sources:
        sources = list(DATA_SOURCES.keys())

    for source in sources:
        if source in DATA_SOURCES:
            logging.info(f"Parsing {source}")
            t = DATA_SOURCES[source](input_dir, output_dir)
            if source in ONTOLOGIES.keys():
                t.run(ONTOLOGIES[source])
            else:
                t.run()