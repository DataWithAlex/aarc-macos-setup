# Parallel Computing Project Guide

This repository provides a guide for connecting to the ARCC (Advanced Research Computing Center) servers, managing files between your local machine and the remote server, and setting up the necessary modules and environments for our parallel computing class.

```
/Parallel-Computing
    ├── /testing
    ├── id_rsa
    ├── id_rsa.pub
    └── README.md
```

## Prerequisites & Set-Up

- Ensure you have VS Code installed
- Download this repo, open VScode, and follow these steps: `File > Open Folder > Select Cloned Folder`
- Have your `id_rsa` and `id_rsa.pub` private keys in the directory. This key should be securely stored and not shared with anyone.

## How to Login

- Right Click in the `VScode Explorer` and select `Open in Integrated Terminal`. Run the command below and make sure you have the expected output.

```bash
ls
```

```bash
# Expected Output
README.md       id_rsa          id_rsa.pub      testing
```

- Set the correct permissions for the SSH key:

```bash
chmod 600 id_rsa
```

### Connect to the remote server using SSH:

- replace `XX` with your assigned student code

```bash
ssh -Y -i id_rsa cop6526.studentXX@stokes.ist.ucf.edu
```

Once connected, type the following command to access the Newton server:

- type your assigned password

```bash
n*****n 000
```

## Viewing the Directory

To view your current directory on the remote server, use:

```bash
pwd
```

```bash
# Expected Output:
/home/cop6526.studentXX
```

If you got this output, you can move forward with the next commands. __It is important to make sure you are actually logged in__

## Loading Modules

Here are the modules that the professor loaded. __As more modules are reccommended, I will update this repo.__

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

## Uploading Files to the Remote Server (VERY IMPORTANT)

Since all interactions with the `AARC Server` is through the terminal, we want to make all of our code in our VScode directory so it is easier to code. Once you are done coding and want to test it on the `AARC Server`, follow these steps:

To upload files from your local machine to the remote server, use the following command:

- right click on the `id_rsa` file, and select `copy path`. 
- right click on the `testing` file, and select `copy path` (If you want to do another folder, you can do the same with that folder).

```bash
rsync -avz -e "ssh -i 'id_rsa path'" "testing path" cop6526.studentXX@stokes.ist.ucf.edu:/home/cop6526.studentXX/testing/
```

to test it 

## Downloading Files from the Remote Server to Local Directory

To download files from the remote server to your local machine, use the following command:

```bash
rsync -avz -e "ssh -i 'd_rsa path'" "cop6526.studentXX@stokes.ist.ucf.edu:/home/cop6526.studentXX/testing/test.txt" "/Users/alexsciuto/Library/Mobile Documents/com~apple~CloudDocs/DataWithAlex/MSDA Classes/Parallel-Computing/testing/"
```

Troubleshooting Tips

- Permission Denied Errors: Make sure the id_rsa file has the correct permissions (chmod 600 id_rsa).
- File/Directory Not Found: Double-check the file paths in the commands, ensuring they match your local and remote directory structure.
- SSH Connection Issues: Verify that your SSH key is properly configured and that you can connect to the server without issues using the ssh command.