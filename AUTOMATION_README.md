# 🚀 GitHub Pages 自动化配置指南

## 📋 配置步骤

### 步骤 1：创建 GitHub 仓库

1. 访问：https://github.com/new
2. 填写信息：
   - **Repository name**: `daily-summary`
   - **Description**: Daily NASDAQ summary reports
   - **Visibility**: **Public** (公开)
   - **Initialize with**: **None**

### 步骤 2：创建 GitHub Token

1. 访问：https://github.com/settings/tokens
2. 选择权限：
   - ✅ `Public_repo`
   - ✅ `repo`
3. 复制 Token (只显示一次！)

### 步骤 3：配置 Token

修改脚本中的 Token：

```bash
# 编辑脚本
nano /opt/data/notes/daily-summary/push-to-github.sh

# 找到这一行，替换成你的 Token：
GITHUB_TOKEN="YOUR_TOKEN_HERE"

# 替换为：
GITHUB_TOKEN="ghp_xxxxxx..."
```

### 步骤 4：首次推送

```bash
cd /opt/data/notes/daily-summary/
bash push-to-github.sh
```

### 步骤 5：开启 GitHub Pages

1. 访问：https://github.com/steveyu2026/daily-summary/settings/pages
2. 选择 **Source** → **GitHub Actions**
3. 保存

### 步骤 6：手机访问

访问地址：
```
https://steveyu2026.github.io/daily-summary/
```

---

## 🎯 自动化脚本

我已经创建了自动化脚本：

```bash
/opt/data/notes/daily-summary/push-to-github.sh
```

### 功能：
- ✅ 生成每日报告
- ✅ 自动推送到 GitHub
- ✅ 支持 Markdown 格式

### 使用方法：

```bash
# 每天手动运行
cd /opt/data/notes/daily-summary/
bash push-to-github.sh

# 或者配置定时任务 (crontab)
crontab -e

# 添加以下内容 (每天 6:30 运行)
30 6 * * * cd /opt/data/notes/daily-summary && bash push-to-github.sh
```

---

## 📱 手机访问

### 访问方式：

**方式 1：浏览器访问**
```
https://steveyu2026.github.io/daily-summary/
```

**方式 2：GitHub App**
- 下载 GitHub 手机 App
- 访问仓库页面
- 查看最新报告

**方式 3：Telegram Bot** (可选)
- 创建 Telegram Bot
- 设置定时推送链接

---

## 🔧 配置定时任务

### 每天 6:30 自动推送：

```bash
# 编辑 crontab
crontab -e

# 添加以下内容：
30 6 * * * cd /opt/data/notes/daily-summary && bash push-to-github.sh >> /tmp/daily-summary.log 2>&1
```

### 查看日志：

```bash
cat /tmp/daily-summary.log
```

---

## 🎯 完成清单

- [ ] 创建 GitHub 仓库 `daily-summary`
- [ ] 创建 GitHub Personal Access Token
- [ ] 替换脚本中的 Token
- [ ] 运行首次推送脚本
- [ ] 开启 GitHub Pages
- [ ] 配置定时任务
- [ ] 手机访问测试

---

## 📱 最终效果

**每天早上 7:00 北京时间：**
1. ⏰ 报告自动生成
2. 📤 自动推送到 GitHub
3. 📱 手机访问：https://steveyu2026.github.io/daily-summary/

---

## 💡 提示

- **Token 安全**: 不要将 Token 分享给他人
- **备份**: GitHub 会自动备份所有报告
- **历史**: 支持查看历史版本
- **格式**: 支持 Markdown 预览

---

**需要我帮你完成配置吗？** 🚀

告诉我你的 GitHub Token，我可以帮你完成配置！
