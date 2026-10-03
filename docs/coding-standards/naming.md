# 命名規則

## 関数名

- 関数名は処理内容を直感的に理解できるように動詞から始める。I/O 処理とビジネスロジックの区別が付きやすい命名にする
  - 例: `validate_input_data`, `calculate_score`, `save_result`
- コントローラー層から呼ばれる関数はI/O処理とビジネスロジックが混在した処理を持つ。処理全体で実現したい処理内容が直感的に把握できる命名にする
  - 例: `prepare_prompt_meta`, `load_experiment_definitions`, `load_domain_knowledge`

## 定数名

- 定数名は値の内容ではなく、その定数を利用するコードにおける定数値の目的が分かる名前にする
  - 例: `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT_SECONDS`

## クラス名

- I/O処理が読み書き先パスや接続先情報などの情報を必要とする場合、クラスで管理する。外部I/Oのリソース名が分かる命名にする
  - 例: `JsonFileManager`, `S3FileManager`, `SqliteManager`

## データクラス名

- データクラス名は扱うデータの内容ではなく、そのデータクラスを引数として受け取る関数や処理から逆算して、データクラスインスタンスの目的が理解できる名前にする
  - 例: `ExperimentMeta`, `GenerationResult`, `LLMResponse`

## レビュー観点
- TODO: 記載
