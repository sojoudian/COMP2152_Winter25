
# Setting Up Git for GitHub on Windows 11

## Step 1: Install Git
1. Download Git from the official website: [Git SCM](https://git-scm.com/)
2. Run the installer and choose the default options:
   - Select a text editor (e.g., VS Code).
   - Add Git to the PATH environment.
   - Use Unix-style line endings.
3. Verify installation by running:
   ```bash
   git --version
   ```

## Step 2: Configure Git
1. Set up your identity for Git commits:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your-email@example.com"
   ```
2. Verify configuration:
   ```bash
   git config --list
   ```

## Step 3: Generate GitHub Personal Access Token
1. Log in to GitHub and go to **Settings > Developer Settings > Personal Access Tokens**.
2. Generate a new token with scopes like `repo` and `workflow`.
3. Copy the token and keep it safe.

## Step 4: Set Up GitHub Repository Using HTTPS
1. Clone a repository:
   ```bash
   git clone https://github.com/your-username/repo-name.git
   ```
2. Authenticate using:
   - **Username**: Your GitHub username.
   - **Password**: Your Personal Access Token.

## Step 5: Push Changes to GitHub
1. Add files to the repository:
   ```bash
   git add .
   ```
2. Commit changes:
   ```bash
   git commit -m "Initial commit"
   ```
3. Push changes to GitHub:
   ```bash
   git push -u origin main
   ```

## Step 6: Verify Setup
1. Ensure the repository is updated on GitHub.
2. Your Git is now ready for GitHub using HTTPS and Personal Access Token!
