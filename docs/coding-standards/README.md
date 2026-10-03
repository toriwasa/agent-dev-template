# コード規約

## 索引
本ディレクトリでは実装時に維持すべきコード規約を集約する。
実装レビュー時やコーディング時の方針に悩んだ際に参照される。

- [architecture.md](architecture.md) — アーキテクチャ方針
- [naming.md](naming.md) — 命名規則
- [type-hint.md](type-hint.md) — 型ヒント・データクラス・Literal 型分岐・バリデーション境界
- [comments.md](comments.md) — docstring・コードコメントの記載方針
- [testing.md](unit-testing.md) — 単体テストケース作成方針

## コード規約レビューについて

本ディレクトリの規約は、読み取り専用サブエージェント `.claude/agents/coding-standards-validator.md` が設計レビュー・コードレビュー双方から呼び出されて検証する。

エージェントは実行のたびに本READMEの索引を起点に各規約ファイルを動的に読み込み、本文の規範記述と `## レビュー観点` 節の両方を検証根拠とする。チェック観点は規約ファイル側に一元化されているため、規約の追加・変更・削除時にエージェント定義側を個別に更新する必要はない。
