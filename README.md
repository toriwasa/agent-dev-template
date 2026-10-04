# README
## AIエージェント開発テンプレート
- Claude Code や Codex で開発する際のテンプレートリポジトリ
- CLIツールやバックエンドジョブの実装プロジェクトを想定

## ディレクトリ構成
- `project-name/` — Python プロジェクト一式(uv 管理)。構成と層の役割は [docs/coding-standards/architecture.md](docs/coding-standards/architecture.md) を参照
- `docs/` — ワークフロー・コード規約・spec・ADR などのドキュメント。索引は [docs/README.md](docs/README.md) を参照
- `.claude/` — ワークフローの各タスクを実行する SKILL とレビュー用サブエージェント

## テンプレートの使い始め方
1. プロジェクト名を決め、次の3箇所を置き換える(例: `csv-exporter` / `csv_exporter`)
   - ディレクトリ `project-name/` → `csv-exporter/`
   - パッケージディレクトリ `src/project_name/` → `src/csv_exporter/`
   - `pyproject.toml` の `name`・`description`・`[project.scripts]`
2. `project-name` / `project_name` をリポジトリ全体で検索し、ドキュメント・SKILL・サブエージェント・PR テンプレート内の表記も置き換える
3. サンプルの `greet` 処理を削除する
   - `src/<パッケージ>/handler/cli.py` の中身(エントリーポイント `main` は残して書き換える)
   - `src/<パッケージ>/controller/greeting.py`・`logic/greeting.py`・`infrastructure/clock.py`
   - `tests/controller/test_greeting.py`・`tests/logic/test_greeting.py`
4. 動作確認する

```sh
uv run --directory project-name pytest
uv run --directory project-name pyright
uv run --directory project-name project-name --name 山田
```

- サンプルを削除してテストが0件になると `pytest` は失敗扱い(終了コード5)になるため、最初の実装フェーズでテストを追加する
