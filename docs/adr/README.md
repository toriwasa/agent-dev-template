# ADR (Architecture Decision Record)
設計上の決定とその理由を記録する

- 設計メモの「代替案と却下理由 Why Not」に検討に値する代替案があった場合のみ作成する
- 1つの作業から複数の ADR を作成してよい
- 設計メモは削除されるため、ADR 単体で意味が通るように背景を書き切る。設計メモの slug やパスは記載しない
- 作成は [implementation-workflow.md](../workflow/implementation-workflow.md) の spec/ADR昇格タスクで行う

## ファイル名
`yyyy-MM-dd-<決定内容の kebab-case>.md`

- 日付は ADR の作成日
- 例: `2026-10-20-use-stdlib-csv-writer.md`

## yamlフロントマター

```yaml
document_type: adr
status: accepted
created_at: yyyy-MM-dd
superseded_by: yyyy-MM-dd-xxx.md
```

| 項目 | 内容 |
|---|---|
| status | `accepted`: 有効な決定 / `superseded`: 後続の ADR で置き換えられた決定(削除せず残す) |
| superseded_by | `superseded` の場合のみ、後継 ADR のファイル名を記載する |

## 本文の構成

```markdown
# <決定内容>
## 背景
## 決定内容
## 代替案と却下理由
## 影響
```
