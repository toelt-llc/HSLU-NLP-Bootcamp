# Fixing Issues after Running `install.sh`

## Issue Description

The `install.sh` script was designed to:

- Rename existing configuration files by appending `.backup` to their name
- Create symbolic links to the configuration files located in `sw01_setup_installations/dotfiles`.

To work properly, it must be executed from within the `dotfiles` directory. However the script in the instructions:

```bash
cd sw01_setup_installations/ && zsh dotfiles/install.sh
```

was executed from the parent directory, causing the symbolic links to be created with incorrect paths. As a result, zsh is left without a valid configuration file, leading to an error.

If you encountered this issue, your may have seen the following error message (on Windows / WSL):

![ZSH error message](/images/zsh_message.png)

## Fix Implementation

To undo the changes made by `install.sh`, a new script `fix-install.sh` has been created. This script:

- Removes the broken symbolic link that point to non-existent files
- Restores the original configuration files that were renamed with `.backup`.

### Steps to Fix the Issue

1. Ensure you're in the correct repository directory

```bash
cd sw01_setup_installations
```

2. Get the changes from GitLab:

```bash
git pull
```

3. Run the fix script

```bash
zsh fix-install.sh
```

### Verification steps

After running the script:

- Your terminal should be restored, displaying a colored arrow at the start.

![ZSH terminal](/images/zsh_terminal.png)

- Your home directory should no longer contain broken symbolic links. To confirm, run:

```bash
ls -la ~ | grep sw01_setup_installations
```

If no output is shown, the issue has been resolved.

## Next Steps

If this solution resolved your issue, go back to the `Dotfiles` section of your corresponding guide and follow the updated steps.

If the issue persists or you encounter a different error, please reach out to a teaching assistant for further assistance.
