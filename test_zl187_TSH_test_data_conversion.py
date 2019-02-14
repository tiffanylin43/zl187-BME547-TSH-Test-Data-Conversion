import pytest


@pytest.mark.parametrize("TSH, expected", [
    ([[1, 0.8, 2, 3.5, 2.2, 1.5],
      [4.0, 3.9, 2.8]], ['hyperthyroidism', 'normal thyroid function']),
    ([[3.3, 4.0, 2.3, 2.5, 3],
      [2.3, 2.5, 2.0, 3.0, 2.8, 2.7]
      ], ['normal thyroid function', 'normal thyroid function']),
    ([[5, 4.5, 3.8, 2.9, 3],
      [0.5, 0.6, 0.7, 0.9]], ['hypothyroidism', 'hyperthyroidism']),
    ([[3.8, 3.9, 4.2, 2.9, 2.0],
      [0.5, 1.5, 1.8, 0.9, 1.0],
      [2.0, 2.1, 2.2, 2.3, 2.4]
      ], ['hypothyroidism', 'hyperthyroidism', 'normal thyroid function']),
])
def test_diagnosis(TSH, expected):
    from zl187_TSH_test_data_conversion import diagnosis
    result = diagnosis(TSH)
    assert result == expected
