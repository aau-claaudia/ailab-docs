# Login

???+ warning "Have you read our [Usage Policy](/overview/usage-policy)?"
    We kindly ask all users to read the [Usage Policy](/overview/usage-policy) for using AI Student Cloud before moving on.

In practice, working in the AI Student Cloud primarily takes place via a [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface). You can access the platform using Secure Shell ([SSH](https://wiki.archlinux.org/index.php/OpenSSH#Client_usage)).

??? info "For Windows users"
    The operating system on the servers in AI Student Cloud is Linux, which may make it beneficial for some users to run [Linux for Windows (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) to achieve the best experience. However, the documentation also provides guidance for Windows users on how to use AI Student Cloud. You will need to run [Windows PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/overview?) to be able to follow the documentation for AI Student Cloud.


The AI Student Cloud is only directly accessible when being on the AAU network
(including VPN). You can connect to AI Student Cloud front-end node by running
the following command on the command line of your local Windows (Windows PowerShell), MacOS or Linux computer:

???+ example

    ```console
    ssh -l <aau email> ai-fe02.srv.aau.dk
    ```
    
    Replace `<aau email>` with your AAU email address, e.g.

    ```console
    ssh -l tari@its.aau.dk ai-fe02.srv.aau.dk
    ```
    
    ==CHANGE ai-fe02.srv.aau.dk ADDRESS==

If you wish to access while **not** being connected to the AAU
network, you have two options: [Use
VPN](https://www.en.its.aau.dk/instructions/VPN/) or use AAU's [SSH
gateway](https://www.en.its.aau.dk/instructions/ssh).
