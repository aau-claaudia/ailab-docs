

srun --pty --gres=gpu:1 singularity shell --nv ollama.sif

Og kan så kører kommandoerne:

ollama serve & ollama run llama3
