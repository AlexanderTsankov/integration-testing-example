import pytest
from discount_module import apply_discount

def test_no_discount():
    assert apply_discount(400) == 400

def test_five_percent_discount():
    assert apply_discount(800) == 760  

def test_ten_percent_discount():
    assert apply_discount(1200) == 1080  
