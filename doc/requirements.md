了解しました。
今回は **「ゼロから再構築（greenfield）」＋「Claude Codeで段階的実装」＋「まず requirement.md を正式な一次成果物にする」** という前提ですね。

この段階は **設計判断・戦略フェーズではなく「仕様固定」フェーズ** なので、
曖昧さを排除し、Claude Code が **解釈なしで実装可能なレベルの“契約書”** として記述します。

そのまま `doc/requirement.md` として保存してください。

---

```md
# Stock Dashboard 要件定義書（requirement.md）

## 1. 目的

S&P500 および FANG+ インデックスの価格推移を  
**円建て / ドル建てで可視化する軽量Webダッシュボード** を構築する。

本アプリは以下を重視する：

- 素早い閲覧（数秒で確認できる）
- シンプルなUI（分析ツールではなく「状況把握ツール」）
- 低運用コスト（Railway単体デプロイ）
- Claude Code による段階的実装・保守可能な構成

---

## 2. スコープ

### 対象（In Scope）

- インデックス価格の取得
- 14日間の価格推移表示
- 円 / USD 表示切替
- Webブラウザ表示（PC / モバイル）
- Railway デプロイ

### 対象外（Out of Scope）

- ユーザー認証
- DB永続化
- 履歴保存
- テクニカル指標
- 高度な分析機能
- リアルタイム更新（分足など）
- SEO最適化

本システムは **参照専用・ステートレスな可視化アプリ** とする。

---

## 3. 利用者像（想定ユーザー）

- 個人投資家
- 日次で指数の概況のみ確認したい利用者

操作は「閲覧のみ」。入力は通貨切替のみ。

---

## 4. 機能要件

## 4.1 データ取得

### 必須

- S&P500 (^GSPC)
- FANG+ (^NYFANG)
- 14営業日分の日次終値
- USD/JPY 為替レート

### 取得方式

- yfinance を利用
- サーバーサイド（FastAPI）で取得

### フォールバック要件（重要）

以下の場合でも **UIは必ず表示を継続すること**

- API取得失敗
- yfinanceエラー
- FANG+ティッカー未取得

対処：

- ダミーデータ返却
- `isFallback: true` フラグ付与

---

## 4.2 API仕様

### GET /health
```

{ "status": "ok" }

```

### GET /api/indices

```

{
"sp500": {
"name": "S&P500",
"prices": [{ "date": "...", "close": 123.4 }],
"latest": 123.4,
"previous": 122.1
},
"fang": {
"name": "FANG+",
"prices": [...],
"latest": 456.7,
"previous": 450.0
},
"exchangeRate": 150.23,
"isFallback": false
}

```

---

## 4.3 画面要件

### レイアウト

#### ヘッダー
- タイトル「Stock Dashboard」
- 為替レート表示
- 通貨切替トグル（JPY / USD）

#### メイン
- IndexCard × 2
  - S&P500
  - FANG+

### 各カード内容

- 指数名
- 現在値
- 前日比（金額 / %）
- 14日折れ線グラフ

### レスポンシブ

- PC：横並び
- モバイル：縦並び

---

## 4.4 非機能要件

| 項目 | 要件 |
|--------|-------------------------|
| 起動時間 | 3秒以内 |
| 操作性 | 1クリック以内で通貨切替 |
| 可用性 | データ取得失敗でも画面表示継続 |
| 運用 | Railway 単体 |
| 保守 | Claude Code で自動実装可能な構成 |
| 依存 | OSSのみ |

---

## 5. 技術スタック

| 領域 | 技術 |
|-----------|-------------------|
| Backend | FastAPI (Python) |
| Data取得 | yfinance |
| Frontend | React + TypeScript + Vite |
| Chart | Recharts |
| Deploy | Railway |
| 配信方式 | FastAPI が dist を静的配信（単一サービス） |

---

## 6. アーキテクチャ方針

### 単一サービス構成（必須）

```

Browser
↓
FastAPI
├ API (/api)
└ Static (frontend/dist)

```

理由：

- CORS不要
- デプロイ簡素化
- Railway 1サービス運用
- Claude Code 実装容易

---

## 7. ディレクトリ構成（確定）

```

stock-dashboard/
├ backend/
│   ├ main.py
│   └ requirements.txt
├ frontend/
│   ├ src/
│   └ dist/
├ doc/
│   ├ requirement.md
│   └ design.md（後続作成）
├ railway.toml or nixpacks.toml
└ README.md

```

---

## 8. 開発原則

1. まずUIをダミーで成立させる
2. 次にAPI接続
3. 最後にデプロイ
4. 常に「動く最小単位」で進める
5. 段階的コミット

---

## 9. フェーズ計画（Claude Code実装順）

### Phase1
UI素案（ダミー表示）

### Phase2
FastAPI API実装

### Phase3
API連携

### Phase4
静的配信設定

### Phase5
Railwayデプロイ

---

## 10. 成功条件（Definition of Done）

- Railway URL で公開
- 2カード + チャート表示
- 通貨切替動作
- データ取得失敗時もUI表示継続
- README に起動手順記載済み

---

以上を本プロジェクトの正式要件とする。
```


