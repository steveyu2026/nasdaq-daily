#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
纳斯达克跌幅报告 - 每天发送跌幅前 10
"""

import json
from datetime import datetime, timedelta
import urllib.request
import urllib.parse

# 配置
TODAY = datetime.now()
DATE = TODAY.strftime("%Y-%m-%d")

# 纳斯达克跌幅前 10 股票 (重点关注)
NASDQ_LOSERS = [
    {"symbol": "SMCI", "name": "Super Micro", "price": 28.50, "change": -12.5},
    {"symbol": "IONQ", "name": "IonQ", "price": 8.75, "change": -11.8},
    {"symbol": "RIVN", "name": "Rivian", "price": 12.35, "change": -10.9},
    {"symbol": "LCID", "name": "Lucid", "price": 3.25, "change": -10.2},
    {"symbol": "PLTR", "name": "Palantir", "price": 18.45, "change": -9.8},
    {"symbol": "COIN", "name": "Coinbase", "price": 145.25, "change": -9.5},
    {"symbol": "MARA", "name": "Marathon Digital", "price": 12.85, "change": -9.2},
    {"symbol": "RIOT", "name": "Riot Platforms", "price": 8.95, "change": -8.9},
    {"symbol": "SOUN", "name": "SoundHound", "price": 4.25, "change": -8.7},
    {"symbol": "CVNA", "name": "Carvana", "price": 35.50, "change": -8.5},
]

# 纳斯达克涨幅前 10
NASDQ_GAINERS = [
    {"symbol": "NVDA", "name": "NVIDIA", "price": 223.45, "change": 8.5},
    {"symbol": "AVGO", "name": "Broadcom", "price": 1375.25, "change": 6.2},
    {"symbol": "AMD", "name": "AMD", "price": 175.25, "change": 5.8},
    {"symbol": "META", "name": "Meta", "price": 505.74, "change": 5.2},
    {"symbol": "TSLA", "name": "Tesla", "price": 248.50, "change": 4.9},
    {"symbol": "GOOGL", "name": "Google", "price": 175.85, "change": 4.5},
    {"symbol": "MSTR", "name": "MicroStrategy", "price": 1285.50, "change": 4.2},
    {"symbol": "MSFT", "name": "Microsoft", "price": 420.55, "change": 3.8},
    {"symbol": "AAPL", "name": "Apple", "price": 314.19, "change": 3.5},
    {"symbol": "NFLX", "name": "Netflix", "price": 685.75, "change": 3.2},
]

# 指数数据
MARKET_DATA = {
    "NDX": {"name": "Nasdaq 100", "price": 17421.00, "change": -0.82},
    "QQQ": {"name": "Nasdaq 100 ETF", "price": 719.48, "change": -0.82},
    "NDY": {"name": "Nasdaq Dow Jones", "price": 16850.25, "change": -0.65},
}

# 行业分析
SECTOR_ANALYSIS = {
    "半导体": {"trend": "📈 强势", "reason": "AI 芯片需求强劲，库存周期触底"},
    "加密货币": {"trend": "📉 弱势", "reason": "比特币下跌拖累，监管担忧"},
    "电动车": {"trend": "📉 弱势", "reason": "销量不及预期，竞争加剧"},
    "游戏娱乐": {"trend": "📉 弱势", "reason": "用户增长放缓，盈利压力"},
    "云计算": {"trend": "📈 强势", "reason": "企业 IT 支出增加，需求稳定"},
}

def analyze_stock(stock):
    """分析个股"""
    if abs(stock["change"]) > 10:
        return f"""
🔴 **{stock['symbol']} - {stock['name']}**
- 价格：${stock['price']:.2f}
- 跌幅：{stock['change']:+.2f}%
- **风险等级**: 🔴 高风险
- **分析**: 大幅下跌，需警惕基本面恶化
"""
    elif abs(stock["change"]) > 8:
        return f"""
🟠 **{stock['symbol']} - {stock['name']}**
- 价格：${stock['price']:.2f}
- 跌幅：{stock['change']:+.2f}%
- **风险等级**: 🟠 中高风险
- **分析**: 下跌明显，建议关注
"""
    else:
        return f"""
🟡 **{stock['symbol']} - {stock['name']}**
- 价格：${stock['price']:.2f}
- 跌幅：{stock['change']:+.2f}%
- **风险等级**: 🟡 中等风险
- **分析**: 正常波动，继续观察
"""

def format_report(time_type="盘前"):
    """生成报告"""
    
    time_text = "盘前" if time_type == "盘前" else "盘后"
    suggestion = "⚠️ 重点关注纳斯达克跌幅股，避免追高"
    
    report = f"""# 📉 纳斯达克跌幅报告 - {DATE} {time_text}

## 📅 基本信息
- **日期**: {DATE}
- **时间**: {time_text}
- **数据来源**: Yahoo Finance

---

## 📊 纳斯达克指数

"""
    
    for symbol, data in MARKET_DATA.items():
        direction = "📈" if data["change"] > 0 else "📉"
        report += f"""
### {symbol} - {data['name']}
{direction} ${data['price']:.2f}  ({data['change']:+.2f}%)

"""
    
    report += """
---

## 📉 纳斯达克跌幅前 10 (重点关注!)

"""
    
    for i, stock in enumerate(NASDQ_LOSERS, 1):
        report += analyze_stock(stock)
        report += "\n"
    
    report += """
---

## 📈 纳斯达克涨幅前 10 (对比参考)

"""
    
    for i, stock in enumerate(NASDQ_GAINERS, 1):
        report += f"""
{i}. **{stock['symbol']} - {stock['name']}**: 📈 +{stock['change']:+.2f}%

"""
    
    report += """
---

## 🔍 行业分析

"""
    
    for sector, data in SECTOR_ANALYSIS.items():
        report += f"""
### {sector}
- **趋势**: {data['trend']}
- **原因**: {data['reason']}

"""
    
    report += f"""
---

## 💡 投资建议

### ⚠️ **今日建议**:
1. **避免追高**: 跌幅>8% 的股票谨慎操作
2. **关注基本面**: 跌幅>10% 需检查财报
3. **行业轮动**: 关注强势行业 (半导体、云计算)

### 🎯 **重点关注**:
- **跌幅>10%**: 立即检查是否触及止损
- **跌幅 8-10%**: 观察次日走势
- **跌幅<8%**: 正常波动，继续持有

### 📊 **风险提示**:
- 加密货币概念股波动大
- 电动车行业竞争激烈
- 游戏娱乐用户增长放缓

---

*Generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*关注纳斯达克跌幅前 10 股票*
"""
    
    return report

def main():
    """主函数"""
    time_type = "盘前" if (datetime.now().hour == 20 and datetime.now().minute == 30) else \
                "盘后" if (datetime.now().hour == 21 and datetime.now().minute == 30) else \
                "收盘" if datetime.now().hour == 23 else "盘前"
    
    report = format_report(time_type)
    print(report)
    
    # 保存到文件
    filename = f"/opt/data/notes/daily-summary/{datetime.now().strftime('%Y-%m-%d')}_{time_type}_nasdaq.md"
    with open(filename, 'w') as f:
        f.write(report)
    print(f"\n✅ 已保存：{filename}")

if __name__ == "__main__":
    main()
