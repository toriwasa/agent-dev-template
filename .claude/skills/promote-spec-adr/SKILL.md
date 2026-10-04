---
name: promote-spec-adr
description: 設計メモの変更対象 spec と Why Not から spec・ADR を作成・更新し、整合レビューの must を修正して設計メモを削除する(実装ワークフローの spec/ADR昇格タスク)
disable-model-invocation: true
argument-hint: "[slug]"
---

実装ワークフローの spec/ADR昇格タスクを実行します。タスクの定義・完了条件は `docs/workflow/implementation-workflow.md` の「spec/ADR昇格タスク」節、重大度は `docs/workflow/README.md`、spec・ADR の書式は `docs/spec/README.md` と `docs/adr/README.md` が正本です。最初にこれらを読んでください。

## 1. 対象を特定し、事前条件を確認する
- slug は引数があれば引数を使い、なければ現在のブランチ名 `feat/<slug>` から求める
- 次のどれかを満たさない場合は、作業を始めずに理由をユーザーに伝えて終了する
  - 引数がない場合、ブランチ名が `feat/<slug>` の形式である
  - `git status --porcelain` が空である(作業ツリーがクリーン)
  - 設計メモ `docs/design-notes/<slug>.md` が存在する
  - 設計メモの Plan のチェックボックスが全て完了している

完了条件: slug と設計メモのパスが決まり、事前条件を全て満たしている

## 2. spec を作成・更新する
- 設計メモの「変更対象 spec」に挙がった spec ごとに、実装後のソースコードを読み、外から見たインターフェース・振る舞いを確認する
- spec は設計メモではなくソースコードの実際の挙動に合わせて書く。設計メモと実装が食い違っている箇所は、spec を実装に合わせたうえで手順5で報告する
- spec は README のフロントマターと本文の構成に従い、作成時は `created_at`、更新時は `updated_at` を今日の日付にする。`sources` にはその spec が記述するソースファイルを全て挙げる
- 機能を廃止した spec は削除せず `status: deprecated` にする
- 設計メモの slug やパスは書かず、spec 単体で意味が通るように書く

完了条件: 変更対象 spec の全てが、実装後のソースコードの挙動に合わせて作成・更新されている

## 3. ADR を作成する
- 設計メモの「代替案と却下理由 Why Not」が「ADRなし」の場合は、ADR を作成せず次の手順に進む
- 検討に値する代替案がある場合は、決定ごとに `docs/adr/<今日の日付>-<決定内容の kebab-case>.md` を作成する。設計メモの Why と How から背景を書き切り、ADR 単体で意味が通るようにする
- 既存の ADR の決定を置き換える場合は、既存の ADR を削除せず `status: superseded` と `superseded_by` を設定する

完了条件: Why Not の検討に値する代替案が全て ADR に記録されている、または「ADRなし」を確認している

## 4. 整合レビューで must を修正する
- `spec-adr-validator` を、基準 `main` を渡して起動する
- 各 must 指摘の根拠となるソースコードを自分でも確認し、spec・ADR・docstring・コメントを修正する。根拠を確認した結果、誤検知だと判断した must は修正せず、判断した理由を記録する
- 修正した場合はバリデータを再度起動し、新しい must が出ていないことを確認する。再レビューは最大2回とし、2回目でも残った must は「未解決の must」として記録する
- should・nit は修正せず記録する。PR作成タスクで改めてレビューされ、ユーザーが判断する

完了条件: 全ての指摘が「修正済みの must」「誤検知と判断した must」「未解決の must」「should・nit」のいずれかに分類されている

## 5. 設計メモを削除してコミットする
- 設計メモ `docs/design-notes/<slug>.md` を削除する
- 作成・更新した spec・ADR、修正したソースコード、設計メモの削除をステージングしてコミットする。コミットメッセージには作成・更新した spec と ADR を要約する
- コミット後、次の内容を報告する
  - 作成・更新した spec と ADR
  - 設計メモと実装が食い違っていた箇所
  - 修正済みの must
  - 誤検知と判断した must とその理由、未解決の must
  - should・nit の一覧
  - 次の作業: `/create-pr` で実装レビューと実装PR作成を行う

完了条件: 設計メモの削除を含むコミットが作成され、結果を報告している
