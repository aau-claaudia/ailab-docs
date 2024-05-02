Downloading some Singularity images to AI Lab may require a large amount of memory to succeed, such as:

```console
srun singularity pull docker://nvcr.io/nvidia/tensorflow:23.03-tf1-py3
```

If you simply run this command as-is, you are likely to experience an out-of-memory error during build of the image. A work-around for this issue is to simply allocate more memory to your job using the `--mem` option for `srun` (it could easily require 40-50GB). This may cause your job to have to wait for a long time before it can start. 

There is, however, a better way to run Singularity to avoid the unreasonable memory requirement. Please follow these steps to use the `/tmp` partition of a compute node during build of your image:

1. Start an interactive job for building your image:  
   ```console
   srun --pty bash -l
   ```
   (You may add the `--nodelist` parameter to request a particular compute node as usual with `srun`.)
   
2. Create a temporary directory for yourself to use during build of your image:  
   ```console
   mkdir /tmp/`whoami`
   ```
   *Take note of the back-tick characters in the above command; this is just to create a directory called `/tmp/username` if your username is `username`. You can call it something else instead, but it is important to create it under `/tmp`.*
   
3. Run Singularity to build your image, using your new directory in `/tmp` for temporary data storage:  
   ```console
   SINGULARITY_TMPDIR=/tmp/`whoami` singularity pull docker://nvcr.io/nvidia/tensorflow:23.03-tf1-py3
   ```
   *The `SINGULARITY_TMPDIR` variable should be set to whatever you named your temporary directory in step 2.*
   
4. After Singularity has finished building, delete your temporary directory:  
   ```console
   rm -r /tmp/`whoami`
   ```

5. Exit your interactive job:  
   ```console
   exit
   ```