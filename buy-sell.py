def get_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        return get_float("Invalid input. " + prompt)

def get_macd_values():
    print("\nEnter MACD values:")
    macd_line = get_float("  MACD line: ")
    signal_line = get_float("  Signal line: ")
    histogram = get_float("  Histogram: ")
    return macd_line, signal_line, histogram

def make_decision(ema_short, ema_long, rsi, macd_line, signal_line, bbw, volume, vol_mc_ratio, ichimoku_trend):
    signals = []

    # EMA crossover
    if ema_short > ema_long:
        signals.append("EMA crossover: Bullish")
    else:
        signals.append("EMA crossover: Bearish")

    # RSI interpretation
    if rsi > 70:
        signals.append("RSI: Overbought")
    elif rsi < 30:
        signals.append("RSI: Oversold")
    elif rsi > 50:
        signals.append("RSI: Bullish")
    else:
        signals.append("RSI: Weak")

    # MACD
    if macd_line > signal_line:
        signals.append("MACD: Bullish crossover")
    else:
        signals.append("MACD: Bearish")

    # Volatility
    if bbw > 0.2:
        signals.append("Volatility: High")
    elif bbw < 0.05:
        signals.append("Volatility: Low")
    else:
        signals.append("Volatility: Moderate")

    # Volume/Market Cap ratio
    if vol_mc_ratio > 0.05:
        signals.append("Volume/MC: High activity")
    else:
        signals.append("Volume/MC: Normal")

    # Ichimoku trend
    signals.append(f"Ichimoku trend: {ichimoku_trend}")

    # Simple decision logic
    bullish_count = sum('Bullish' in s or 'High activity' in s for s in signals)
    bearish_count = sum('Bearish' in s or 'Overbought' in s for s in signals)

    if bullish_count >= 3:
        decision = "✅ Buy Signal"
    elif bearish_count >= 3:
        decision = "❌ Sell Signal"
    else:
        decision = "⏸️ Hold / Wait"

    print("\n--- Analysis ---")
    for s in signals:
        print("- " + s)
    print("\n📊 Final Decision:", decision)

# ===== Main Program =====
print("Manual Crypto Analysis Tool (Technical Indicators)")

ema_short = get_float("Enter short EMA: ")
ema_long = get_float("Enter long EMA: ")
rsi = get_float("Enter RSI (0-100): ")
macd_line, signal_line, histogram = get_macd_values()
bbw = get_float("Enter BBW (e.g. 0.12): ")
volume = get_float("Enter volume: ")
vol_mc_ratio = get_float("Enter volume / market cap ratio (e.g. 0.03): ")
ichimoku_trend = input("Describe Ichimoku trend (above/below cloud): ")

make_decision(ema_short, ema_long, rsi, macd_line, signal_line, bbw, volume, vol_mc_ratio, ichimoku_trend)
