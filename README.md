# Parallel Computing Project Guide

This repository provides a guide for connecting to the ARCC (Advanced Research Computing Center) servers, managing files between your local machine and the remote server, and setting up the necessary modules and environments for our parallel computing class.

```
/Parallel-Computing
    ├── alex-testing
    ├── code.md
    ├── id_rsa
    ├── id_rsa.pub
    ├── README.md
    ├── test.py
    └── username.md
```

## Prerequisites

- Ensure you have VS Code installed with the Remote - SSH extension.
- Have your `id_rsa` private key in the directory. This key should be securely stored and not shared with anyone.

## How to Login

1. Open the VS Code integrated terminal and navigate to the project directory.
2. Set the correct permissions for the SSH key:

```bash

   chmod 600 id_rsa
   
```

## Connect to the remote server using SSH:

```bash

# replace XX with your assigned student code
ssh -Y -i id_rsa cop6526.studentXX@stokes.ist.ucf.edu

```

Once connected, type the following command to access the Newton server:

```bash

# type your assigned password
n*****n 000

```

Loading Modules

```bash

module load mvapich2/mvapich2-2.3.7-1-oneapi-2023.1.0
module load anaconda/anaconda-2023.09

```

Check available conda environments:

```bash

conda info --envs

```

Activate the environment for MPI with Python:

```bash

conda activate mpi4Python

```

Viewing the Directory

To view your current directory on the remote server, use:

```bash

pwd

```

Expected Output:

```bash

/home/cop6526.studentXX

```

## Uploading Files to the Remote Server

To upload files from your local machine to the remote server, use the following command:

```bash

rsync -avz -e "ssh -i '/Users/alexsciuto/Library/Mobile Documents/com~apple~CloudDocs/DataWithAlex/MSDA Classes/Parallel-Computing/id_rsa'" "/Users/alexsciuto/Library/Mobile Documents/com~apple~CloudDocs/DataWithAlex/MSDA Classes/Parallel-Computing/alex-testing/" cop6526.student29@stokes.ist.ucf.edu:/home/cop6526.student29/alex-testing/

```

## Downloading Files from the Remote Server to Local Directory

To download files from the remote server to your local machine, use the following command:

```bash

rsync -avz -e "ssh -i '/Users/alexsciuto/Library/Mobile Documents/com~apple~CloudDocs/DataWithAlex/MSDA Classes/Parallel-Computing/id_rsa'" "cop6526.student29@stokes.ist.ucf.edu:/home/cop6526.student29/alex-testing/test.txt" "/Users/alexsciuto/Library/Mobile Documents/com~apple~CloudDocs/DataWithAlex/MSDA Classes/Parallel-Computing/alex-testing/"

```

Troubleshooting Tips

- Permission Denied Errors: Make sure the id_rsa file has the correct permissions (chmod 600 id_rsa).
- File/Directory Not Found: Double-check the file paths in the commands, ensuring they match your local and remote directory structure.
- SSH Connection Issues: Verify that your SSH key is properly configured and that you can connect to the server without issues using the ssh command.