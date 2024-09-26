from flies import __version__, run_linters


def test_flies():
    run_linters([])

def test_version():
    assert __version__


