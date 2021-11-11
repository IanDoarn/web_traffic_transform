import unittest
from pathlib import Path
import os
import pandas as pd
import numpy as np

import src.web_transform


class TestWebTransform(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_file = Path('dummy.csv')
        self.tf_config = {
            'columns':
                ['user_id', 'length', 'path'],
            'index': 'user_id'
        }

    def test_tf_data_to_output_result_type(self):

        result = src.web_transform.tf_data_to_output(
            self.csv_file,
            selected_columns=self.tf_config['columns'],
            index=self.tf_config['index']
        )

        assert isinstance(result, pd.DataFrame)
        assert isinstance(
            result.columns,
            pd.core.indexes.base.Index
        )

    def test_tf_data_to_output_result_columns(self):

        result = src.web_transform.tf_data_to_output(
            self.csv_file,
            selected_columns=self.tf_config['columns'],
            index=self.tf_config['index']
        )

        dummy_np_array = np.array([[220,  11],
                                   [314,   8],
                                   [345,   4],
                                   [378,   7],
                                   [449,   4]], dtype=int)

        assert list(result.columns) == ['user_id', '/']

        np.testing.assert_array_equal(result.values, dummy_np_array)