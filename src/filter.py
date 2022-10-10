from brainflow.data_filter import DataFilter, FilterTypes, AggOperations, NoiseTypes
from brainflow.board_shim import BoardShim, NDArray

from set_board import CYTON_ID
from nptyping import Float64

CYTON_SAMPLING_RATE = BoardShim.get_sampling_rate(CYTON_ID)

# Filters:

def envi_noise(data: NDArray[Float64]) -> None:
    DataFilter.remove_environmental_noise(data, CYTON_SAMPLING_RATE, NoiseTypes.FIFTY.value)

def bandpass(data: NDArray[Float64], start_freq: float, stop_freq: float, order: int = 4) -> None:
    DataFilter.perform_bandpass(data, CYTON_SAMPLING_RATE, start_freq, stop_freq, order, FilterTypes.BESSEL.value, 0)

def bandstop(data: NDArray[Float64], start_freq: float = 50, stop_freq: float = 70, order: int = 4) -> None:
    DataFilter.perform_bandstop(data, CYTON_SAMPLING_RATE, start_freq, stop_freq, order, FilterTypes.BUTTERWORTH.value, 0)

# Apply filters

def default_filtering(data: NDArray[Float64]) -> None:
    envi_noise(data)
    bandstop(data)