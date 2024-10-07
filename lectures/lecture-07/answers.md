## Quiz 01 - Forking and Enhancing an Existing GitHub Repository

### Task 1: Fork this repository to your GitHub account.

To fork the repository:

1. Go to the original repository on GitHub.
2. Click the **Fork** button in the top-right corner of the page.
3. Select your GitHub account as the destination for the fork.

### Task 2: Clone your forked repository to your local machine using the command line.

```bash
git clone https://github.com/your-username/qtm350-quiz01.git
```

### Task 3: Change directory into the cloned repository.

```bash
cd qtm350-quiz01
```

### Task 4: Create a file named `commands.txt` (or `command.ipynb`) in the root of the repository to document all commands used throughout the project.

```bash
touch commands.txt
```

### Task 5: Create and switch to a new branch named `feature-update`.

```bash
git checkout -b feature-update
```

### Task 6: Create a new directory called `reports` within the repository.

```bash
mkdir reports
```

### Task 7: Inside the `reports` directory, create an empty file named `summary.md` using the command line.

```bash
touch reports/summary.md
```

### Task 8: Use a command to add the following line to `summary.md`: `This document provides a summary of the project updates.`

```bash
echo "This document provides a summary of the project updates." > reports/summary.md
```

### Task 9: Stage the newly created `reports` directory.

```bash
git add reports
```

### Task 10: Commit the staged changes with the message "Add reports directory".

```bash
git commit -m "Add reports directory"
```

### Task 11: Open `commands.txt` and paste all the commands used up to this point.

Add the following commands to `commands.txt`:

```bash
git clone https://github.com/your-username/quiz-repo.git
cd quiz-repo
touch commands.txt
git checkout -b feature-update
mkdir reports
touch reports/summary.md
echo "This document provides a summary of the project updates." > reports/summary.md
git add reports
git commit -m "Add reports directory"
```

### Task 12: Create three empty text files named `file1.txt`, `file2.txt`, and `file3.txt` in the `reports` folder using a single command with brace expansion.

```bash
touch reports/file{1..3}.txt
```

### Task 13: Rename the file `data/raw-data.csv` to `data/input-data.csv`.

```bash
git mv data/raw-data.csv data/input-data.csv
```

### Task 14: Create a new directory named `backup` inside the `scripts` directory, then copy all `.py` files from the `scripts` directory to the newly created `backup` directory. Use wildcards to copy the files and chain both commands in a single line of code.

```bash
mkdir scripts/backup && cp scripts/*.py scripts/backup/
```

### Task 15: Delete the `docs/documentation.md` file.

```bash
git rm docs/documentation.md
```

### Task 16: Stage and commit all changes so far. Add the message "Update project files".

```bash
git add .
git commit -m "Update project files"
```

### Task 17: Create a new file named `.gitignore` in the root of the repository.

```bash
touch .gitignore
```

### Task 18: Add the specified lines to `.gitignore` using the command line.

```bash
echo -e "temp/\ndataset0?.csv" >> .gitignore
```

### Task 19: Read the contents of your `.gitignore` file using the command line.

```bash
cat .gitignore
```

### Task 20: Stage and commit the `.gitignore` file with the message "Add .gitignore file". Use only one line to do both.

```bash
git add .gitignore && git commit -m "Add .gitignore file"
```

### Task 21: Switch back to the `main` branch and merge the `feature-update` branch into `main`.

```bash
git checkout main
git merge feature-update
```

### Task 22: Update the `commands.txt` file with all commands used so far, stage the file, and commit it with a descriptive message of your choice.

1. Open `commands.txt` and append all the recent commands.
2. Stage and commit the file:

```bash
git add commands.txt
git commit -m "Document all executed commands in commands.txt"
```

### Task 23: Push the updated `main` branch to your forked repository on GitHub.

```bash
git push origin main
```

### Task 24: Delete the `feature-update` branch from your local machine.

```bash
git branch -d feature-update
```

### Task 25: Delete the `feature-update` branch from your forked repository on GitHub using the command line.

```bash
git push origin --delete feature-update
```

## Bonus Questions

### Bonus Question 1: Send a pull request with your changes to the original repository (this one). Document each step of the process.

1. Go to your forked repository on GitHub.
2. Click the **Compare & pull request** button.
3. Review the changes to ensure they are correct.
4. Add a title and comment for your pull request.
5. Click **Create pull request** to submit.

### Bonus Question 2: Perform an interactive rebase to squash the last two commits into a single commit.

```bash
git checkout main
git pull origin main
git checkout feature-update
git rebase -i HEAD~2
```

In the editor that appears:

- Change `pick` to `squash` for the second commit.
- Save and exit the editor.
- Edit the commit message.
- Save and exit to complete the rebase.

### Bonus Question 3: Implement a pre-commit hook that prevents commits if the `README.md` file is not updated. Provide the bash script for the hook and describe how to set it up.

**Bash Script for Pre-Commit Hook (`.git/hooks/pre-commit`):**

```bash
#!/bin/bash

# Check if README.md is staged
if git diff --cached --name-only | grep -q "^README\.md$"; then
    # Check if README.md has been updated
    if git diff --cached README.md | grep -q "^-"; then
        echo "Error: README.md has been removed or is not updated."
        exit 1
    fi
    echo "README.md has been updated."
else
    echo "Error: README.md must be updated before committing."
    exit 1
fi
```

**Setup Instructions:**

1. Navigate to the `.git/hooks` directory in your repository.
2. Create a file named `pre-commit`:

   ```bash
   touch pre-commit
   ```

3. Open the `pre-commit` file in a text editor and paste the bash script provided above.
4. Make the hook executable:

   ```bash
   chmod +x pre-commit
   ```

Now, the pre-commit hook will automatically check for updates to `README.md` before allowing a commit. 