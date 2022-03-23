# Lab 1
## Description
<details>
  <summary>Click to expand!</summary>
  
**Lab 1:** The purpose of Lab 1 is to familiarize oneself with common terminal commands for Linux-based systems. Roughly based on the following list of commands.
![image](https://user-images.githubusercontent.com/43688127/159589275-6f8833fc-fec4-4c1e-b83e-55be10f40290.png)
</details>

## The Linux Terminal
<details>
  <summary>Click to expand!</summary>
  
The Linux terminal (or Linux command line) is a textual representation of your basic computer file system. The entire computer could be controlled using text     commands sent through the terminal. **Commands** are small phrases, words, or characters that can be entered into the terminal to perform a specific action like moving files, changing directories, or deleting folders. Anything that isn't a part of the command is called an **argument** and serves as a modifier to the original command.  <br>

There are plenty of terminal tutorials on the internet. Here are a couple:  <br>
[opensource.com](https://opensource.com/article/21/8/linux-terminal#:~:text=The%20Linux%20terminal%20is%20a,the%20most%20efficient%20method%20available.)  <br>
[ubuntu.com](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)  <br>
[Ryans Tutorials](https://ryanstutorials.net/linuxtutorial/#structure)  <br>
</details>

## Commands
### Movement & Location
<details>
  <summary>Click to expand!</summary>
  
- `$ ls`  <br>
This command lists all of the files in your current directory. It's really useful since it can give a ton of other important information like file sizes, subdirectories, and hidden files.  <br>
![image](https://user-images.githubusercontent.com/43688127/159590129-17818d4a-dbb2-4422-8c57-ec7067b22725.png)  <br>
This command can be modified with the following arguments for some cool and useful outputs:  <br>
    1. `$ ls -a` lists all files including hidden files  <br>
    2. `$ ls -F` lists files while including file types by putting different characters after the filename ('/' for directories and '\*' for executables)  <br>
    3. `$ ls -l` lists files vertically and includes important information in each column (starting from left to right)  <br>
    &nbsp;&nbsp;&nbsp;&nbsp;- **First column** gives file type and permissions  <br>
    &nbsp;&nbsp;&nbsp;&nbsp;- **Second column** gives the number of links to a file  <br>
    &nbsp;&nbsp;&nbsp;&nbsp;- **Third column** gives the name of the user who owns the file  <br>
    &nbsp;&nbsp;&nbsp;&nbsp;- **Fourth column** gives the name of the Unix group of users who own the file  <br>
    &nbsp;&nbsp;&nbsp;&nbsp;- **Fifth column** gives the size of the file in bytes  <br>
    &nbsp;&nbsp;&nbsp;&nbsp;- **Sixth column - Eigth column** give the month, day, and year or time respectively of when the file was last edited  <br>
    &nbsp;&nbsp;&nbsp;&nbsp;- **Ninth column** gives the name of the file  <br>
    4. `$ ls -R` gives a recursive listing of the directory (lists stuff in subdirectories)  <br>
    5. `$ ls -t` lists files using the time they were last edited (newest first)  <br>
    6. `$ ls -r` lists files in the reverse order that they would originally be listed in  <br>
- `& cd`  <br>
This command lets you travel into or out of directories depending on the argument that you specify. It's basically your tool to move around in the Linux terminal. Usually, you would use this after using `$ ls` to locate a specific directory. In the below example, I used `$ ls` to find the asm directory and then used the `$ cd` command to travel inside the asm directory.  <br>
![image](https://user-images.githubusercontent.com/43688127/159594750-f34f81ee-90f2-4495-bc4d-1b5f7fff227d.png)  <br>
This command can be modified with the following arguments to change where you end up:  <br>
    1. `& cd directory_name` places you inside the directory you specified in 'directory_name' (must be within the current directory).   <br>
        *Note: Linux is case-sensitive!*  <br>
    2. `& cd /new/file_path/directory` places you inside the directory you specified in the filepath '/new/file_path/directory'. This allows you to travel to a directory that isn't directly located in your current directory, and the filepath specified is known as an **absolute or full path**  <br>
    2. `& cd..` moves you one directory back  <br>
    3. `& cd` takes you straight to the home folder  <br>
    4. `& cd -` takes you to your previous directory  <br>
- `& pwd`  <br>
This command tells you where you are in the system. It outputs your current absolute path.  <br>
![image](https://user-images.githubusercontent.com/43688127/159595125-fbb9ad85-ea1b-49ba-814f-93b75f2089a3.png)  <br>
- `& locate`  <br>
- `& find`  <br>
</details>

### File Management
- `& cp`
- `& mv`
- `& rm`
- `& cat`
- `& nano`
- `$ mkdir`
- `$ rmdir`
- `$ chmod`
- `$ wget`
### System Internals
- `$ df`
- `$ hostname`
- `$ env`
- `$ ps`
- `$ uname`
### Internet and Networking
- `& ifconfig`
- `& ping`
- `& netstat`
### GitHub
- `$ git clone`
- `& git add`
- `& git commit`
- `& git push`
- `& git status`
### Help
- `$ man`
- `$ clear`
- `$ history`
- `$ kill`
