from pyaddons import getOS

def test_os():
    assert getOS() == 'linux'