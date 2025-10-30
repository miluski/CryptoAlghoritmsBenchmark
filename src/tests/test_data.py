import pytest
from data.generator import DataGenerator

def test_data_generator():
    generator = DataGenerator()
    text = generator.generate_random_text(10)
    assert len(text) == 10
    assert all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' for c in text)
