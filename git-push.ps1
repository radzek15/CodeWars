$repository = git remote -v | ForEach-Object { $_ -split '\s+' } | Select-Object -First 1
Write-Host "Your actual repository is: $repository"

git add .

git status

# Prompt for commit message
$commit_message = Read-Host "Enter commit message"
git commit -m $commit_message

# Display the current branch
$branch = git rev-parse --abbrev-ref HEAD
Write-Host "Your actual branch is: $branch"

$branch_name = Read-Host "Enter branch name"

git push -u origin $branch_name