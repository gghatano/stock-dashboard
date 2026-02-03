# Stock Dashboard

S&P500 および FANG+ インデックスの価格推移を円建て/ドル建てで可視化する軽量Webダッシュボード。

## 技術スタック

- **Backend**: FastAPI + Jinja2
- **Frontend**: htmx
- **Chart**: Plotly
- **Data**: yfinance
- **Package**: uv

## ローカル開発

### 前提条件

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

### セットアップ

```bash
# 依存関係インストール
uv sync

# 開発サーバー起動
uv run uvicorn backend.main:app --reload
```

ブラウザで http://localhost:8000 を開く。

## API

### GET /health

ヘルスチェック

```json
{ "status": "ok" }
```

### GET /api/indices

インデックスデータ取得

```json
{
  "sp500": { "name": "S&P500", "prices": [...], "latest": 5800.0, "previous": 5780.0 },
  "fang": { "name": "FANG+", "prices": [...], "latest": 12000.0, "previous": 11900.0 },
  "exchangeRate": 150.23,
  "isFallback": false
}
```

## デプロイ (Railway)

```bash
railway up
```
