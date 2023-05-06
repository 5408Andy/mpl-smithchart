import pytest
import numpy as np
from mpl_smithchart import SmithAxes

from matplotlib import pyplot as pp


@pytest.fixture
def mpl_figure(tmpdir):
    pp.figure(figsize=(6, 6))
    pp.subplot(1, 1, 1, projection='smith')
    yield
    pp.savefig(tmpdir/'out.png', format='png')


@pytest.mark.parametrize(
    "point",
    (
        200+100j,
        50.0,
        50-10j,
    )
)
def test_plot_point(mpl_figure, point):
    pp.plot(point, datatype=SmithAxes.Z_PARAMETER)


def test_plot_s_param(mpl_figure):
    freqs = np.logspace(0, 9, 200)
    s11 = (1-1j*freqs*1e-9)/(1+1j*freqs*1e-9)
    pp.plot(s11, markevery=1, datatype=SmithAxes.S_PARAMETER)


def test_plot_labels(mpl_figure):
    freqs = np.logspace(0, 9, 200)
    s11 = (1-1j*freqs*1e-9)/(1+1j*freqs*1e-9)
    pp.plot(s11, markevery=1, datatype=SmithAxes.S_PARAMETER, label='s11')
    pp.legend()

