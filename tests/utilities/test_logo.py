# coding=utf-8

"""weiss logo tests"""

from numpy import uint8 
from sksurgeryimage.utilities.weisslogo import WeissLogo

def test_logo():
    """
    Test that we can make a nice looking logo
    """
    logo = WeissLogo()

    image = logo.get_logo()

    assert image.shape == (331, 331, 3)
    assert image.dtype == uint8

    logo = WeissLogo(400)
    image = logo.get_noisy_logo()

    assert image.shape == (400, 400, 3)
    assert image.dtype == uint8


