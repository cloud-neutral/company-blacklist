#!/usr/bin/env python3
"""
公司黑名单检查工具
用法: python3 check.py "公司名称"
"""

import sys
import os
import re

# 黑名单目录
BLACKLIST_DIR = os.path.dirname(os.path.abspath(__file__)) + "/.."

def load_blacklist(city=None):
    """加载黑名单"""
    files = []
    if city:
        files.append(f"{city}.md")
    files.append("all.md")
    
    blacklist = {}
    for filename in files:
        filepath = os.path.join(BLACKLIST_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                # 提取公司名称
                matches = re.findall(r'\|\s*([^|\n]+?)\s*\|', content)
                for match in matches:
                    company = match.strip()
                    if company and not company.startswith('-') and not company.startswith('---') and len(company) > 1:
                        if company not in blacklist:
                            blacklist[company] = filename
    return blacklist

def check_company(company_name, city=None):
    """检查公司是否在黑名单中"""
    blacklist = load_blacklist(city)
    
    # 模糊匹配
    results = []
    for company, source in blacklist.items():
        if company_name.lower() in company.lower() or company.lower() in company_name.lower():
            results.append((company, source))
    
    return results

def main():
    if len(sys.argv) < 2:
        print("用法: python3 check.py \"公司名称\" [城市]")
        print("例如: python3 check.py \"字节跳动\" Shanghai")
        sys.exit(1)
    
    company_name = sys.argv[1]
    city = sys.argv[2] if len(sys.argv) > 2 else None
    
    results = check_company(company_name, city)
    
    if results:
        print(f"⚠️  发现 {len(results)} 个匹配:")
        for company, source in results:
            print(f"  - {company} (来自: {source})")
    else:
        print(f"✅ 未在黑名单中找到: {company_name}")
    
    # 也检查所有城市
    all_results = check_company(company_name)
    if all_results and not city:
        print(f"\n📍 其他城市匹配:")
        for company, source in all_results:
            if source.endswith('.md') and source != 'all.md':
                print(f"  - {company} ({source.replace('.md', '')})")

if __name__ == "__main__":
    main()