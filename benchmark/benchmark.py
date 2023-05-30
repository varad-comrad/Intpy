import time
import csv
import typing  # Callable
import pathlib



class Benchmark:
    def __init__(self, *args):
        self.funcs = list(args)
        self.results: list[list] = []

    def benchmark(self, *args, i: int, **kwargs) -> None:
        for func in self.funcs:
            self.benchmark_one(func, *args, i=i, **kwargs)

    def benchmark_one(self, func, *args, i: int,  **kwargs) -> None:
        aux: list = [] # TODO: check for possibility of speeding this method (parallelism?)
        for _ in range(i):
            t = time.perf_counter()
            func(*args, **kwargs)
            aux.append(time.perf_counter()-t)
        self.results.append(aux)

    def save_csv(self, filepaths: list[str], folder: str | None =None,
                    opening_mode: typing.Literal['w', 'a'] = 'w',
                    hidden_folder:bool = False) -> None:
        
        if opening_mode not in ['w', 'a']: # ! To implement proper arg handling
            raise ValueError('Invalid opening mode')
        if folder is None:
            folder = './' # TODO: use pathlib to change this line and the open() line
        path = pathlib.Path(folder)
        if not path.exists():
            path.mkdir(exist_ok=True,parents=True)
        for filepath, lst in zip(filepaths,self.results):
            with open(folder+'/'+filepath, opening_mode) as fp:
                writer = csv.writer(fp)
                if opening_mode == 'w':
                    writer.writerow(range(1,len(lst)+1))
                writer.writerow(lst)

