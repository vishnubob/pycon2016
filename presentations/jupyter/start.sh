#!/usr/bin/env bash

export JUPYTER_CONFIG_DIR=$(dirname $(realpath $0))
jupyter notebook
