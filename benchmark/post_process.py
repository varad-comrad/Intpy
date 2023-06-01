import pandas as pd
import numpy as np
from typing import Optional, overload
import pathlib
# from multipledispatch import dispatch
import matplotlib.pyplot as plt
import seaborn as sns

# df1 = pd.read_csv('results_intpy.csv')
# s1 = df1.mean(axis=0)
# df2 = pd.read_csv('results_no_intpy.csv')
# s2 = df2.mean(axis=0)
# s3 = (s1-s2)/s2

# s3.plot(title='relative difference between intpy and vanilla')
# plt.show()
# ! HASHES DIFERENTES 
class ProcessResults:

    graphic_kinds = {
        'box': sns.boxplot,
        # 'line': sns.lineplot,
        # 'rel': sns.relplot,
        'violin': sns.violinplot,
        'scatter': sns.scatterplot
    } 

    # @overload
    def __init__(self,files: list[str], folder: str) -> None:
        self.__results: list[pd.core.frame.DataFrame] = []
        for element in files:
            self.__results.append(pd.read_csv(element))
        self.medians: list[pd.core.series.Series] = [element.median(axis=1).iloc[0] for element in self.__results]
    
    # @overload
    # def __init__(self, folder: pathlib.Path) -> None:
    #     self.__results: list[pd.core.frame.DataFrame] = []
    #     pass

    def plot_graphic(self, *args, kind='scatter', show=False, xlabel=None,ylabel=None,title=None, **kwargs):
        fig, ax = plt.subplots()
        ax = self.graphic_kinds[kind](x=range(len(self.medians)),y=self.medians,*args, **kwargs)
        if show:
            fig.show()
        return fig, ax

