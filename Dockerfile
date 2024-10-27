# ベースイメージをPython 3.10に設定
FROM python:3.10-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要なライブラリをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Pythonライブラリをインストール
RUN pip install --no-cache-dir duckdb pandas

# アプリケーションコードをコンテナにコピー
COPY ./src .

# エントリーポイントを設定（後ほど説明するPythonスクリプトを実行）
CMD ["python", "app.py"]
