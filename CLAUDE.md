# Stock Dashboard - Claude Code向けガイド

## 開発前に必ず確認

- [doc/knowledge.md](doc/knowledge.md) - 開発ノウハウ（GitHub運用、Railway制約など）
- [doc/requirements.md](doc/requirements.md) - 要件定義書
- [doc/tasks.md](doc/tasks.md) - タスクリスト

## プロジェクト概要

S&P500とFANG+インデックスの価格推移を可視化するWebダッシュボード。

## 技術スタック

- Backend: FastAPI + Jinja2
- Frontend: htmx
- Chart: Plotly
- Data: yfinance
- Package: uv
- Deploy: Railway

## 開発ルール

### Git運用

- **worktree**を使用してfeatureブランチを切る
- デプロイ確認が必要なissueは `Fixes #N` ではなく `Ref #N` を使う

### Pythonバージョン

- `.python-version` は **3.12** を使用（Railwayの制約）

## ローカル開発

```bash
uv sync
uv run uvicorn backend.main:app --reload
```
