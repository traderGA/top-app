

def ticker_serial(ticker) -> dict:
    return {
        'id': str(ticker['_id']),
        'symbol': ticker['symbol'],
        'name': ticker['name'],
        'primary_exchange': ticker['primary_exchange'],
        'type': ticker['type'],
        'list_date': ticker['list_date'],
        'sector': ticker['sector'],
        'group': ticker['group'],
        'industry': ticker['industry'],
        'sub_industry': ticker['sub_industry']
    }

def list_tickers(tickers) -> list:
    return [ticker_serial(ticker) for ticker in tickers]
    
def daily_bar_serial(daily_bar) -> dict:
    return {
        'id': str(daily_bar['_id']),
        'symbol': daily_bar['symbol'],
        'v': daily_bar['v'],
        'o': daily_bar['o'],
        'c': daily_bar['c'],
        'h': daily_bar['h'],
        'l': daily_bar['l'],
        't': daily_bar['t'],
        'volsma20': daily_bar['volsma20'],
        'volsma30': daily_bar['volsma30'],
        'volsma50': daily_bar['volsma50'],
        'dv': daily_bar['dv'],
        'dv20': daily_bar['dv20'],
        'dv30': daily_bar['dv30'],
        'dv50': daily_bar['dv50'],
        'sma5': daily_bar['sma5'],
        'sma10': daily_bar['sma10'],
        'sma20': daily_bar['sma20'],
        'sma50': daily_bar['sma50'],
        'sma100': daily_bar['sma100'],
        'sma150': daily_bar['sma150'],
        'sma200': daily_bar['sma200'],
        'ema4': daily_bar['ema4'],
        'ema5': daily_bar['ema5'],
        'ema8': daily_bar['ema8'],
        'ema9': daily_bar['ema9'],
        'ema10': daily_bar['ema10'],
        'ema20': daily_bar['ema20'],
        'ema21': daily_bar['ema21'],
        'ema65': daily_bar['ema65'],
        'tr': daily_bar['tr'],
        'atr3': daily_bar['atr3'],
        'atr5': daily_bar['atr5'],
        'atr10': daily_bar['atr10'],
        'atr14': daily_bar['atr14'],
        'atr20': daily_bar['atr20'],
        'dr': daily_bar['dr'],
        'adr3': daily_bar['atr3'],
        'adr5': daily_bar['atr5'],
        'adr10': daily_bar['atr10'],
        'adr14': daily_bar['atr14'],
        'adr20': daily_bar['atr20'],
        'roc1w': daily_bar['roc1w'],
        'roc1m': daily_bar['roc1m'],
        'roc3m': daily_bar['roc3m'],
        'roc6m': daily_bar['roc6m'],
        'as1w': daily_bar['as1w'],
        'as1m': daily_bar['as1m'],
        'as3m': daily_bar['as3m'],
        'as6m': daily_bar['as6m'],
        'cycle': daily_bar['cycle']
    }

def list_daily_bars(daily_bars) -> list:
    return [daily_bar_serial(daily_bar) for daily_bar in daily_bars]

def daily_cycle_serial(daily_cycle) -> dict:
    return {
        'id': str(daily_cycle['_id']),
        'date': daily_cycle['date'],
        'total': daily_cycle['total'],
        'uptrend': daily_cycle['uptrend'],
        'pullback': daily_cycle['pullback'],
        'mini_base': daily_cycle['mini_base'],
        'base': daily_cycle['base'],
        'up_right_side': daily_cycle['up_right_side'],
        'off_bottom': daily_cycle['off_bottom'],
        'below_200sma': daily_cycle['below_200sma']
    }

def list_daily_cycles(daily_cycles) -> list:
    return [daily_cycle_serial(daily_cycle) for daily_cycle in daily_cycles]

def filter_param_serial(filter_param) -> dict:
    return {
        'id': str(filter_param['_id']),
        'name': filter_param['name'],
        'arg1': filter_param['arg1'],
        'operator': filter_param['operator'],
        'arg2': filter_param['arg2']
    }

def list_filter_params(filter_params) -> list:
    return [filter_param_serial(filter_param) for filter_param in filter_params]

def filter_serial(filter) -> dict:
    return {
        'id': str(filter['_id']),
        'name': filter['name'],
        'arg1': filter['arg1'],
        'operator': filter['operator'],
        'arg2': filter['arg2']
    }

def list_filters(filters) -> list:
    return [filter_serial(filter) for filter in filters]

def screen_serial(screen) -> list:
    return {
        'id': str(screen['_id']),
        'name': screen['name'],
        'filters': list_filters(screen['filters'])
    }

def list_screens(screens) -> list:
    return [screen_serial(screen) for screen in screens]