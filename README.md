# RSA Generator

## Description

このスクリプトはRSAキーペアを生成し、指定したダイジェストアルゴリズムを用いてデータに署名を行い、関連する各種の値を出力するデモです。RSA暗号およびデジタル署名の基本的な概念を理解するために作りました。

## Requirements

- Bash
- OpenSSL

## Usage

コマンドラインからスクリプトを実行してください。ダイジェストアルゴリズムの選択肢が表示されるので、選択してください：

```bash
bash rsa-signature-generator.sh
```

## Output

スクリプトは以下の値を出力します：

- `Signature`: データのRSAデジタル署名
- `Offset for modulus`: モジュラスを抽出するためのオフセット
- `Modulus`: RSAで使用されるモジュラス

例：

```bash
Signature: hex_string_here
Offset for modulus: offset_value_here
Modulus: hex_string_here
```

## Customization

ダイジェストアルゴリズムはスクリプト実行時に選択できます。サポートしているアルゴリズムは "md5", "sha1", "sha224", "sha256", "sha384", "sha512", "sha512-224", "sha512-256" です。
