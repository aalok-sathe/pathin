# pathin (पथिन्)

a convenient utility to add arbitrary directories to your PATH variable

keeps track of your rc file(s) (e.g., `.bashrc`, `.bash_profile`), 
and optionally a separate paths file (suggested: `.bash_paths`), 
and stores PATH variable values in pathin config (`.pathin`).

allows you to navigate to any directory and simply call this utility to add it to PATH.
intended for Linux and Unix-based OSes.



## Install pathin (also quick-start example!)

```
  git clone https://github.com/aalok-sathe/pathin.git
  cd pathin
  pip install -r requirements.txt
  
  ./pathin configure
  ./pathin add
  source PATH/TO/YOUR_SHELL_CONFIG  #(e.g. source ~/.bashrc)
```


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

## Example

Here's an example added on the suggestion of @rohan999chaudhary.
![](https://i.imgur.com/qrhxpZQ.png)
