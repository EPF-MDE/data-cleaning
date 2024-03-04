# TP 1 : Formatting and Sanitizing - Instructions

For this first practical assignment, we'll be working with data from _Montpellier métropole_. You will be downloading the raw "Defibrilators of Montpellier" dataset (the one you've played with in CodinGame) and will write a loader script that cleans and loads a sane dataframe.

This assignment will also be an opportunity to practice some test-oriented development.
To build the loading script, you will proceed with the following steps: 
1. Test-oriented problem specification
2. Implementation of the cleaning functions
3. Validation with tests

## Technical requisites
Throughout this assignent you'll use multiple pandas functionalities such as:
- drop useless columns
- convert string types to numeric or datetime types
- manipulating strings with `.str` (aka the string accessor)
- checking strings for patterns using regular expressions

To learn how to do this in Pandas, you may reffer to the following documents:
- ["Pythonic Data Cleaning With pandas and NumPy",  by Malay Agarwal at RealPython.com](https://realpython.com/python-data-cleaning-numpy-pandas/)
- ["Working with text data", at pandas docs](https://pandas.pydata.org/docs/user_guide/text.html#)
- ["Time series / date functionality", at pandas docs](https://pandas.pydata.org/docs/user_guide/timeseries.html)

## Step 1. Problem specification
Prepare some tests cases that ensure that your cleaning function works as expected:

1. Select a handful of examples (between 10 and 15) from your data that cover the problems you have identified
2. With these examples, compose a sample dirty data file (`sample_dirty.csv`) that will serve as a testing reference.
3. Manually compose a `pd.DataFrame` that corresponds to the `sample_dirty` data loaded with the correct types/formats (`sample_formatted`).
4. Manually compose a `pd.DataFrame` where all the sanity problems got fixed (`sample_sanitized`).

These test cases should be specified in the file `loader_test.py` where indicated.


## Step 2. Implementation of the cleaning functions
Your loading function should be in a file `loader.py`. It should be as modular as possible. For instance:
```python
...

def sanitize_dataframe(df:pd.DataFrame) -> pd.DataFrame:
    """ One function to do all sanitizing"""
    df = (df.pipe(sanitize_adr_num)
            .pipe(sanitize_adr_voie)
            .pipe(sanitize_com_cp)
            .pipe(sanitize_com_nom)
            # ... add others (or remove) if necessary
          )
    return df


def load_clean_dataframe(df:pd.DataFrame)-> pd.DataFrame:
    """one function to run it all and return a clean dataframe"""
    df = (df.pipe(load_formattted_dataframe)
          .pipe(sanitize_dataframe)
    )
    return df
```
## Step 3. Validation
Since the problem is defined in terms of test cases, verifying the task is completed consists in passing each of the test cases.
The `loader_test.py` file contains testing functions that check each of them (assuming you implemented all the test cases). You can run them using `pytest`.
