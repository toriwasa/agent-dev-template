# docsディレクトリの運用ルール
## ドキュメントMarkdownファイルの作成ルール
- docs ディレクトリ配下に作成される Markdown ファイルにはメタ情報として yaml フロントマター を記載してください
- document_type ごとに yamlフロントマターに含まれる要素は変化します
- yamlフロントマターにどのような要素を含めるべきかは当該ドキュメントディレクトリのREADME.mdに記載します

### yamlフロントマターの例

```yaml
document_type: some-document-type
status: some-status
created_at: yyyy-MM-dd
expired_at: yyyy-MM-dd
```
