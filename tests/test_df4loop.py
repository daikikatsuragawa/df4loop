import pandas as pd
import pytest

from df4loop import DFGenerator, DFIterator

sample_dict = {
    "column_1": [100, 200, 300, 400, 500],
    "column_2": ["A", "B", "C", "D", "D"],
    "column_3": ["a", "b", "c", "d", "e"],
}
sample_df = pd.DataFrame.from_dict(sample_dict)


def test_df_iterator():
    answer = []
    for index, row in sample_df.iterrows():
        answer.append(index)
        answer.append(row["column_1"])
        answer.append(row["column_2"])
        answer.append(row["column_3"])

    test = []
    df_iterator = DFIterator(sample_df)
    for index, row in df_iterator.iterrows():
        test.append(index)
        test.append(row["column_1"])
        test.append(row["column_2"])
        test.append(row["column_3"])

    assert answer == test

    answer = []
    for _, row in sample_df.iterrows():
        answer.append(row["column_1"])
        answer.append(row["column_2"])
        answer.append(row["column_3"])

    test = []
    df_iterator = DFIterator(sample_df)
    for row in df_iterator.iterrows(return_indexes=False):
        test.append(row["column_1"])
        test.append(row["column_2"])
        test.append(row["column_3"])

    assert answer == test


def test_df_generator():
    df_generator = DFGenerator()
    for _, row in sample_df.iterrows():
        tmp_row = {
            "column_1": row["column_1"],
            "column_2": row["column_2"],
            "column_3": row["column_3"],
        }
        df_generator.append(tmp_row)
    df = df_generator.generate_df()
    assert df.columns.values.tolist() == sample_df.columns.values.tolist()
    assert df.index.values.tolist() == sample_df.index.values.tolist()
    assert df["column_1"].values.tolist() == sample_df["column_1"].values.tolist()
    assert df["column_2"].values.tolist() == sample_df["column_2"].values.tolist()
    assert df["column_3"].values.tolist() == sample_df["column_3"].values.tolist()

    df_generator = DFGenerator(columns=sample_df.columns.values.tolist())
    for _, row in sample_df.iterrows():
        tmp_row = {
            "column_1": row["column_1"],
            "column_2": row["column_2"],
            "column_3": row["column_3"],
        }
        df_generator.append(tmp_row)
    df = df_generator.generate_df()
    assert df.columns.values.tolist() == sample_df.columns.values.tolist()
    assert df.index.values.tolist() == sample_df.index.values.tolist()
    assert df["column_1"].values.tolist() == sample_df["column_1"].values.tolist()
    assert df["column_2"].values.tolist() == sample_df["column_2"].values.tolist()
    assert df["column_3"].values.tolist() == sample_df["column_3"].values.tolist()

    df_generator = DFGenerator(columns=["column_a", "column_b", "column_c"])
    for _, row in sample_df.iterrows():
        tmp_row = {
            "column_1": row["column_1"],
            "column_2": row["column_2"],
            "column_3": row["column_3"],
        }
        with pytest.raises(Exception):
            df_generator.append(tmp_row)

    df_generator = DFGenerator()
    with pytest.raises(Exception):
        df = df_generator.generate_df()

    df_generator = DFGenerator(sample_df.columns.values.tolist())
    for _, row in sample_df.iterrows():
        df_generator.append([row["column_1"], row["column_2"], row["column_3"]])
    df = df_generator.generate_df()
    assert df.columns.values.tolist() == sample_df.columns.values.tolist()
    assert df.index.values.tolist() == sample_df.index.values.tolist()
    assert df["column_1"].values.tolist() == sample_df["column_1"].values.tolist()
    assert df["column_2"].values.tolist() == sample_df["column_2"].values.tolist()
    assert df["column_3"].values.tolist() == sample_df["column_3"].values.tolist()

    df_generator = DFGenerator()
    with pytest.raises(Exception):
        df_generator.append([1, 2, 3])
