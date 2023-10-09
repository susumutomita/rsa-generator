# RSA Generator

## Description

このスクリプトはRSAキーペアを生成し、データに署名を行い、関連する各種の値を出力するデモです。RSA暗号およびデジタル署名の基本的な概念を理解するために作りました。

## Requirements

- Python 3.x
- cryptographyライブラリ

必要なPythonパッケージはpipを使用してインストールできます：

```bash
pip install -r requirements.txt
```

## Usage

コマンドラインからスクリプトを実行し、署名したいデータを引数として渡してください：

```bash
python3 rsa-generator.py "your_data_here"
```

## Output

スクリプトは以下を含むJSONオブジェクトを出力します：

- `DIGEST`: データのSHA-256ハッシュ
- `SHA256_HASHED`: データのSHA-256ハッシュ（DIGESTと同じ）
- `EXPONENT`: RSAで使用される公開指数
- `SIGNATURE`: データのRSAデジタル署名
- `MODULUS`: RSAで使用されるモジュラス
- `DECIPHER_RESULT`: 署名の検証結果（"Signature verification succeeded" または "Signature verification failed"）

例：

```result.json
{
  "DIGEST": "hex_string_here",
  "SHA256_HASHED": "hex_string_here",
  "EXPONENT": "hex_string_here",
  "SIGNATURE": "hex_string_here",
  "MODULUS": "hex_string_here",
  "DECIPHER_RESULT": "0x0001f...（省略）"
}
```
