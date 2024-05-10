On AI-LAB, we have a ready-to-use [MATLAB](https://se.mathworks.com/products/matlab.html) container image. This means that you can quickly access MATLAB's functionality within the AI-LAB environment without needing to install or configure the software yourself. Lets try to batch process a MATLAB script:

!!! example

    First, copy the MATLAB container image from the container directory on AI-LAB to your own user directory:

    ```console
    scp /container/matlab_r2024a.sif ~
    ```

    Next, set the environment variable to specify the MATLAB license. In this case, point it to the AAU license server:

    ```console
    export MLM_LICENSE_FILE=27000@matlab.srv.aau.dk
    ```

    You can now process MATLAB scripts. To test if everything is working, copy the following script:

    ```console
    scp course/ailab-docs-files/matlab_script.m ~
    ```

    Then, batch process the script using the command:

    ```console
    srun singularity exec matlab_r2024a.sif matlab -batch "run('script.m')"
    ```

    If successful, the script should print `Hello World.`

    <br>