# Blender Dev Environment
An easy to use Blender Development Environment to develop and test new addons in.

### Motivation
Trying new Blender addons can be annoying, when you have to either install them to your Blender setup or re-route your Blender setup to only look at that one addon's Git clone on your hard drive. If an addon requires extra python packages to be installed, we have to roll more setup, sometimes including installing those packages into your Blender installation.

Instead, having the Blender Dev Environment setup makes it as easy as adding your addon's location to a config file. If need be, you can also execute some startup logic along with it.

## Getting started

 1. Create an `addons.json` file - you can simply copy the `example_addons.json` to get started.

 2. __Start Blender by running the blender.bat__

## Configuration
### blender.bat
You can set the path to your Blender executable at the top of the blender.bat
### requirements.txt
If any of your addons has python requirements, add them to the requirements.txt, following the [pip standard](https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers).
### addons.json
You can easily create new entries and sort entries in the addons.json, to determine how and in which order addons should be loaded. All attributes of entries are optional.

| Attribute | Default | Description |
| ---------- | ---------- | ---------- |
| `repo` | "" | where is the addon's folder on disk? |
| `name` | "" | by which name can Blender find the addon |
| `enable` | true | do you want the addon to be enabled when Blender starts |
| `persistent` | true | do you want the addon to stay enabled when the user loads a scene |
| `startup` | false | this is a startup module |
| `code` | "" | what (python) code do we need to execute during startup (only executed if `startup` is `true`) |

A few words on potential use cases:
* You can simply just provide a `repo` path and leave everything else empty. In this case you will still add the repo path as a search path to Blender's addons, but not try to run any other logic on it.
* You can leave the `repo` path empty and just provide a `name` (e.g. if the addon is in Blender's default addon location).
* Most addons should use either `enable` or `startup`, not both.