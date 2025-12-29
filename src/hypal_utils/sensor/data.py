from pydantic import BaseModel, ConfigDict

from hypal_utils.candles import Candle_OHLC


class Sensor_Data(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    source: str
    unit: str
    detectors: list[Candle_OHLC]
