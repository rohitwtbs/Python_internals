#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: source $0 -u username -e email"
    echo "  -u username   Specify the Git user name"
    echo "  -e email      Specify the Git user email"
    exit 1
}

# Parse options
while getopts ":u:e:" opt; do
    case ${opt} in
        u )
            USER="$OPTARG"
            ;;
        e )
            EMAIL="$OPTARG"
            ;;
        \? )
            usage
            ;;
    esac
done
shift $((OPTIND -1))

# Check if both username and email are provided
if [ -z "$USER" ] || [ -z "$EMAIL" ]; then
    usage
fi

# Set the temporary Git environment variables
export GIT_AUTHOR_NAME="$USER"
export GIT_AUTHOR_EMAIL="$EMAIL"
export GIT_COMMITTER_NAME="$USER"
export GIT_COMMITTER_EMAIL="$EMAIL"

echo "Temporarily set Git user name to: $USER"
echo "Temporarily set Git email to: $EMAIL"
echo "These settings will only last for this terminal session."
