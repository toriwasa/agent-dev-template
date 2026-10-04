# コード規約

## 索引
本ディレクトリでは実装時に維持すべきコード規約を集約する。
実装レビュー時やコーディング時の方針に悩んだ際に参照される。

| 規約ファイル | 内容 | 適用モード |
|---|---|---|
| [architecture.md](architecture.md) | アーキテクチャ方針 | 設計・実装 |
| [naming.md](naming.md) | 命名規則 | 実装 |
| [type-hint.md](type-hint.md) | 型ヒント・データクラス・Literal 型分岐・バリデーション境界 | 実装 |
| [comments.md](comments.md) | docstring・コードコメントの記載方針 | 実装 |
| [unit-testing.md](unit-testing.md) | 単体テストケース作成方針 | 実装 |

## yamlフロントマター

```yaml
document_type: coding-standard
created_at: yyyy-MM-dd
updated_at: yyyy-MM-dd
```

- 規約ファイルを追加した際は、索引に「適用モード」とあわせて追記する

## コード規約レビューについて

本ディレクトリの規約は、読み取り専用サブエージェント `.claude/agents/coding-standards-validator.md` が検証する。エージェントは呼び出し元に応じて次のモードで動作し、索引の「適用モード」にそのモードを含む規約ファイルのみを検証対象とする。

| モード | 呼び出し元 | 検証対象 |
|---|---|---|
| 設計 | 設計レビュータスク (`design-review`) | 設計メモ |
| 実装 | 実装レビュータスク (`implementation-review`) | main ブランチとの差分 |

エージェントは実行のたびに本READMEの索引を起点に各規約ファイルを動的に読み込み、本文の規範記述と `## レビュー観点` 節の両方を検証根拠とする。チェック観点は規約ファイル側に一元化されているため、規約の追加・変更・削除時にエージェント定義側を個別に更新する必要はない。指摘の重大度は [workflow/README.md](../workflow/README.md) の定義に従う。
