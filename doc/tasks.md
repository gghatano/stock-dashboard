# Stock Dashboard タスクリスト

> 本タスクリストは `doc/requirements.md` に基づき作成

---

## Phase 1: UI素案（ダミー表示）

- [ ] プロジェクト初期化（Vite + React + TypeScript）
- [ ] 基本レイアウト作成（ヘッダー、メインエリア）
- [ ] IndexCardコンポーネント作成
- [ ] ダミーデータでのチャート表示（Recharts）
- [ ] 通貨切替トグル実装
- [ ] レスポンシブ対応（PC/モバイル）

---

## Phase 2: FastAPI API実装

- [ ] FastAPIプロジェクト初期化
- [ ] /health エンドポイント実装
- [ ] /api/indices エンドポイント実装
- [ ] yfinanceでのデータ取得実装
- [ ] フォールバック処理（ダミーデータ返却）

---

## Phase 3: API連携

- [ ] フロントエンドからAPI呼び出し実装
- [ ] 取得データの画面反映
- [ ] エラーハンドリング（isFallbackフラグ対応）

---

## Phase 4: 静的配信設定

- [ ] フロントエンドビルド設定
- [ ] FastAPIで dist ディレクトリを静的配信

---

## Phase 5: Railwayデプロイ

- [ ] railway.toml または nixpacks.toml 作成
- [ ] デプロイ実行
- [ ] 動作確認
- [ ] README.md に起動手順記載

---

## 完了条件（Definition of Done）

- [ ] Railway URL で公開
- [ ] 2カード + チャート表示
- [ ] 通貨切替動作
- [ ] データ取得失敗時もUI表示継続
- [ ] README に起動手順記載済み
