# localbuild

This is a simple tool for running various commands related to building code
locally. It really just runs shell commands. I built it because I would clone
various repositories, build the code with my preferred settings, and install
the program. Then when I would come back to update the program later on, I
would need to look up any of the various configuration options I had set.


### Installing
1. Clone this repo.
2. Run localbuild within its own repo (requires Python3):
```
./localbuild
```
This will install it into `~/.local/bin/localbuild` (make sure it is on your
path). `./.localbbuild` can be modified to change this location.


### Usage
`localbuild` just looks for a yaml file named `.localbuild` in the current
directory. That yaml file consists of action -> command mappings. The action
names currently supported are: `update`, `setup`, `build`, `install`,
`uninstall`. By default, if no actions are specified, the first four actions are run sequentially. If a given action is not defined, it is skipped. A subset of the actions can be run by passing them as arguments, for example running `localbuild update setup` will  just run those two actions.

An example `.localbuild` file can be found at the root of this repository.
