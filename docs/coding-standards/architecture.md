---
document_type: coding-standard
created_at: 2026-10-03
updated_at: 2026-10-04
---

# アーキテクチャ

## ディレクトリ構成

```txt
project-name
├ pyproject.toml
├ src/project_name
│ ├ handler
│ ├ controller
│ ├ logic
│ └ infrastructure
└ tests
  ├ controller
  └ logic
```

- リポジトリ直下の `project-name/` にプロジェクト一式を置き、プロダクトコード `src/` とテストコード `tests/` を並べる
- `tests/` 配下はテスト対象の層と同名のディレクトリに分ける。small テストは `tests/logic`、middle テストは `tests/controller` に置く
- handler 層は単体テストを作成しないため `tests/handler` は作らない

## ディレクトリの役割
### handler
- handlerディレクトリにはアプリケーションのエントリーポイントとなる処理が定義される
- CLIやWebAPIなどのエントリーポイント処理が定義される
- 最初は cli.py のみで、GUIが必要になったらWebAPIインターフェース定義を追加してローカルWebサーバーでGUIを実装する
- CLIにおける引数バリデーションチェック、WebAPIにおけるリクエストパラメータのバリデーションチェックを担当する
- ユーザーの入力をデータクラス化してコントローラー層処理を呼び出す
- logic, infrastructure 層の関数を直接呼び出さず、必ずコントローラー層の関数を作成して経由する。
  外部入力に影響されずに一連の処理を middle 単体テストできるようにするため
- コントローラー層の処理結果をユーザーに見せるために加工する必要がある場合は cli.py 内に加工用の関数を作成する
- 単体テストではなく、実際にCLIコマンドやGUI表示内容確認などE2Eで動作確認する

### controller
- handler層から呼び出される関数が定義される
- logic, infrastructure 配下のビジネスロジックおよびI/O処理を実行する関数を呼び出して、ユーザーにとって意味のある一連の処理を実行する
- middle単体テストの対象。正常系最小ケースのみテストする
- 処理結果はデータクラスでhandler層に返却する

### logic
- logic ディレクトリ配下は I/O 処理を一切持たない純粋関数のみを定義する
- 現在時刻取得、ネットワークI/O、ディスクI/Oを利用する処理を一切持たない
- 上記I/O処理が必要な場合、infrastructure 層のI/O処理関数を呼び出してから返り値を logic 層関数に引数で渡す
- I/O処理の中でビジネスロジック処理をしたくなった場合、 "I/O処理における判断" だけを logic 層で実行し、返り値を infrastructure 層に引数で渡す
- small単体テストの対象

### infrastructure
- infrastructure ディレクトリ配下は現在時刻取得やネットワークI/OやディスクI/O、DB読み書きなどのI/O処理を担当する
- I/O処理はできる限りシンプルにして、入力データとデータクラスインスタンスの変換、データクラスをディスクやDBに書き込む、といったI/Oとデータクラスの相互変換だけを担当する
- I/O処理にロジックを含めたい場合、入力データをlogicで加工したり、logicで加工や判断を行ってからI/O出力したりすることで対応する

## レビュー観点
- [must] 新規モジュールが `project-name/src/project_name/` 配下の handler・controller・logic・infrastructure のいずれかに配置されている(→ ディレクトリ構成)
- [must][実装] テストファイルが `project-name/tests/` 配下の、テスト対象の層と同名のディレクトリに配置されている(→ ディレクトリ構成)
- [must] CLI 引数・リクエストパラメータのバリデーションが handler 層で行われている(→ handler)
- [must] handler 層がユーザー入力をデータクラスに変換してから controller 層を呼び出している(→ handler)
- [must] handler 層が logic・infrastructure 層の関数を直接呼び出さず、controller 層の関数を経由している(→ handler)
- [must][実装] handler 層の出力加工用の関数が `handler/cli.py` 内に定義されている(→ handler)
- [should][実装] handler 層に単体テストを作成していない(→ handler)
- [must] controller 層の関数が処理結果をデータクラスで handler 層に返している(→ controller)
- [should] controller 層の関数がユーザーにとって意味のある一連の処理単位になっている(→ controller)
- [must][実装] controller 層の関数に正常系最小ケースの middle 単体テストがある(→ controller)
- [must] logic 層に現在時刻取得・ネットワーク・ディスク・DB などの I/O を伴う処理が割り当てられていない(→ logic)
- [must][実装] logic 配下のモジュールが infrastructure 配下を import しておらず、`datetime.now()`・`open()`・HTTP クライアントなどの I/O API を呼んでいない(→ logic)
- [must][実装] logic 層の関数に small 単体テストがある(→ logic)
- [should] infrastructure 層の処理が I/O とデータクラスの相互変換に留まり、加工・判断のロジックが logic 層に切り出されている(→ infrastructure)
