# 調査メモ
実装内容の方針・制約・代替案などを議論した内容を記録する使い捨てのメモを置く

- 本 README 以外のファイルは gitignore 対象であり、リポジトリには含まれない
- 設計メモ作成時にのみ参照される。最新の仕様を把握する目的で読んではいけない
- 運用は [design-workflow.md](../workflow/design-workflow.md) を参照

## ファイル名
`<slug>.md` (slug の規則は [workflow/README.md](../workflow/README.md) を参照)

## yamlフロントマター

```yaml
document_type: investigation
created_at: yyyy-MM-dd
```

## 本文の構成

```markdown
# <依頼内容>
## 背景
なぜこの変更を検討しているか
## 方針
ユーザーと合意した方針
## 制約
方針を縛る前提・制約
## 代替案と評価
検討した選択肢と、採用・却下の理由
## 未決事項
設計タスクに先送りした論点
```
