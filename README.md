# Co4 Starter Kit

Welcome to the starter kit for the Co4 competition. 
It will guide you from the moment of downloading data to running a baseline solution and making your first submission. 

## Getting Started

### Data Preparation

The kit expects that the data files are stored in the `data` folder. 
`stage` is the competition stage, for the files already available in the starter kit `stage = "start"`. 
`language` is the language split, `kotlin` or `python`.

The structure for data is as follows:
```bash
data
├── {language}-{stage}.jsonl # Competition data
└── repositories-{language}-{stage} # Folder with repositories
    └── {owner}__{repository}-{revision} # Repository revision used for collecting context
        └── repository contents
```

To prepare data for the starter kit:
1. Download the data for the respective stage from [the shared folder](https://drive.google.com/drive/folders/1wcpq7ob33z5wHNFzUaiJWuHWw8sNuumC).
2. Put the `{language}-{stage}.jsonl` file (datapoints) and the `{language}-{stage}.zip` archive (repos) to the `data` folder.
3. Run `./prepare_data.sh practice python`, possibly replacing `practice` with the stage and `python` with `kotlin`.


### Running baselines

The starter kit contains two baselines in [baselines.py](baselines.py) 
1. Selecting a random Python file from the repository.
2. Selecting a single Python file according to [BM-25](https://en.wikipedia.org/wiki/Okapi_BM25) metric. 

To run the baselines:
1. `poetry install --no-root` &ndash; install dependencies via poetry
2. `poetry run python baselines.py --stage start --strategy random --lang python` &ndash; run the baselines
   - You can replace `start` with the stage, e.g., `practice`
   - You can replace `random` with another strategy, e.g., `bm25`
   - You can replace `python` with `kotlin` for another split
3. The prediction file will be saved in the `predictions` folder.

### Implementing own strategy
Please look at the implementation of the baselines in [baselines.py](baselines.py) for an example of output formatting.

If the selected context contains multiple files, their parts included in the context should be separated by `<|file_sep|>`.

### Submitting your solution

Go to the [submission page](https://eval.ai/web/challenges/challenge-page/2516/submission) and upload the generated prediction file to the respective stage.

