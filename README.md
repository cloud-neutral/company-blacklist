# 🖤 公司黑名单

> 合并多个来源的公司黑名单，求职避坑指南

## 数据来源

| 来源 | 说明 |
|------|------|
| [996ICU.job.blacklist_company](https://github.com/it-job-blacklist/996ICU.job.blacklist_company) | 996/ICU 黑名单公司 |
| [project-china-company-blacklist](https://hsiong.github.io/project-china-company-blacklist/) | 中国外包公司黑名单 |

## 目录结构

```
company-blacklist/
├── README.md                # 本文件
├── Shanghai.md              # 上海黑名单
├── all.md                   # 完整黑名单（不分城市）
├── outsourcing.md            # 外包公司黑名单
├── blacklist-check.sh       # 检查公司是否在黑名单中
└── .github/
    └── workflows/
        └── update.yml       # 定期更新黑名单
```

## 如何使用

### 检查公司是否在黑名单

```bash
# 方法1: 使用 grep
grep -i "公司名称" all.md

# 方法2: 使用脚本
./blacklist-check.sh "公司名称"
```

### 集成到求职流程

在获取新的职位后，先检查公司是否在黑名单中，再决定是否投递。

## 更新日志

- **2026-03-12**: 初始化仓库，合并两个数据源