# df4loop

df4loop supports general purpose processes that requires a combination of both pandas.DataFrame and loop. Specifically, the mission of df4loop is to "speed up processing" and "make complex code intuitive" at low installation costs.

## Installation

```sh
pip install df4loop
```

## Usage

The following DataFrame is defined to assist users envision the use of df4loop.

```py
import pandas as pd

sample_dict = {
    "column_1": [100, 200, 300, 400, 500],
    "column_2": ["A", "B", "C", "D", "E"],
    "column_3": ["a", "b", "c", "d", "e"],
}
df = pd.DataFrame.from_dict(sample_dict)
df
```

|     |column_1|column_2|column_3|
|----:|-------:|--------|--------|
|    0|     100|A       |a       |
|    1|     200|B       |b       |
|    2|     300|C       |c       |
|    3|     400|D       |d       |
|    4|     500|E       |e       |

### DFIterator

DFIterator helps developers writing the following code. This is code written using pandas.DataFrame.iterrows for the purpose of referencing a value by row.

```py
for index, row in df.iterrows():
    tmp = row["column_1"]
```

DFIterator reproduces this process and speeds it up. Actually, DataFrame and its row pandas.Series are converted to lists and dictionaries to speed up. However, the usage is almost the same.

```py
from df4loop import DFIterator

df_iterator = DFIterator(df)
for index, row in df_iterator.iterrows():
    tmp = row["column_1"]
```

If you do not need to output the index, set `return_indexes=False`.

```py
from df4loop import DFIterator

df_iterator = DFIterator(df)
for row in df_iterator.iterrows(return_indexes=False):
    tmp = row["column_1"]
```

### DFGenerator

DFGenerator supports the generation of DataFrame with rows set by loops. Adding rows to the DataFrame in a loop will take a long time to process. The secret to speeding up is to organize rows in a list or dictionary and then make them pandas.DataFrame at once. DFGenerator supports this process for intuitive implementation.

The following code is an example of selecting the dict type as the row.

```py
from df4loop import DFGenerator

# It is not necessary to specify columns.
df_generator = DFGenerator(columns=df.columns.values.tolist())
for _, row in df.iterrows():
    tmp_row = {
        "column_1": row["column_1"],
        "column_2": row["column_2"],
        "column_3": row["column_3"],
    }
    df_generator.append(tmp_row)
new_df = df_generator.generate_df()
```

The following code is an example of selecting the list type as the row. columns must be specified during initialization.

```py
from df4loop import DFGenerator

df_generator = DFGenerator(columns=df.columns.values.tolist())
for _, row in df.iterrows():
    tmp_row = [
        row["column_1"],
        row["column_2"],
        row["column_3"],
    ]
    df_generator.append(tmp_row)
new_df = df_generator.generate_df()
```
