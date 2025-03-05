import subprocess

def set_git_config(username, email):
    try:
        # Set local username
        subprocess.run(["git", "config", "--local", "user.name", username], check=True)
        print(f"Git username set to: {username}")

        # Set locals email
        subprocess.run(["git", "config", "--local", "user.email", email], check=True)
        print(f"Git email set to: {email}")

    except subprocess.CalledProcessError as e:
        print(f"Error setting Git config: {e}")

if __name__ == "__main__":
    # Replace with your desired GitHub username and email
    github_username = "rohitwtbs"
    github_email = "12rohit4@gmail.com"

    set_git_config(github_username, github_email)
