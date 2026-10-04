# docsディレクトリの運用ルール
## ドキュメントMarkdownファイルの作成ルール
- docs ディレクトリ配下に作成される Markdown ファイルにはメタ情報として yaml フロントマター を記載してください
- document_type ごとに yamlフロントマターに含まれる要素は変化します
- yamlフロントマターにどのような要素を含めるべきかは当該ドキュメントディレクトリのREADME.mdに記載します
- README.md にはフロントマターを記載しません(GitHub 上で表示した際の可読性を保つため)

### yamlフロントマターの例

```yaml
document_type: some-document-type
status: some-status
created_at: yyyy-MM-dd
```

## ディレクトリ一覧
- [workflow](workflow/README.md) — 開発作業の進め方
- [coding-standards](coding-standards/README.md) — コード規約
- [spec](spec/README.md) — プロダクトの外部仕様
- [adr](adr/README.md) — 設計上の決定記録
- [design-notes](design-notes/README.md) — 実装前の設計メモ(使い捨て)
- [investigation](investigation/README.md) — 調査メモ(使い捨て・gitignore対象)
