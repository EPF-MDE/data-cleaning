import pytest
import pandas as pd

# This script contains tests for the cleaning functions and should be
# completed by you


@pytest.fixture
def sample_dirty():
    df = pd.read_csv('data/sample_dirty.csv')
    return df

@pytest.fixture
def sample_sane():
    df = pd.read_csv('data/sample_sane.csv')
    return df


@pytest.fixture
def sample_framed():
    df = pd.read_csv('data/sample_clean.csv')
    return df



def assert_column_equal(clean, target, column):
    assert clean[column].equals(
        target[column]), f"Result should be {clean[column]} but was {target[column]}"

def test_adr_num(sample_dirty, sample_clean):

    from loader import format_adr_num, sanitize_adr_num

    clean_data = (sample_dirty
             .pipe(format_adr_num)
             .pipe(sanitize_adr_num))

    assert_column_equal(clean_data, sample_clean, 'adr_num')


def test_tel(sample_dirty, sample_clean):

    from loader import format_tel, sanitize_tel

    clean_data = (sample_dirty
             .pipe(format_tel)
             .pipe(sanitize_tel))

    assert_column_equal(clean_data, sample_clean, 'tel1')

def test_format_and_sanitize(sample_dirty, sample_clean):
    from loader import format_dataframe, sanitize_dataframe
    clean_data = (sample_dirty
             .pipe(format_dataframe)
             .pipe(sanitize_dataframe))
    assert clean_data.equals(sample_clean)

def test_load_clean_dataframe(sample_dirty, sample_clean):
    from loader import load_clean_dataframe
    clean_data = load_clean_dataframe(sample_dirty)
    assert clean_data.equals(sample_clean)

def test_frame_address():
    sample_dirty=pd.DataFrame([
        {
            'adr_num': '2 bis',
            'adr_voie': 'avenue de la gare',
            'com_cp': '34000',
            'com_nom': 'Montpellier'
        },
        {
            'adr_num': '',
            'adr_voie': 'Place Chaptal',
            'com_cp': '34000',
            'com_nom': 'Montpellier'
        }
    ])
    data_out=pd.DataFrame({
        'address': [
            '2 bis avenue de la gare 34000 Montpellier',
            'Place Chaptal 34000 Montpellier',
        ]
    })

    from loader import frame_address
    clean_data=frame_address(sample_dirty)

    assert clean_data.equals(
        data_out), f"Result should be {data_out} but was {clean_data}"
: