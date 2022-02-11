import datetime
from typing import Tuple, Optional

import pandas as pd
from pathlib import Path
from glob import glob
import re

DATA_INPUT_PATH = Path('data/input/')
DATA_OUTPUT_PATH = Path('data/output/')
DATA_OUTPUT_PREFIX = 'combined_'
DATA_OUTPUT_EXTENSION = '.csv'

INPUT_TS_COL = 'Datum [Europe/Berlin]'
INPUT_COL_PREFIX = 'Leistung '

OUTPUT_TS_COL = 'dt_start'


def transform_data(prev_ts: Optional[str]) -> Tuple[pd.DataFrame, str]:
    if prev_ts is None:
        input_files = [Path(p) for p in glob(str(DATA_INPUT_PATH) + f'/*1000.csv')]
    else:
        input_files = [Path(p) for p in glob(str(DATA_INPUT_PATH) + f'/*0.csv')]
        input_files = [p for p in input_files if re.search(r'\d{8}_\d{4}', p.name).group() > prev_ts]

    timestamp = re.search(r'\d{8}_\d{4}', input_files[0].name).group()

    combined_df = pd.DataFrame()
    for file in input_files:
        df = pd.read_csv(file, sep=';', decimal=',')

        rename_parks = {col: col[len(INPUT_COL_PREFIX):] for col in [c for c in df.columns if c != INPUT_TS_COL]}
        rename_date = {INPUT_TS_COL: OUTPUT_TS_COL}
        df = df.rename(columns=rename_parks)
        df = df.rename(columns=rename_date)

        df = df.set_index(OUTPUT_TS_COL)
        combined_df = df if combined_df.empty else combined_df.join(df)

    if prev_ts is None:
        combined_df.to_csv(DATA_OUTPUT_PATH / f'{DATA_OUTPUT_PREFIX}{timestamp}{DATA_OUTPUT_EXTENSION}',
                           sep=';', decimal=',')

    return combined_df, timestamp


def update():
    prev_file = [Path(p) for p in glob(str(DATA_OUTPUT_PATH) + f'/*.csv')][0]
    df = pd.read_csv(prev_file, sep=';', decimal=',')
    df = df.set_index(OUTPUT_TS_COL)

    prev_ts = re.search(r'\d{8}_\d{4}', prev_file.name).group()
    new_df, new_ts = transform_data(prev_ts)

    max_index = max(df.index)
    new_df = new_df[new_df.index > max_index]

    df = pd.concat([df, new_df])

    df.to_csv(DATA_OUTPUT_PATH / (DATA_OUTPUT_PREFIX + new_ts + DATA_OUTPUT_EXTENSION), sep=';', decimal=',')


def prepare_data():

    # remove parks, that are in both (already done at this point in time)

    in_files = [Path(p) for p in glob(str(DATA_INPUT_PATH) + f'/*0.csv')]

    for file in in_files:
        ts = datetime.datetime.strptime(re.search(r'\d{8}_\d{4}', file.name).group(), '%Y%m%d_%H%M')

        df = pd.read_csv(file, sep=';', decimal=',')

        df['ts'] = pd.to_datetime(df[INPUT_TS_COL], format='%d.%m.%Y %H:%M')
        df = df[df['ts'] <= ts]

        df.drop(columns=['ts'], inplace=True)

        df.to_csv(file, sep=';', decimal=',', index=False)


if __name__ == '__main__':
    # prev_df = transform_data()

    update()




