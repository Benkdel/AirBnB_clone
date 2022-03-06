#!/bin/bash
set -e

cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/.."
{
  pycodestyle ./*.py ./models/*.py ./models/engine/*.py ./tests/*.py ./tests/test_models/*.py
}
