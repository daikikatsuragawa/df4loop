import copy

import pandas as pd


class DFIterator:
    def __init__(self, df):
        self.__df = copy.deepcopy(df)
        self.__indexes = self.__df.index.values.tolist()
        self.__rows = self.__df.to_dict(orient="records")

    def get_df(self):
        return self.__df

    def iterrows(self, return_indexes=True):
        if return_indexes == True:
            return zip(self.__indexes, self.__rows)
        else:
            return self.__rows


class DFGenerator:
    __columns_are_defined = False

    def __init__(self, columns=[]):
        if columns != []:
            self.__columns = columns
            self.__columns_are_defined = True
        self.__rows = []

    def append(self, row):
        if self.__columns_are_defined == True:
            if isinstance(row, dict):
                if set(self.__columns) != set(row.keys()):
                    raise Exception
        else:
            if isinstance(row, list):
                raise Exception
            self.__columns = row.keys()
            self.__columns_are_defined = True
        self.__rows.append(row)

    def generate_df(self):
        if self.__rows == []:
            raise Exception
        if self.__columns == []:
            raise Exception
        return pd.DataFrame(self.__rows, columns=self.__columns)
