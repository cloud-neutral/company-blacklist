# 🖤 公司黑名单

> 合并多个来源的公司黑名单，求职避坑指南

## 数据来源

| 来源 | 说明 |
|------|------|
| [996ICU.job.blacklist_company](https://github.com/it-job-blacklist/996ICU.job.blacklist_company) | 996/ICU 黑名单公司 |
| [project-china-company-blacklist](https://hsiong.github.io/project-china-company-blacklist/) | 华人公司黑名单 |

## 目录结构

```
company-blacklist/
├── README.md
├── Shanghai.md          # 上海黑名单
├── Beijing.md           # 北京黑名单
├── Shenzhen.md          # 深圳黑名单
├── Guangzhou.md         # 广州黑名单
├── Hangzhou.md          # 杭州黑名单
├── all.md               # 完整黑名单（不分城市）
└── scripts/
    └── check.py         # 检查公司是否在黑名单中
```

## 集成到每日求职流程

在筛选职位时，使用以下命令检查公司是否在黑名单中：

```bash
# 检查公司
python3 scripts/check.py "公司名称"

# 或直接在求职汇总中使用
grep -i "公司名称" all.md
```

## 贡献指南

1. 提交 PR 时请注明来源和具体问题
2. 问题类型：996、拖欠工资、试用期裁员、恶意加班等
3. 请提供具体地址或可验证信息

## 更新日志

- **2026-03-12**: 初始化仓库，合并 996ICU 黑名单