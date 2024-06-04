Virtual environment:

```
python3 -m venv my-virtual-env
```

```
srun --pty singularity shell tensorflow_24.03-tf2-py3.sif
```

```
source my-virtual-env/bin/activate
```

```
pip install numpy pandas matplotlib
```


Extending the container:

Bootstrap: localimage
From: tensorflow_24.03-tf2-py3.sif

%post
    # Install additional Python packages
    pip install pycountry


srun --mem 40G singularity build --fakeroot tensorflow_24.03-tf2-py3_extended.sif tensorflow_24.03-tf2-py3_extended.def
srun singularity exec tensorflow_24.03-tf2-py3_extended.sif python3 -c "import pycountry; print(pycountry)"