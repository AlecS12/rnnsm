import pickle
from churn_data import ChurnData, getChurnScores
from survival_model import SurvivalModel
import pandas as pd
import numpy as np
from lifelines import AalenAdditiveFitter
from lifelines.utils import concordance_index
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.model_selection import StratifiedKFold

from multiprocessing import Pool
from functools import partial



class AalenChurnModel(SurvivalModel):
    RESULT_PATH = '../../results/churn/aalen_additive/'

    def __init__(self, penalizer=0, include_recency=False):
        super().__init__(include_recency=include_recency)
        self.cf = AalenAdditiveFitter(coef_penalizer=penalizer)

