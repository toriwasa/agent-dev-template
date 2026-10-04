# ワークフロー概要
このディレクトリでは開発作業ごとの進め方ドキュメントを管理します

## 索引
- [design-workflow.md](design-workflow.md) — 調査から設計PR作成までの進め方
- [implementation-workflow.md](implementation-workflow.md) — 実装から実装PR作成までの進め方

## yamlフロントマター

```yaml
document_type: workflow
created_at: yyyy-MM-dd
updated_at: yyyy-MM-dd
```

## 全体の流れ

```txt
[design-workflow]
調査(Option) → 設計 → PR作成(設計レビュー → ★ユーザー確定 → 設計PR作成) → (マージ)

[implementation-workflow]
実装フェーズ1..N → spec/ADR昇格 → PR作成(実装レビュー → ★should以下の判断 → 実装PR作成) → (マージ)
```

- (Option) は省略可能なタスク。方針が自明な簡単な実装では省略し、設計から始めてよい。実施するかどうかはユーザーが作業開始時に判断する
- ★ はユーザーの承認ゲート。エージェントはここで作業を止めてユーザーの判断を待つ
- 各タスクは対応する SKILL として実行する

| タスク | SKILL | ワークフロー |
|---|---|---|
| 調査 | `investigate` | design |
| 設計 | `design-note` | design |
| 実装(フェーズ実行) | `implement` | implementation |
| spec/ADR昇格 | `promote-spec-adr` | implementation |
| PR作成(設計レビュー・実装レビューを含む) | `create-pr` | 両方 |

## 作業単位の識別子 (slug)
1つの作業は日付付き kebab-case の slug で識別する。日付は作業を開始した日(最初に実施した調査タスクまたは設計タスクの開始日)に固定し、以降付け直さない

- 例: `2026-10-03-add-csv-export`

| 対象 | 命名 |
|---|---|
| 調査メモ | `docs/investigation/<slug>.md` |
| 設計メモ | `docs/design-notes/<slug>.md` |
| 設計ブランチ | `design/<slug>` (設計タスク開始時に main から作成) |
| 実装ブランチ | `feat/<slug>` (設計PRマージ後に main から作成) |

## 承認ゲート
エージェントが作業を止めてユーザーの判断を待つのは次の2箇所のみ

1. 設計PRの PR作成タスクで設計レビューが完了した後: 設計メモとレビュー結果(should以下の指摘を含む)を提示し、ユーザーが設計メモを確定する
2. 実装PRの PR作成タスクで、実装レビューに should 以下の指摘が出たとき: 修正するかどうかをユーザーが判断する

- 実装タスクと spec/ADR昇格タスクのレビューでは、must だけを修正し、should 以下は報告のみとして止まらない。それらの指摘は PR作成タスクのレビューで再び検出され、ユーザーが判断する

## レビュー指摘の重大度
全てのレビュー(設計レビュー・実装レビュー・spec/ADR整合レビュー)で共通の区分を使う

| 重大度 | 定義 | 対応 |
|---|---|---|
| must | 規約違反、spec との矛盾、バグ | エージェントが修正する |
| should | 規約上の推奨事項、改善提案 | ユーザーが修正判断する |
| nit | 好みの範囲の指摘 | ユーザーが修正判断する(無視してよい) |

- must か should か判断に迷う指摘は should に倒す

## ドキュメントのライフサイクル
プロダクトに関する情報は、プロダクトコード・コードコメント・spec・ADR だけで揃う状態を保つ。調査メモと設計メモは使い捨てであり、spec・ADR・コードコメントから参照しない

| ドキュメント | 作成 | 削除 | git管理 |
|---|---|---|---|
| 調査メモ (`docs/investigation`) | 調査タスク (Option) | 不要になったら任意 | 対象外 (gitignore) |
| 設計メモ (`docs/design-notes`) | 設計タスク | spec/ADR昇格タスクの最後 | 対象 |
| spec (`docs/spec`) | spec/ADR昇格タスク | 機能廃止時も削除せず `deprecated` にする | 対象 |
| ADR (`docs/adr`) | spec/ADR昇格タスク | 削除せず `superseded` にする | 対象 |
