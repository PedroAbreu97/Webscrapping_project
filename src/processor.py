import pandas as pd
import os
from src.utils import ensure_dir

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        df = pd.DataFrame(self.data)
        df['price'] = df['price'].str.replace('$', '').astype(float)
        return df

    def save_data(self, df, filepath):
        ensure_dir(os.path.dirname(filepath))
        df.to_csv(filepath, index=False)