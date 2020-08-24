__author__ = 'Aram Koorn'

import pandas as pd
import numpy as np


class Testing:
    def __init__(self, df):
        self.df = df

    def check_na(self, col, verbose=True, **kwargs):
        """
        raise error if there
        :param col: list with column names
        :return:
        """

        for x in col:
            if self.df[x].isna().sum():
                raise ValueError(f'Found NA value in :{col}')

        if verbose:
            print("Check passed!")

    def check_unique(self, col, verbose=True):
        """
        Check if all the values of the specified column(s) are unique
        :param col: list with the column names
        :param verbose: verbose is test passes
        :return:
        """
        for x in col:
            if df[x].shape[0] != df[x].nunique():
                raise ValueError(f"Not all values are unique in {col}")
        if verbose:
            print("Check passed!")


if __name__ == "__main__":
    df = pd.DataFrame({"x1": [1, 2, 3]})
    test = Testing(df)
    test.check_na(col=['x1'], verbose=True)




