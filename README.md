# Co4 Starter Kit

Welcome to the starter kit for the Co4 competition. 
It will guide you from the moment of downloading data to running a baseline solution and making your first submission. 

## Getting Started

### Data Preparation

The kit expects that the data files are stored in the `data` folder. 
`stage` is the competition stage, for the files already available in the starter kit `stage = "start"`

The structure for data is as follows:
```bash
data
├── completion_points_{stage}.jsonl
└── repositories_{stage}
    └── {owner}__{repository}-{revision}
        └── repository contents
```

To prepare data for the starter kit:
1. Download the data for the respective stage from the competition website.
2. Put the `completion_points_{stage}.jsonl` file and the `repo_archives_{stage}.zip` archive to the `data` folder.
3. Run `./prepare_data.sh start`, possibly replacing `start` with the stage, e.g., `practice`).


### Running baselines

The starter kit contains two baselines in [baselines.py](baselines.py) 
1. Selecting a random Python file from the repository.
2. Selecting a single Python file according to [BM-25](https://en.wikipedia.org/wiki/Okapi_BM25) metric. 

To run the baselines:
1. `poetry install` &ndash; install dependencies via poetry
2. `poetry run python baselines.py --stage start --strategy random` &ndash; run the baselines
   - You can replace `start` with the stage, e.g., `practice`
   - You can replace `random` with other strategy, e.g., `bm25`
3. The prediction file will be saved in the `predictions` folder.

### Submitting your solution

Go to the [submission page](https://eval.ai/web/challenges/challenge-page/2497/submission) and upload the generated prediction file to the respective stage.

