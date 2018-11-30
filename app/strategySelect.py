
stock_strategy = {
    "ethicalInvest": {"AAPL": 0.3, "ADBE": 0.2, "MSFT": 0.2, "INTC": 0.2, "TSLA": 0.1},
    "growthInvest": {"EXEL": 0.3, "MB": 0.2, "NKE": 0.3, "SQ": 0.2},
    "indexInvest": {"VTI": 0.3, "IXUS": 0.3, "ILTB": 0.4},
    "qualityInvest": {"MA": 0.3, "BABA": 0.25, "TSM": 0.2, "V": 0.25},
    "valueInvest": {"IAG": 0.15, "LPX": 0.15, "SAFM": 0.1, "TWTR": 0.35, "ZG": 0.25}
    }

def getPortionList(strategy):
    portionList = {}
    strategyAmount = len(strategy)
    for option in strategy:
        initList = stock_strategy[option]
        for key, val in initList.items():
            portionList[key] = val / strategyAmount

    return portionList
