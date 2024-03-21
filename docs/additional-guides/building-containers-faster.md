When building Singularity container images, you may experience very
slow performance. This is due to the fact that when writing files to
your user directory, you write to a network file system which is
known to be slow in some situations. This can cause container image
builds to take hours to complete.

In order to make this build process much faster, there is a
work-around you can use to build your containers. In order to do this,
you must use one of the compute nodes that have local storage; please
see [this overview](introduction.md#overview) - look for the "Disk"
column in the table.

Please follow these steps to use the local storage of a compute node
during build of your container:

1. Start an interactive job for building your container:  
   `srun --pty --nodelist nv-ai-01 bash -l`  
   *It is important to use the `--nodelist` parameter to request a
   compute node with local storage.*
2. Create a cache directory for yourself to use during build of
   your container image:  
   ```console
   mkdir /raid/`whoami`
   cd /raid/`whoami`
   ```  
   *Take note of the back-tick characters in the above command; this
   is just to create a directory called "/raid/username" if your
   username is "username". You can call it something else instead, but
   it is important to create it under "/raid".*
3. Run Singularity to build your container image, using your new
   directory in "/raid" for cache data storage:  
   ``SINGULARITY_CACHEDIR=/raid/`whoami` singularity pull docker://nvcr.io/nvidia/tensorflow:23.03-tf1-py3``  
   *The SINGULARITY_CACHEDIR variable should be set to whatever you
   named your cache directory in step 2.*  
4. Exit your interactive job:  
   ``exit``

You have now built your container image in the directory
"/raid/username" on a specific compute node, so you can only access it
on that compute node. You can choose to keep using it on that specific
compute node by making sure to use the `--nodelist` parameter with the
same compute node for subsequent jobs using this container image and
accessing it from your "/raid/username" directory. You can also copy
the image from there to your user directory in order to access it from
all compute nodes. Again, this copy operation may be slow due to slow
access to your user directory.  

Please remember to delete any files you have in your user directory on `/raid` on the
specific compute nodes involved when you no longer need them: 
``rm -r /raid/`whoami` ``

???+ info
      This method can be combined with [Building Memory Consuming Containers](/additional-guides/building-memory-consuming-containers) by using both the
      temporary directory in `/tmp` and the local cache directory in `/raid`
      and specifying both the `SINGULARITY_TMPDIR` and the
      `SINGULARITY_CACHEDIR` environment variables.