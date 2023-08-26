from .publaynet import PubLayNetDataset
from .rico import Rico25Dataset
from .coco import COCODataset
_DATASETS = [
    Rico25Dataset,
    PubLayNetDataset,
    COCODataset,
]
DATASETS = {d.name: d for d in _DATASETS}
