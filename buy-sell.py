def analyze_ema(short_ema, mid_ema, long_ema):
    if short_ema > mid_ema > long_ema:
        print("✓ EMA trend: Strong Bullish (+1)")
        return 1
    elif short_ema < mid_ema < long_ema:
        print("✗ EMA trend: Strong Bearish (+0)")
        return 0
    else:
        print("~ EMA trend: Mixed (+0)")
        return 0

def analyze_rsi(rsi):
    if rsi > 70:
        print("✗ RSI: Overbought (+0)")
        return 0
    elif rsi < 30:
        print("✓ RSI: Oversold (+1)")
        return 1
    elif 50 < rsi < 70:
        print("✓ RSI: Mild Bullish (+1)")
        return 1
    else:
        print("~ RSI: Neutral (+0)")
        return 0

def analyze_macd(macd, signal):
    if macd > signal:
        print("✓ MACD: Bullish crossover (+1)")
        return 1
    elif macd < signal:
        print("✗ MACD: Bearish crossover (+0)")
        return 0
    else:
        print("~ MACD: Neutral (+0)")
        return 0

def analyze_bbw(bbw):
    if bbw > 0.1:
        print("✓ Volatility (BBW): High → Strong movement (+1)")
        return 1
    else:
        print("✗ Volatility (BBW): Low/Moderate → Weak movement (+0)")
        return 0

def analyze_volume_mc(volume_mc):
    if volume_mc > 0.05:
        print("✓ Volume/MC: Good activity (+1)")
        return 1
    else:
        print("✗ Volume/MC: Low activity (+0)")
        return 0

def analyze_ichimoku(position):
    if position == "above":
        print("✓ Ichimoku: Above cloud → Bullish (+1)")
        return 1
    elif position == "below":
        print("✗ Ichimoku: Below cloud → Bearish (+0)")
        return 0
    else:
        print("~ Ichimoku: Inside cloud → Uncertain (+0)")
        return 0

def analyze_stoch_rsi(k, d):
    if k < 20 and d < 20:
        # في منطقة التشبع البيعي
        if k > d:
            print("✓ Stoch RSI: Oversold + Bullish crossover → Potential Buy (+1)")
            return 1
        else:
            print("✓ Stoch RSI: Oversold zone, no bullish crossover yet (+0.5)")
            return 0.5
    elif k > 80 and d > 80:
        # في منطقة التشبع الشرائي
        if k < d:
            print("✗ Stoch RSI: Overbought + Bearish crossover → Potential Sell (+0)")
            return 0
        else:
            print("✗ Stoch RSI: Overbought zone, no bearish crossover yet (+0.5)")
            return 0.5
    else:
        # خارج مناطق التشبع
        if k > d:
            print("✓ Stoch RSI: Bullish momentum (+1)")
            return 1
        elif k < d:
            print("✗ Stoch RSI: Bearish momentum (+0)")
            return 0
        else:
            print("~ Stoch RSI: No clear momentum (+0)")
            return 0


# --- USER INPUTS ---
ema_9 = float(input("EMA 9: "))
ema_26 = float(input("EMA 26: "))
ema_50 = float(input("EMA 50: "))

rsi = float(input("RSI: "))

macd = float(input("MACD Line: "))
macd_signal = float(input("MACD Signal: "))

bbw = float(input("BBW (Bollinger Band Width): "))

volume = float(input("Volume: "))
volume_mc = float(input("Volume / Market Cap: "))

ichimoku_pos = input("Ichimoku position (above / below / inside): ").strip().lower()

k = float(input("Stoch RSI %K: "))
d = float(input("Stoch RSI %D: "))

# --- ANALYSIS ---
print("\n--- Analysis Breakdown ---")
score = 0
score += analyze_ema(ema_9, ema_26, ema_50)
score += analyze_rsi(rsi)
score += analyze_macd(macd, macd_signal)
score += analyze_bbw(bbw)
score += analyze_volume_mc(volume_mc)
score += analyze_ichimoku(ichimoku_pos)
score += analyze_stoch_rsi(k, d)

print(f"\n📊 Total Bullish Points: {score}/7")

# --- FINAL DECISION ---
print("\n📈 Final Decision:", end=" ")
if score >= 5:
    print("✅ BUY")
elif score <= 2:
    print("❌ SELL")
else:
    print("⏸️ HOLD / WAIT")
