"""
C2S Cell Type Transform
"""

from pathlib import Path
from typing import Optional
from koza.cli_utils import transform_source
from kg_vasc.transform_utils.transform import Transform

C2S_C_SOURCES = {
    "C2S_C": "c2s_c.csv"
}

C2S_C_CONFIGS = {
    "C2S_C_C": "c2s_c_c.yaml",
    "C2S_C_G": "c2s_c_g.yaml"
}

TRANSLATION_TABLE = Path(__file__).parent / "translation_table.yaml"

class C2SCTransform(Transform):
    """Transform class for c2s_c single-cell gene expression data."""

    def __init__(self, input_dir: Optional[Path] = None, output_dir: Optional[Path] = None) -> None:
        source_name = "c2s_c"
        super().__init__(source_name, input_dir, output_dir)

    def run(self) -> None:
        for key in C2S_C_CONFIGS:
            config = Path(__file__).parent / C2S_C_CONFIGS[key]
            print(f"Transforming using config {config}")

            transform_source(
                source=config,
                output_dir=self.output_dir,
                output_format="tsv",
                global_table=TRANSLATION_TABLE,
                local_table=None,
            )