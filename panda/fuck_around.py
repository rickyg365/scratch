import numpy
import pandas as pd


def match_index(index, data):
    """
    The length of the index array can be greater than the length of the data,
    but the length of the data cannot be greater than the length of the index arrays or you will get a shape error
    """

    new_index = [*index]

    sample_point = list(data.keys())[0]
    condition = len(new_index) < len(data[sample_point])

    counter = 1
    while condition:
        new_index.append(f"extra_row_{counter}")
        counter += 1
        condition = len(new_index) < len(data[sample_point])

    return new_index


if __name__ == "__main__":
    """ Creating, Reading, Writing """
    sample_dict = {
        "height": [30, 20, 20, 30, 20, 30],
        "width": [30, 20, 20, 30, 20, 30],
        "depth": [30, 20, 20, 30, 20, 30],
        "weight": [30, 20, 30, 20, 20, 30]
    }

    custom_index = ["values"]
    fixed_index = match_index(custom_index, sample_dict)

    print(f"Custom Index: {custom_index}")
    print(f"Fixed Index: {fixed_index}")

    # Can pass in a list to use as the index, but can also use index_col to select a column to use as index
    df = pd.DataFrame(sample_dict, index=fixed_index)
    print(df)

    # Save a dataframe by using df.to_csv(filepath)
    output_filepath = "sample.csv"
    df.to_csv(output_filepath)

    """ Indexing, Selecting, Assigning """


