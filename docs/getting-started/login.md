# Login
In practice, working in AI Lab primarily takes place via a [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface). You can access the platform using Secure Shell ([SSH](https://wiki.archlinux.org/index.php/OpenSSH#Client_usage)).

AI Lab is only directly accessible when being on the AAU network (including [VPN](https://www.en.its.aau.dk/instructions/vpn) or AAU's [SSH gateway](https://www.en.its.aau.dk/instructions/ssh)). You can connect to AI Lab [front-end node](/glossery/#front-end-node) by running the following command on the command line of your local Windows (*Windows PowerShell*), MacOS or Linux computer:

!!! example

    ```console
    ssh -l xxxxxx@student.aau.dk ai-fe02.srv.aau.dk
    ```

    Replace `xxxxxx@student.aau.dk` with your AAU email address.
    
    ==CHANGE ai-fe02.srv.aau.dk ADDRESS==

You are now ready to proceed to learn about <span style="color: var(--md-primary-fg-color); font-weight: 700;"><a href="/getting-started/file-transfer">file transfer :octicons-arrow-right-24:</a></span>
