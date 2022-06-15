# Azure Sentiment Analysis

This project is use to test deployment of a Python API exposing a machine learning pipeline provided by HuggingFace's transformers library.

[![build status](https://github.com/rtrompier/azure-sentiment-analysis/workflows/CI%20tests/badge.svg)][ci-tests]
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)][pullrequest]

## Requirements

* Python 3.9
* Azure Account


## Development

To start locally the projet, execute the folowing command : 

To install dependencies : `pip install -r requirements.txt`
To start the function : `func start`

## Deployment

The deployment is managed by Github Action pipeline.
It use the Azure CLI.


## TODO

- Add unit & integrations tests
- Add API Security