#!/bin/bash
# 自动推送到 GitHub Pages 脚本

cd /opt/data/notes/daily-summary/

echo "🔄 正在生成每日报告..."
echo "📅 日期：$(date +%Y-%m-%d)"

# 生成报告
python3 daily-summary-china.py

# 添加到 Git
git add .
git commit -m "Update daily report $(date +%Y-%m-%d)"

# 配置远程仓库
git remote set-url origin https://steveyu2026@github.com/steveyu2026/Hermes_Assitant.git

# 推送到 GitHub
echo "📤 正在推送到 GitHub..."
git push origin master

echo "✅ 报告已推送！"
echo "📱 访问地址：https://steveyu2026.github.io/Hermes_Assitant/"
