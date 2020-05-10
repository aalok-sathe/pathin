# pathin

a convenient utility to add directories to your PATH variable
keeps track of your rc file (e.g., .bashrc, .bash_profile), 
and optionally a separate paths file (suggested: .bash_paths), 
and stores PATH variable values in pathin config (.pathin).

allows you to navigate to any directory and simply call the script to add it to PATH

## Usage

```
Usage: pathin [OPTIONS] COMMAND [ARGS]...

  pathin. conveniently add a directory to your System PATH.

  for help on commands, type "pathin <command> -h", e.g., pathin add -h

Options:
  -h, --help  Show this message and exit.

Commands:
  add        add a directory to path (default: pwd)
  configure  configure pathin's defaults
  ```
  
### Commands

**Configure** (required once). You can re-configure any time by simply running this command again.

```
Usage: pathin configure [OPTIONS]

  configure pathin's defaults

Options:
  --show                   display current config and exit
  --bash-config-file PATH  bash config file path (e.g., ~/.bashrc)
  --bash-paths-file PATH   bash paths file path (e.g., ~/.bash_paths or
                           ~/.bashrc)

  --reset                  reset configuration
  -h, --help               Show this message and exit.
```

**Add** (each new directory you want to add)
```
Usage: pathin add [OPTIONS]

  add a directory to path (default: pwd)

Options:
  --directory PATH  directory to add to path
  -h, --help        Show this message and exit.
```

## Install

  pip install pathin
