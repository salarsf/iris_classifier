import numpy as np


class IrisFlower():

    with open("iris.csv") as file:
        lines = file.readlines()[1:]
        data = []
        for line in lines:
            data.append(line.strip().split(","))

    dataArr = np.array(data)
    setosa_array = np.array(dataArr[:50,:4], dtype=float)
    versicolor_array = np.array(dataArr[50:100, :4], dtype=float)
    virginica_array = np.array(dataArr[100:, :4], dtype=float)

    setosa_mean = setosa_array.mean(axis=0)
    versicolor_mean = versicolor_array.mean(axis=0)
    virginica_mean = virginica_array.mean(axis=0)

    def __init__(self,sepal_len:float,sepal_wid:float,petal_len:float,petal_wid:float):
        self.spal_len = sepal_len
        self.sepal_wid = sepal_wid
        self.petal_len = petal_len
        self.petal_wid = petal_wid

        self.flower_data = np.array([self.spal_len, self.sepal_wid, self.petal_len, self.petal_wid])

    @property
    def iris_type(self):
        setosa_diff = float(np.linalg.norm(self.flower_data-IrisFlower.setosa_mean))
        versicolor_diff = float(np.linalg.norm(self.flower_data-IrisFlower.versicolor_mean))
        virginica_diff = float(np.linalg.norm(self.flower_data-IrisFlower.virginica_mean))

        min_diff = min(setosa_diff, versicolor_diff, virginica_diff)

        if min_diff == setosa_diff:
            return "setosa"
        elif min_diff == versicolor_diff:
            return "versicolor"
        elif min_diff == virginica_diff:
            return "virginica"