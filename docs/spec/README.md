# spec
プロダクトが外から見てどのようなインターフェース・振る舞いを持つかを記述する。最新の仕様を把握する際はこのディレクトリを参照する

- 機能・ユースケース単位で1ファイルとする(例: CSVエクスポート、実験定義の読み込み)
- 内部実装の説明は書かず、ソースコードの docstring に任せる
- 作成・更新は [implementation-workflow.md](../workflow/implementation-workflow.md) の spec/ADR昇格タスクで行う

## ファイル名
`<機能名の kebab-case>.md` (例: `csv-export.md`)

## yamlフロントマター

```yaml
document_type: spec
status: active
created_at: yyyy-MM-dd
updated_at: yyyy-MM-dd
sources:
  - src/project-name/...
```

| 項目 | 内容 |
|---|---|
| status | `active`: 現行の仕様 / `deprecated`: 廃止された機能(削除せず残す) |
| updated_at | 最後に spec を更新した日 |
| sources | この spec が記述するソースファイルのパス一覧。整合レビューの検証範囲として使う |

## 本文の構成

```markdown
# <機能名>
## 概要
その機能が何をするか
## インターフェース
入出力、公開関数、CLIコマンドなど外から見える部分
## 振る舞い
正常系、異常系、境界条件
## 制約・前提
```
