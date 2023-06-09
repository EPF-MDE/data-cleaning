import os
import requests
import numpy as np
import pandas as pd

def download_data(url, force_download=False, **read_csv_kwargs):
    # Donwload data if it is not in disk
    data_path = os.path.join('data', os.path.basename(url.split('?')[0]))
    if not os.path.exists(data_path) or force_download:
        # ensure data dir is created
        os.makedirs('data', exist_ok=True)
        # request data from url
        response = requests.get(url, allow_redirects=True)
        # save file
        with open(data_path, "w") as f:
            # Note the content of the response is in binary form: 
            # it needs to be decoded.
            # The response object also contains info about the encoding format
            # which we use as argument for the decoding
            f.write(response.content.decode(response.apparent_encoding))

    # load to pandas dataframe
    data = pd.read_csv(data_path, **read_csv_kwargs)
    return data


# Define formating functions per feature (column)

def format_adr_num(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    df.loc[:, 'adr_num'] = (
        df.adr_num
        .astype(str)  # cast all elements to str type
        .str.strip(' ') # trim leading and trailing whitespaces
        # complete with other manipulations if necessary
    )
    
    return df


# and so on.... complete with all the other functions


# once they are all done, call them in the general formatting function
def format_dataframe(df:pd.DataFrame) -> pd.DataFrame:
    """ One function to do all formatting"""
    df = (df.pipe(format_adr_num)
            # .pipe(format_adr_voie)
            # .pipe(format_com_cp)
            # .pipe(format_com_nom)
            # ... addor others (or remove) if necessary
          )
    return df


# Define sanitizing functions per feature (column)
def sanitize_adr_num(df:pd.DataFrame) -> pd.DataFrame:
    return df


# and so on.... complete with all the other functions


# once they are all done, call them in the general sanitizing function
def sanitize_dataframe(df:pd.DataFrame) -> pd.DataFrame:
    """ One function to do all sanitizing"""
    df = (df.pipe(sanitize_adr_num)
            # .pipe(sanitize_adr_voie)
            # .pipe(sanitize_com_cp)
            # .pipe(sanitize_com_nom)
            # ... add others (or remove) if necessary
          )
    return df



# and so on.... complete with all the other functions




# once they are all done, call them in the general clean loading function
def load_clean_dataframe(df:pd.DataFrame)-> pd.DataFrame:
    """one function to run it all and return a clean dataframe"""
    df = (df.pipe(format_dataframe)
          .pipe(sanitize_dataframe)
    )
    return df


# if the module is called, run the main loading function
if __name__ == '__main__':
    load_clean_dataframe(download_data())