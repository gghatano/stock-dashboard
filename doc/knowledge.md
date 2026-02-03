# 開発ノウハウ

## GitHub Issue管理

### 自動クローズに注意

コミットメッセージやPR本文に以下のキーワードを含めると、PRマージ時にissueが**自動クローズ**される：

- `Fixes #N`
- `Closes #N`
- `Resolves #N`

#### 使い分け

| 状況 | 使うべきキーワード |
|------|-------------------|
| コード修正のみで完了するissue | `Fixes #N` |
| デプロイ確認が必要なissue | `Ref #N` または `Related to #N` |
| 複数PRにまたがるissue | `Ref #N` |

#### 例

```
# デプロイ確認が必要な場合
fix: Change Python version to 3.12 for Railway compatibility

Ref #2
```

---

## Railway / Nixpacks

### Pythonバージョンの制約

RailwayのNixpacks環境では、最新のPythonバージョンがサポートされていない場合がある。

#### 推奨

- `.python-version` は安定版を指定（例: `3.12`）
- 最新版（3.14等）は避ける
- `pyproject.toml` の `requires-python` も合わせて確認

#### エラー例

```
error: No interpreter found for Python 3.14 in managed installations or system path
```

#### 対処

1. `.python-version` を `3.12` 等に変更
2. `uv.lock` を再生成（`rm uv.lock && uv sync`）
3. ローカルで動作確認後にデプロイ
