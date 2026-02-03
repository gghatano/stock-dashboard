# Stock Dashboard タスクリスト

> 本タスクリストは `doc/requirements.md` に基づき作成
> 技術スタック変更: React → htmx + Jinja2, Recharts → Plotly

---

## Phase 0: Git初期化

- [x] git init
- [x] 初期コミット（doc/のみ）
- [x] worktree/feature-htmx ブランチ作成

---

## Phase 1: プロジェクト基盤

- [x] uv init でプロジェクト初期化
- [x] pyproject.toml に依存関係追加
- [x] FastAPIアプリ作成
- [x] Jinja2テンプレート設定
- [x] 静的ファイル配信設定
- [x] htmx CDN読み込み

---

## Phase 2: UI実装

- [x] base.html（レイアウト、htmx読み込み）
- [x] index.html（ヘッダー、カードエリア）
- [x] cards.html（IndexCard × 2）
- [x] style.css（レスポンシブ対応）
- [x] 通貨切替トグル（htmx hx-get）

---

## Phase 3: データ取得・チャート

- [x] yfinanceでS&P500, FANG+, USD/JPY取得
- [x] フォールバック処理（ダミーデータ）
- [x] Plotly で折れ線グラフ生成（HTML埋め込み）
- [x] /api/indices エンドポイント
- [x] /health エンドポイント

---

## Phase 4: htmx連携

- [x] /partial/cards エンドポイント（HTML部分返却）
- [x] 通貨切替時のカード更新
- [x] isFallback時の警告表示

---

## Phase 5: デプロイ

- [x] railway.toml作成
- [ ] デプロイ実行
- [ ] 動作確認
- [x] README.md に起動手順記載

---

## 完了条件（Definition of Done）

- [ ] Railway URL で公開
- [x] 2カード + チャート表示
- [x] 通貨切替動作
- [x] データ取得失敗時もUI表示継続
- [x] README に起動手順記載済み
