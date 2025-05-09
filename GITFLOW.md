# GitFlow Workflow Guide for NoLock Social Marketing

This repository follows the GitFlow branching model. This document provides a quick reference for common GitFlow operations.

## Branch Structure

- **main**: Production-ready code
- **develop**: Latest development changes
- **feature/xxx**: New features (branched from develop)
- **release/xxx**: Release preparation (branched from develop)
- **hotfix/xxx**: Urgent production fixes (branched from main)

## Common Operations

### Starting a New Feature

```bash
# Make sure you're on the develop branch
git checkout develop
git pull

# Create a new feature branch
git flow feature start feature-name
```

### Working on a Feature

```bash
# Make changes, commit regularly
git add .
git commit -m "Descriptive message"

# Push to remote (first time)
git push -u origin feature/feature-name

# Push subsequent changes
git push
```

### Completing a Feature

```bash
# Finish the feature
git flow feature finish feature-name

# Push changes to develop
git checkout develop
git push
```

### Creating a Release

```bash
# Create a release branch
git flow release start 1.0.0

# Push release branch to remote
git push -u origin release/1.0.0

# Make final adjustments, commit changes
git add .
git commit -m "Prepare release 1.0.0"

# Finish the release
git flow release finish 1.0.0

# Push tags and branches
git push --tags
git checkout main
git push
git checkout develop
git push
```

### Fixing Production Issues

```bash
# Create a hotfix branch
git flow hotfix start hotfix-name

# Fix the issue, commit changes
git add .
git commit -m "Fix critical issue"

# Finish the hotfix
git flow hotfix finish hotfix-name

# Push all branches and tags
git push --tags
git checkout main
git push
git checkout develop
git push
```

## Best Practices

1. **Descriptive Commit Messages**: Write clear, concise commit messages explaining what changed and why.
2. **Regular Updates**: Pull from develop regularly to stay up-to-date.
3. **Feature Scope**: Keep features focused and relatively small when possible.
4. **Code Review**: Have teammates review your code before merging features.
5. **Documentation**: Update documentation as part of feature development.

## Working with PR/MR (Pull/Merge Requests)

When working with GitHub/GitLab:

1. Push your feature branch to remote
2. Create a PR/MR to the develop branch
3. Request code review
4. Address feedback
5. Once approved, merge the PR/MR

## Getting Help

For more information on GitFlow, see:
- [GitFlow Cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)
- [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)