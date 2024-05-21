# Login
You connect to AI-LAB [front-end nodes](/glossery/#front-end-node) by running the following command on the command line of your local Windows (*Windows PowerShell*), MacOS or Linux computer:

```console
ssh -l <email> ailab-fe01.srv.aau.dk
```
or
```console
ssh -l <email> ailab-fe02.srv.aau.dk
```

Replace `<email>` with your AAU email address.

!!! info
    The first time you connect, you will get a message like:

    ```console
    The authenticity of host 'ailab-fe01.srv.aau.dk (172.21.131.1300)' can't be established.
    ED25519 key fingerprint is SHA256:xosJtOSfQyyW16c6RtpN8tAi/91XHCR3GxM9/KJEogg.
    This key is not known by any other names.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    ```

    Type `yes` and press `ENTER` to continue connecting.

Enter your AAU password when prompted and press `ENTER`. When you can see `<email>@ailab-fe01:~$` you are succesfully logged in.

You are now ready to proceed to learn about <span style="color: var(--md-primary-fg-color); font-weight: 700;"><a href="/getting-started/file-management">file management :octicons-arrow-right-24:</a></span>