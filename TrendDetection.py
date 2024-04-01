def detectTrend(data):
    prevHigh = max(data[:2])
    prevLow = min(data[:2])
    upTrendCount = 0
    downTrendCount = 0
    trend_data = [0] * len(data)
    starting_index = 0
    current_trend = 0
    prev_trend = 0
    prev_data = data[1]
    for i in range(2, len(data)):
        if data[i] < prev_data:
            if data[i] > prevLow:
                upTrendCount += 1
                downTrendCount = 0
                current_trend = 1
            else:
                downTrendCount += 1
                upTrendCount = 0
                current_trend = -1
            prevLow = data[i]
        else:
            if data[i] > prevHigh:
                upTrendCount += 1
                downTrendCount = 0
                current_trend = 1
            else:
                downTrendCount += 1
                upTrendCount = 0
                current_trend = -1
            prevHigh = data[i]

        if((current_trend is not prev_trend and i - starting_index >= 3)):
            for i in range(starting_index, i):
                trend_data[i] = prev_trend
        if(i == len(data) - 1):
            if(current_trend == prev_trend):
                for i in range(starting_index, i + 1):
                    trend_data[i] = prev_trend
            else:
                trend_data[len(data) - 1] = 0
        
        if(current_trend is not prev_trend):
            starting_index = i
        prev_trend = current_trend
        prev_data = data[i]

    return trend_data
