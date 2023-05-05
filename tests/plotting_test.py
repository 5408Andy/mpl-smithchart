import pytest
import numpy as np
from mpl_smithchart import SmithAxes

from matplotlib import pyplot as pp
from matplotlib import rcParams


@pytest.fixture
def mpl_figure():
    pp.figure(figsize=(6,6))
    ax = pp.subplot(1, 1, 1, projection='smith')
    pp.plot([10, 100], markevery=1)
    yield
    pp.draw()


def test_plot_point(mpl_figure):
    pp.plot(200+100j, datatype=SmithAxes.Z_PARAMETER)


def test_plot_s_param(mpl_figure):
    freqs = np.logspace(1, 1e9, 200)
    s11 = (1-1j*freqs*1e-9)/(1+1j*freqs*1e-9)
    pp.plot(s11, markevery=1, datatype=SmithAxes.S_PARAMETER)
