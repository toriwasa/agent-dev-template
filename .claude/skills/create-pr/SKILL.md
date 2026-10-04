---
name: create-pr
description: ブランチ名から設計PRか実装PRかを判定し、レビュー・承認ゲート・コミットを経て PR を作成する(設計・実装ワークフローの PR作成タスク)
disable-model-invocation: true
---

設計・実装ワークフローの PR作成タスクを実行します。PR作成タスクにはレビューと承認ゲートが含まれ、レビューを通さずに PR を作成することはありません。タスクの定義・完了条件は `docs/workflow/design-workflow.md` と `docs/workflow/implementation-workflow.md` の「PR作成タスク」節、重大度と承認ゲートは `docs/workflow/README.md` が正本です。最初に、手順1で判定した種別のワークフロー文書と README を読んでください。

## 1. 種別を判定し、事前条件を確認する
現在のブランチ名から種別と slug を求める。

| ブランチ名 | 種別 | 種別ごとの手順 |
|---|---|---|
| `design/<slug>` | 設計PR | [design.md](design.md) |
| `feat/<slug>` | 実装PR | [implementation.md](implementation.md) |

次のどれかを満たさない場合は、作業を始めずに理由をユーザーに伝えて終了する。

- ブランチ名が上の表のどちらかの形式である
- `git status --porcelain` が空である(作業ツリーがクリーン)
- `gh auth status` が成功する
- `gh pr view` で、現在のブランチの PR がまだ存在しないことを確認できる

完了条件: 種別と slug が決まり、事前条件を全て満たしている

## 2. 種別ごとの手順を実行する
種別ごとの手順ファイルを読み、その手順を全て実行する。手順ファイルにはレビュー・承認ゲート・コミットと、PR本文の材料の集め方が書かれている。

完了条件: 種別ごとの手順ファイルの全手順が完了し、PR本文の材料が揃っている

## 3. PR を作成する
- `.github/PULL_REQUEST_TEMPLATE/` 配下の種別のテンプレート(設計PRは `design.md`、実装PRは `implementation.md`)を読み、全ての節を手順2で集めた材料で埋めて PR本文を作る。テンプレートの HTML コメントは削除する
- PR タイトルは、設計PRなら `[設計] <変更内容の要約>`、実装PRなら `[実装] <変更内容の要約>` とする
- `git push -u origin <ブランチ名>` で push し、`gh pr create --base main --title <タイトル> --body-file <PR本文のファイル>` で PR を作成する。PR本文のファイルはリポジトリの外の一時ディレクトリに置く
- 作成した PR の URL を報告する

完了条件: PR が作成され、URL を報告している
