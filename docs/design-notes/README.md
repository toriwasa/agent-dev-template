# 設計メモ
実装前の設計内容を記録するメモを置く

- 設計メモは使い捨てであり、spec/ADR昇格タスクの最後に削除される
- spec・ADR・コードコメントから設計メモを参照しない
- 必須の節や運用は [design-workflow.md](../workflow/design-workflow.md) と [implementation-workflow.md](../workflow/implementation-workflow.md) を参照

## ファイル名
`<slug>.md` (slug の規則は [workflow/README.md](../workflow/README.md) を参照)

## yamlフロントマター

```yaml
document_type: design-note
status: draft
created_at: yyyy-MM-dd
```

| status | 意味 |
|---|---|
| draft | ユーザーが設計メモを確定する前 |
| approved | ユーザーが確定済み。設計PR作成時に更新する |

- 実装の進捗は status ではなく Plan のチェックボックスで管理する
