"""
C2S Cell Type / Tissue Transform
"""

from pathlib import Path
from typing import Optional
from koza.cli_utils import transform_source
from kg_vasc.transform_utils.transform import Transform

C2S_CT_SOURCES = {
    "C2S_CT": "c2s_ct.csv"
}

C2S_CT_CONFIGS = {
    "C2S_CT_CT": "c2s_ct_ct.yaml",
    "C2S_CT_G": "c2s_ct_g.yaml"
}

TRANSLATION_TABLE = Path(__file__).parent / "translation_table.yaml"

class C2SCTTransform(Transform):
    """Transform class for c2s_ct single-cell gene expression data."""

    def __init__(self, input_dir: Optional[Path] = None, output_dir: Optional[Path] = None) -> None:
        source_name = "c2s_ct"
        super().__init__(source_name, input_dir, output_dir)

    def run(self) -> None:
        for key in C2S_CT_CONFIGS:
            config = Path(__file__).parent / C2S_CT_CONFIGS[key]
            print(f"Transforming using config {config}")

            transform_source(
                source=config,
                output_dir=self.output_dir,
                output_format="tsv",
                global_table=TRANSLATION_TABLE,
                local_table=None,
            )