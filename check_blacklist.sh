#!/bin/bash
# 检查公司是否在黑名单中

COMPANY=$1

if [ -z "$COMPANY" ]; then
    echo "用法: ./check_blacklist.sh \"公司名称\""
    exit 1
fi

echo "🔍 检查公司: $COMPANY"
echo "---"

# 检查所有黑名单
FOUND=0

for file in *.md; do
    if [ "$file" = "README.md" ] || [ "$file" = "check_blacklist.sh" ]; then
        continue
    fi
    
    if grep -qi "$COMPANY" "$file" 2>/dev/null; then
        echo "⚠️  在 $file 中发现"
        grep -i "$COMPANY" "$file" | head -3
        FOUND=1
    fi
done

if [ $FOUND -eq 0 ]; then
    echo "✅ 未在黑名单中发现该公司"
fi