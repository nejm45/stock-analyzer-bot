import requests
import smtplib
import os
from email.mime.text import MIMEText

BASE_URL = "https://api.binance.com"

WARNING_COINS = [
    "JASMYUSDT",
    "WAVESUSDT",
    "STMXUSDT",
    "RSRUSDT",
]


def send_email(message):
    sender_email = os.environ.get("EMAILUSER")
    receiver_email = sender_email
    password = os.environ.get("EMAIL_PASS")

    msg = MIMEText(message)
    msg["Subject"] = "Weekly Red Candles Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()


def get_usdt_pairs():
    data = requests.get(f"{BASE_URL}/api/v3/exchangeInfo").json()
    return [
        s['symbol']
        for s in data['symbols']
        if s['quoteAsset'] == 'USDT' and s['status'] == 'TRADING'
    ]


def get_weekly_data(symbol):
    url = f"{BASE_URL}/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": "1w",
        "limit": 10
    }
    return requests.get(url, params=params).json()


def count_red_streak(klines):
    count = 0

    for candle in reversed(klines):
        open_price = float(candle[1])
        close_price = float(candle[4])

        if close_price < open_price:
            count += 1
        else:
            break

    return count


def is_strong_volume(klines):
    volumes = [float(k[5]) for k in klines]

    last_vol = volumes[-1]
    avg_vol = sum(volumes[:-1]) / (len(volumes) - 1)

    return last_vol > avg_vol * 1.5


def analyze():
    pairs = get_usdt_pairs()

    results = {2: [], 3: [], 4: [], 5: [], 6: []}

    for symbol in pairs:
        try:
            klines = get_weekly_data(symbol)

            if len(klines) < 6:
                continue

            streak = count_red_streak(klines)

            if streak >= 2:
                strong_vol = is_strong_volume(klines)

                tags = []

                if symbol in WARNING_COINS:
                    tags.append("WARNING")

                if strong_vol:
                    tags.append("VOL")

                if tags:
                    label = f"{symbol} ({' '.join(tags)})"
                else:
                    label = symbol

                if streak >= 6:
                    results[6].append(label)
                else:
                    results[streak].append(label)

        except:
            continue

    return results


if __name__ == "__main__":
    data = analyze()

    result_text = "===== RESULT =====\n\n"

    for weeks in sorted(data.keys()):
        result_text += f"{weeks} Weeks Red Candles:\n"

        if not data[weeks]:
            result_text += "   None\n"
        else:
            for coin in data[weeks]:
                result_text += f"   - {coin}\n"

        result_text += "\n"

    print(result_text)

    send_email(result_text)
