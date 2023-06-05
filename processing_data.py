import pandas as pd
import pathlib
import seaborn as sns

l = [pd.read_csv(file) for file in pathlib.Path('results_fibonacci').iterdir()]
df = pd.DataFrame({file: pd.read_csv(file).median(axis=1) for file in pathlib.Path('results_fibonacci').iterdir()})
print(df['    results_fibonacci/results_intpy.csv'])
# sns.scatterplot(x=range(len(l)), y=)
print(df)