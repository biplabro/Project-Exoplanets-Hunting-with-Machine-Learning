# AI-ML-DS_exercises
Learn, share, collaborate & implement.
...
### Software used: 
1. [Anaconda](https://www.anaconda.com/products/distribution) 
2. [Github Desktop Client](https://github.com/shiftkey/desktop) 
3. [Remarkable Markdown Editor](https://github.com/jamiemcg/Remarkable) 
4. [Ubuntu 18.04.06 LTS x86](https://releases.ubuntu.com/18.04/) 

#### Virtual env setup in anaconda:

The codebase of this repo uses a specific version of python to avoid conflicts between libraries and dependancies. 

Creating virtual env with python 3.7.6. Using terminal, running the below command will create virtual environment. 

`conda create --name student python==3.7.6 anaconda`

Summary: <br>
`conda create` = initiate env creation <br>
`--name` = < specify name >  <br>
`python` = < specify version > <br>
`anaconda` = < specify software packages > , in this case we want to install the entire anaconda in the virtual env.

#### Installing Software packages

Install the latest package
`conda install --name student <pkg_name>`

Install a specific version of package
`conda install --name student <pkg_name>==<version_name>`

Install a package from a specific software channel
`conda install -c <channel_name> <package name>`
 <br> <br>
**Official Anaconda Documentation** <br>
[Anaconda Installation Guide](https://docs.anaconda.com/anaconda/install/linux/)<br>
[Managing Conda virtual Env](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) <br>
[Managing Packages](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html)  <br>
[Managing Software Channels](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html) 




