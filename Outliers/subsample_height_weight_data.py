import os
import requests
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import seaborn as sns

#increase font size of all elements
sns.set(font_scale=1.5)


# Data can be found at https://www.kaggle.com/datasets/mustafaali96/weight-height and also at the following url
url = "https://gist.githubusercontent.com/nstokoe/7d4717e96c21b8ad04ec91f361b000cb/raw/bf95a2e30fceb9f2ae990eac8379fc7d844a0196/weight-height.csv"

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
    print(f"File saved to {data_path}")

download_data(url)

# read csv file
data = pd.read_csv('data/weight-height.csv')
#Convert inches/pounds to m/kg
data.loc[:, 'Weight'] /= 2.205
data.loc[:, 'Height'] /= 39.37

# visualize the first 5 rows
data.head()

out = pd.concat([
    data.query("Height > 2"),
    data.query("Height < 1.38"),
    data.query("Weight > 115"),
    data.query("Weight < 38"),
])

inl = pd.concat([
    data.query("Height < 1.9"),
    data.query("Height > 1.40"),
    data.query("Weight < 100"),
    data.query("Weight > 45"),
]).sample(100)

sub = pd.concat([inl,out]).sort_values(by=['Height','Weight']).reset_index(drop=True)
sub.to_csv('data/weights_sub.csv')
