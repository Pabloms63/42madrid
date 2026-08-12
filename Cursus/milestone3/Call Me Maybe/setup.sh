#!/bin/bash
# Prepara el entorno tras un reinicio o cambio de puesto.

mkdir -p /goinfre/$USER/hf_cache /goinfre/$USER/uv_cache

ln -sfn /goinfre/$USER/hf_cache ~/.cache/huggingface
ln -sfn /goinfre/$USER/uv_cache ~/.cache/uv

grep -q UV_PROJECT_ENVIRONMENT ~/.zshrc || \
  echo 'export UV_PROJECT_ENVIRONMENT=/goinfre/$USER/venvs/call_me_maybe' >> ~/.zshrc

export UV_PROJECT_ENVIRONMENT=/goinfre/$USER/venvs/call_me_maybe
uv sync

echo "Listo. El modelo se descargará en la primera ejecución si hace falta."

### chmod +x setup.sh
### cd ~/Documents/Cursus/milestone3/"Call Me Maybe"
### ./setup.sh