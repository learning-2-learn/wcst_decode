from __future__ import annotations
from typing import Tuple, List
import numpy.typing as npt
from sklearn.model_selection import KFold
from .trial_splitter import TrialSplitter

class KFoldSplitter(TrialSplitter):
    """Splits trials into train/test sets using k folds on each iteration"""
    def __init__(self, trial_numbers: List[int], n_splits) -> None:
        self.trial_numbers = trial_numbers
        self.n_splits = n_splits
        kf = KFold(n_splits=n_splits)
        self.splits = kf.split(self.trial_numbers)
        self.iter = iter(self.splits)


    def __iter__(self) -> KFoldSplitter:
        self.iter = iter(self.splits)
        return self

    def __next__(self) -> Tuple[List[int], List[int]]:
        return next(self.iter)

    def __len__(self) -> int:
        return self.n_splits
