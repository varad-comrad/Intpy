import pandas as pd
import numpy as np
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
class ProcessResults:

    graphic_kinds = {
        'box': sns.boxplot,
        # 'line': sns.lineplot,
        # 'rel': sns.relplot,
        'violin': sns.violinplot,
        'scatter': sns.scatterplot
    } 

    def __init__(self, dirs: list[str] = ['.'], files: list[str] | None = None) -> None:
        # TODO: type checking to format everything properly
        # TODO: implement handling of subdirectories if the user wishes so
        if isinstance(dirs, list) and isinstance(dirs[0], str) and isinstance(files, list | None):
            new_dirs = [pathlib.Path(element) for element in dirs]
        else:
            raise TypeError('dirs must be a list of strings')

        self.__results: list[pd.core.frame.DataFrame] = []
        if files is not None:
            self.__iter_with_files(new_dirs, files)
        else:
            self.__iter_without_files(new_dirs)


    def __iter_without_files(self, dirs: list[pathlib.Path]) -> None:
        for element in dirs:
            for file in element.iterdir():
                self.__results.append(pd.read_csv(
                    file.absolute()).T) if file.is_file() else None

    def __iter_with_files(self, dirs: list[pathlib.Path], files: list[str]) -> None:
        for file in files:
            for dir in dirs:
                aux = dir.joinpath(file)
                self.__results.append(pd.read_csv(
                    aux.absolute()).T) if aux.is_file() else None

    def plot_graphic(self, *args, kind: str='scatter', show: bool=False,
                     xlabel: str | None=None,
                     ylabel: str | None=None,
                     title: str | None=None,
                     use_median: bool=False,
                     **kwargs) -> tuple:
        
        fig, ax = plt.subplots()
        if use_median:
            self.graphic_kinds[kind](x=range(len(self.__results)))
        # # ax = self.graphic_kinds[kind](x=range(len(self.medians)),y=self.medians,*args, **kwargs)
        # if show:
        #     fig.show()
        return fig, ax

a = ProcessResults(['results_fibonacci'])