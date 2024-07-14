# [Project] Exoplanets Hunting with Machine Learning


### Introduction

Welcome to the "Exoplanets Hunting with Machine Learning" project. This wiki will provide a comprehensive understanding of exoplanets, their detection history, and the role of machine learning in discovering these distant worlds.

---

### What is an Exoplanet?
![Image](https://github.com/biplabro/Project-Exoplanets-Hunting-with-Machine-Learning/blob/master/assets/exo-space.gif)

An [Exoplanet](https://www.space.com/17738-exoplanets.html) is any planet beyond our solar system. They are detected by astronomers by observing the intensity of their parent stars. These stars are the central points around which exoplanets orbit. Exoplanets are made up of elements similar to those of the planets in our solar system, but their mixes of those elements may differ. For instance, some exoplanets may be dominated by water or ice, while others by iron or carbon.

---

### Types and Sizes of Exoplanets

Exoplanets come in a wide variety of sizes, from gas giants larger than Jupiter to small rocky planets about as big as Earth or Mars. In the sixteenth century, the Italian philosopher [Giordano Bruno](https://en.wikipedia.org/wiki/Giordano_Bruno) suggested that distant stars were similar to our Sun and, therefore, may harbor planets of their own.

---

### History of Exoplanet Detection

- **19th Century**: Early claims of exoplanet detection were made by William Jacob in 1855, who observed deviations in the orbits within the nearby 70 Ophiuchi binary star system.
- **1917**: The first time we detected an exoplanet was by NASA's Jet Propulsion Laboratory, but it wasn't confirmed.
- **1995**: The first confirmed planet orbiting a star similar to our Sun was found. This planet was at least half the mass of Jupiter and no more than twice its mass.
- **Present**: We live in an era of exoplanets. The count of confirmed exoplanets is in the thousands and rising, which is just a small sampling of our galaxy. The number could rise to tens of thousands within a decade as we enhance the number and observing power of robotic telescopes launched into space.

---

### Why Hunt for Exoplanets?

Observing exoplanets allows us to determine whether we truly understand planetary processes, even in our own solar system. Most stellar systems observed so far do not resemble our solar system. Discovering exoplanets opens up a vast exploration area to search for other habitable worlds and increases the likelihood that we are not alone in the universe.

---

### Methods to Detect Exoplanets

#### Transit Method

The transit method is a photometric method that aims to indirectly detect the presence of one or more exoplanets in orbit around a star. This method involves regularly measuring the luminosity of a star to detect the periodic decrease in brightness associated with an exoplanet's transit. By examining the light dip caused by a planet, scientists can determine the planet's size and its orbital period.

![Transit Method](https://example.com/transit-method.png)

---

### Telescope Utilized

#### Kepler Telescope

The Kepler spacecraft, named after the German astronomer Johannes Kepler, was designed to look for planets with sizes ranging from one-half to twice the size of Earth in the habitable zone of their stars. The spacecraft's primary scientific goals included determining the abundance of these planets, estimating the number of planets in multiple-star systems, and determining the properties of stars with planetary systems.

Kepler detects planets by observing transits, or tiny dips in the brightness of a star, caused by a planet crossing in front of it. The spacecraft monitored approximately 100,000 main-sequence stars over three and a half years.

![Kepler Telescope](https://example.com/kepler-telescope.png)

---

### Achievements of the Kepler Mission

- **Planets Outnumber Stars**: Kepler has proven that there are more planets than stars in our galaxy, revolutionizing our understanding of our place in the cosmos.
- **Commonality of Small Planets**: Our galaxy teems with terrestrial-sized worlds. Kepler's discoveries suggest that 20 to 50 percent of stars likely have small, rocky planets in the habitable zone.
- **Diversity of Planets and Systems**: Kepler has unveiled a diversity of planet types and stellar systems, finding planets unlike any in our solar system and multi-planet systems with up to eight planets orbiting close to their parent stars.

---

### Conclusion

This project aims to harness machine learning techniques to enhance the detection and study of exoplanets. By understanding the past and leveraging advanced technology, we can explore the vast universe and potentially find habitable worlds beyond our solar system.

---

### Software used: 
1. [Anaconda](https://www.anaconda.com/products/distribution) 
2. [Github Desktop Client](https://github.com/shiftkey/desktop) 
3. [Remarkable Markdown Editor](https://github.com/jamiemcg/Remarkable)
4. [Ubuntu 18.04.06 LTS x86](https://releases.ubuntu.com/18.04/)
5. [GhostWriter Markdown Editor](https://github.com/KDE/ghostwriter)
6. [Linux Mint 21.3 x86](https://www.linuxmint.com/)
7. [vscodium](https://github.com/VSCodium/vscodium/)

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




