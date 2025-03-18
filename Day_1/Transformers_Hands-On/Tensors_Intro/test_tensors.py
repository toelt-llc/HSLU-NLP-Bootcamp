import pytest
import tensorflow as tf
import numpy as np

# Load your dictionary (this will be replaced in the Jupyter Notebook)
results_dict = {}  # Empty placeholder; in Jupyter, you pass the actual dictionary

# Custom assertion function for TensorFlow tensors
def assert_tensors_equal(tensor1, tensor2):
    np.testing.assert_array_equal(tensor1.numpy(), tensor2.numpy())

@pytest.mark.parametrize("key, expected_value", [
    ("a", tf.ones(shape=(3, 3))),
    ("b", tf.expand_dims(tf.ones(shape=(3, 3)), 0)),
    ("c", tf.zeros(shape=(9, 1))),
    ("d_shape", (1, 3, 3)),
    ("e", tf.constant([[[0.0, 0.0, 0.0],
                        [0.0, 0.0, 0.0],
                        [0.0, 0.0, 0.0]]])),

    ("f", tf.constant([[[1.0, 2.0, 3.0],
                        [1.0, 2.0, 3.0],
                        [4.0, 5.0, 6.0],
                        [7.0, 8.0, 9.0]]])),

    ("g", tf.constant([3.0, 3.0, 6.0, 9.0])),

    ("i", tf.constant([[[0.0, 0.0, 0.0, 0.0],
                        [0.0, 0.0, 0.0, 0.0],
                        [0.0, 0.0, 0.0, 0.0]]])),

    ("j", tf.constant([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [1., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [1., 1., 1., 0., 0., 0., 0., 0., 0., 0.],
                       [1., 1., 1., 1., 0., 0., 0., 0., 0., 0.],
                       [1., 1., 1., 1., 1., 0., 0., 0., 0., 0.],
                       [1., 1., 1., 1., 1., 1., 0., 0., 0., 0.],
                       [1., 1., 1., 1., 1., 1., 1., 0., 0., 0.],
                       [1., 1., 1., 1., 1., 1., 1., 1., 0., 0.],
                       [1., 1., 1., 1., 1., 1., 1., 1., 1., 0.],
                       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]])),

    ("k", tf.constant([1, 2, 3, 4, 8])),
    ("l", tf.constant([[1, 2, 3, 4, 8]])),
    ("m", tf.tile(tf.constant([[1, 2, 3, 4, 8]]), (50, 1))),
    ("n", tf.tile(tf.constant([[1, 2, 3, 4, 8]]), (50, 1)) == 3),
    ("o", tf.tile(tf.constant([[1, 2, 3, 4, 8]]), (50, 1)) / 3),
    ("p_shape", [10, 5])
])

def test_notebook_results(key, expected_value):
    """Test function that checks notebook dictionary values against expected values."""
    actual_value = results_dict[key]  # Fetch from the dictionary

    if isinstance(expected_value, tf.Tensor):
        assert_tensors_equal(actual_value, expected_value)
    else:
        assert actual_value == expected_value
