You can access the platform using
[SSH](https://wiki.archlinux.org/index.php/OpenSSH#Client_usage). How
to use SSH depends on which operating system you use on your local
computer:

=== "Linux"
    If you use a modern Linux distribution such as Ubuntu on your computer, the necessary tools to connect to AI Cloud are usually already installed by default.

=== "MacOS"
    MacOS has SSH built into the command line terminal. This means you
    can invoke SSH commands as shown in the following examples directly
    from your command line.  
    MacOS does, however, not have a built-in [X
    server](https://en.wikipedia.org/wiki/X.Org_Server) so it is
    necessary to install additional software if you wish to be able to
    show the graphical user interface (GUI) of applications (using X
    forwarding).  
    Installing [XQuartz](https://www.xquartz.org/) should enable MacOS to
    use X forwarding.

=== "Windows"

    Newer versions of Windows have SSH built into the command line
    terminal. This means you can invoke SSH commands as shown in the
    following examples directly from your command line.  
    Windows does, however, not have a built-in [X
    server](https://en.wikipedia.org/wiki/X.Org_Server) either so it is
    necessary to install additional software if you wish to be able to
    show the graphical user interface (GUI) of applications (using X
    forwarding).  
    If you wish to use a convenient way to connect to the AI Cloud from
    Windows with the ability to display the GUI of applications you run
    in AI Cloud, we recommend that you install and use
    [MobaXterm](https://mobaxterm.mobatek.net/) on your local computer.


The AI Cloud is only directly accessible when being on the AAU network
(including VPN). You can connect to AI Cloud front-end node by running
the following command on the command line of your local computer:

???+ example

    ```console
    ssh -l <aau email> ai-fe02.srv.aau.dk
    ```

    Replace `<aau email>` with your AAU email address, e.g.

    ```console
    ssh -l tari@its.aau.dk ai-fe02.srv.aau.dk
    ```

If you wish to access while **not** being connected to the AAU
network, you have two options: [Use
VPN](https://www.en.its.aau.dk/instructions/VPN/) or use AAU's [SSH
gateway](https://www.en.its.aau.dk/instructions/ssh).

??? info

    If you are often outside AAU, you can use the SSH gateway by default
    through your personal SSH configuration (in Linux/OS X this is often
    located in: `$HOME/.ssh/config`).

    ```console
    Host ai-fe02.srv.aau.dk
         User <aau email>
         ProxyJump %r@sshgw.aau.dk
    ```

    Add the above configuration to your personal ssh config file (often
    located in: `$HOME/.ssh/config` on Linux or OS X systems). Now you
    can easily connect to the platform regardless of network using the
    commands from preceding examples.
