from pydantic import BaseModel
from enum import Enum

class Ticker(BaseModel):
    symbol: str
    name: str
    primary_exchange: str
    type: str
    list_date: str | None = None
    sector: str | None = None  
    group: str | None = None  
    industry: str | None = None  
    sub_industry: str | None = None  

class Cycle(Enum):
    uptrend = 'UPTREND'
    pullback = 'PULLBACK'
    mini_base = 'MINI BASE'
    base = 'BASE'
    up_right_side = 'UP RIGHT SIDE'
    off_bottom = 'OFF BOTTOM'
    below_200sma = 'BELOW 200SMA'

class DailyBar(BaseModel):
    symbol: str
    v: float
    o: float
    c: float
    h: float
    l: float
    t: float
    volsma20: float | None = None
    volsma30: float | None = None
    volsma50: float | None = None
    dv: float | None = None
    dv20: float | None = None
    dv30: float | None = None
    dv50: float | None = None
    sma5: float | None = None
    sma10: float | None = None
    sma20: float | None = None
    sma50: float | None = None
    sma100: float | None = None
    sma150: float | None = None
    sma200: float | None = None
    ema4: float | None = None
    ema5: float | None = None
    ema8: float | None = None
    ema9: float | None = None
    ema10: float | None = None
    ema20: float | None = None
    ema21: float | None = None
    ema65: float | None = None
    tr: float | None = None
    atr3: float | None = None
    atr5: float | None = None
    atr10: float | None = None
    atr14: float | None = None
    atr20: float | None = None
    dr: float | None = None
    adr3: float | None = None
    adr5: float | None = None
    adr10: float | None = None
    adr14: float | None = None
    adr20: float | None = None   
    roc1w: float | None = None
    roc1m: float | None = None
    roc3m: float | None = None
    roc6m: float | None = None
    as1w: float | None = None
    as1m: float | None = None
    as3m: float | None = None
    as6m: float | None = None
    cycle: Cycle | None = None

class DailyCycle(BaseModel):
    date: str
    total: int
    uptrend: int
    pullback: int
    mini_base: int
    base: int
    up_right_side: int
    off_bottom: int
    below_200sma: int

class MathOperator(Enum):
    plus = 'PLUS'
    minus = 'MINUS'
    mulitply = 'MULTIPLY'
    divide = 'DIVIDE'

class FilterParameter(BaseModel):
    name: str | None
    arg1: None = None
    operator: MathOperator
    arg2: None = None

class BoolOperator(Enum):
    gt = 'GT'
    gte = 'GTE'
    lt = 'LT'
    lte = 'LTE'
    eq = 'EQ'

class Filter(BaseModel):
    name: str | None
    arg1: None = None
    operator: BoolOperator
    arg2: None = None

class Screen(BaseModel):
    name: str
    filters: list[Filter]





