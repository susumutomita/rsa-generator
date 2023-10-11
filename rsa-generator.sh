#!/bin/bash

# サポートしているダイジェストアルゴリズムのリスト
SUPPORTED_DIGESTS=("md5" "sha1" "sha224" "sha256" "sha384" "sha512" "sha512-224" "sha512-256")

# ユーザーに選択肢を表示
echo "サポートしているダイジェストアルゴリズム:"
for i in "${!SUPPORTED_DIGESTS[@]}"; do
  echo "$((i+1)). ${SUPPORTED_DIGESTS[$i]}"
done

# ユーザーの選択を受け取る
read -p "選択してください (1-${#SUPPORTED_DIGESTS[@]}): " selection
DIGEST_ALGO=${SUPPORTED_DIGESTS[$((selection-1))]}

# RSAプライベートキーの生成
openssl genrsa -out private.pem 2048

# メッセージに署名
signature=$(echo -n "hello world" | openssl dgst -$DIGEST_ALGO -sign private.pem | xxd -p | tr -d \\n)
echo "Signature: $signature"

# 公開キーを抽出
openssl rsa -in private.pem -outform PEM -pubout -out public.pem

# モジュラス（n）を抽出するためのオフセットを取得
offset=$(openssl asn1parse -inform PEM -in public.pem | grep 'BIT STRING' | head -2 | tail -1 | awk '{print $1}' | cut -d: -f1)
echo "Offset for modulus: $offset"

# 適切なオフセットでモジュラスを抽出
modulus=$(openssl asn1parse -inform PEM -in public.pem -strparse $offset | grep 'prim: INTEGER' |  awk '{print $7}' | cut -d: -f2)
echo "Modulus: $modulus"
