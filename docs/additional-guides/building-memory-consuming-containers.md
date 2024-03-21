Building some Singularity containers in AI Student Cloud may require an
unreasonably large amount of memory to succeed, such as:

???+ example
    
	**Not the right way to do it:**
	```console
	srun singularity pull docker://nvcr.io/nvidia/tensorflow:23.03-tf1-py3
	```

If you simply run this command as-is, you are likely to experience an
out-of-memory error during build of the container image. A crude
work-around for this issue is to simply allocate more memory to your
job using the `--mem` option for `srun` (it could easily require
40-50GB). This may cause your job to have to wait for a long time
before it can start. There is, however, a better way to run
Singularity to avoid the unreasonable memory requirement. Please
follow these steps to use the "/tmp" partition of a compute node
during build of your container:

1. Start an interactive job for building your container:  
   `srun --pty bash -l`  
   (You may add the `--nodelist` parameter to request a particular
   compute node as usual with `srun`.)
2. Create a temporary directory for yourself to use during build of
   your container image:  
   ``mkdir /tmp/`whoami` ``  
   *Take note of the back-tick characters in the above command; this
   is just to create a directory called "/tmp/username" if your
   username is "username". You can call it something else instead, but
   it is important to create it under "/tmp".*
3. Run Singularity to build your container image, using your new
   directory in "/tmp" for temporary data storage:  
   ``SINGULARITY_TMPDIR=/tmp/`whoami` singularity pull docker://nvcr.io/nvidia/tensorflow:23.03-tf1-py3``  
   *The SINGULARITY_TMPDIR variable should be set to whatever you
   named your temporary directory in step 2.*
4. After Singularity has finished building, delete your temporary
   directory:  
   ``rm -r /tmp/`whoami` ``
5. Exit your interactive job:  
   ``exit``

???+ info
      This method can be combined with [Building Containers Faster](/additional-guides/building-containers-faster) by using both the
      temporary directory in `/tmp` and the local cache directory in `/raid`
      and specifying both the `SINGULARITY_TMPDIR` and the
      `SINGULARITY_CACHEDIR` environment variables.