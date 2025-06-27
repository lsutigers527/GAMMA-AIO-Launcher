# [1.0] GAMMA AIO Launcher

## Creator

New Iberia Haircut

## Short Description

A comprehensive launcher for GAMMA , TALKER, Voice Pet, and PySAIC. Honestly you could launch pretty much anything as long as you set the paths.

## Screenshots / Videos

(Add your screenshots or video links here)

## Long Description

GAMMA AIO Launcher streamlines the process of playing with the GAMMA modpack with mods that require additional programs to be executed. It provides an all-in-one interface for launching all these in one click.

**Features:**

- One-click game launch for
- Currently configured for:
  - TALKER
  - VoicePet
  - PySAIC

## Requirements

Python (I built on 3.13)

## Installation Guide EXE

1. Download the `GAMMA_AIO_Launcher_vX.X.zip`
2. Extract the contents to your preferred directory. You only need the .exe
3. Run `GAMMA_AIO_Launcher.exe`.
4. Follow the on-screen instructions to set up your paths. If you aren't using a mod when the file browser for it pops up, simply hit cancel.

## Installation Guide BUILD

1. Download the `GAMMA_AIO_Launcher_vX.X.zip`
2. Extract the contents to your preferred directory. All you will need is the folder named "Buildable"
3. Run the included batch file to build the exe file:

   ```Text
   build_exe.bat
   ```

   This will install PyInstaller if needed and create a standalone `.exe` from `gamma_aio_launcher.py`.
4. Run `GAMMA_AIO_Launcher.exe`.
5. Follow the on-screen instructions to set up your paths. If you aren't using a mod when the file browser for it pops up, simply hit cancel.

## Configuration

On first launch, the program will prompt you to select the paths to the required executables. These are saved in a `GAMMA_AIO.cfg` file in the same directory as the launcher. You can clear or update these paths at any time using the "Clear Config" button in the launcher.

## Troubleshooting

- If the launcher does not open, ensure you have Python installed (and in your PATH) and that your antivirus is not blocking the executable.
- If you get errors about missing DLLs or modules, try rebuilding the `.exe` or running the `.py` file directly with Python.
- If you want to reset all paths, use the "Clear Config" button in the launcher.
- The launcher uses Tkinter for its interface. If you get errors about missing `tkinter`, install it via your Python package manager.

## Download

You can find the source code and latest updates on the [GitHub repository](https://github.com/lsutigers527/GAMMA-AIO-Launcher).

## Changelog

### [1.0] - Initial Release

- First public release of GAMMA AIO Launcher
- One-click launch for GAMMA, TALKER, VoicePet, and PySAIC
- Path setup for each supported mod
- Simple, user-friendly interface
