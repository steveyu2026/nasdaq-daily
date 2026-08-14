#!/bin/bash
# 自动推送所有本地文件到 GitHub
# 永久有效的规则 - 所有新文件自动推送

# 配置（Token 从环境变量读取）
GITHUB_USER="${GITHUB_USER:-steveyu2026}"
GITHUB_REPO="${GITHUB_REPO:-nasdaq-daily}"
GITHUB_TOKEN="${GITHUB_TOKEN:-}"
WORKDIR="/opt/data/notes/daily-summary"
LOG_FILE="/tmp/github-push.log"

# 日志
echo "[$(date '+%Y-%m-%d %H:%M:%S')] 开始自动推送..." >> $LOG_FILE

# 切换到工作目录
cd $WORKDIR

# 检查是否有未提交的文件
if [ -n "$(git status --porcelain)" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 发现未提交的文件，开始推送..." >> $LOG_FILE
    
    # 添加所有文件
    git add .
    
    # 生成提交信息
    LATEST_REPORT=$(ls -t 2026-*.md | head -1 || echo "daily-report")
    COMMIT_MSG="Auto-push: Update files at $(date '+%Y-%m-%d %H:%M:%S')"
    
    # 提交（使用 GitHub Actions 作为作者）
    git commit -m "$COMMIT_MSG" --author="GitHub Actions <actions@github.com>"
    
    # 推送到 GitHub
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 推送到 GitHub: ${GITHUB_USER}/${GITHUB_REPO}" >> $LOG_FILE
    git push "https://${GITHUB_TOKEN}@github.com/${GITHUB_USER}/${GITHUB_REPO}.git" master
    
    # 提交成功
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ 推送成功!" >> $LOG_FILE
    echo "✅ 推送成功！"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 没有新文件需要推送" >> $LOG_FILE
    echo "✅ 没有新文件需要推送"
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 完成" >> $LOG_FILE
