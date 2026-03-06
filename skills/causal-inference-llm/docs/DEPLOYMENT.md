# Deployment Guide for CausalGraph Skills

This guide explains how to share and deploy the causal-inference-llm skill for use with Claude Code.

## Package Structure

```
skills/
├── README.md                                  # Overview and quick start
├── INSTALL.md                                 # Installation instructions
├── DEPLOYMENT.md                              # This file
├── package.json                               # npm package metadata
├── causal-inference-llm.skill                 # Packaged skill (zip)
└── causal-inference-llm/                      # Source skill directory
    ├── SKILL.md                               # Core skill instructions
    ├── scripts/
    │   ├── basic_analysis.py                  # Complete analysis example
    │   └── quick_relationship_check.py        # Quick pairwise check
    └── references/
        ├── causal-theory.md                   # Theoretical background
        └── api-reference.md                   # Complete API docs
```

## Distribution Methods

### Method 1: GitHub Repository (Recommended)

Share via GitHub for version control and community contributions:

1. **Push to GitHub:**
   ```bash
   git add skills/
   git commit -m "Add causal-inference-llm skill for Claude Code"
   git push origin main
   ```

2. **Users install with:**
   ```bash
   # Clone and copy
   git clone https://github.com/yourusername/causalgraph.git
   cp -r causalgraph/skills/causal-inference-llm ~/.claude/skills/

   # Or download release
   wget https://github.com/yourusername/causalgraph/releases/download/v0.1.0/causal-inference-llm.skill
   unzip causal-inference-llm.skill -d ~/.claude/skills/
   ```

### Method 2: npm Package

Publish to npm for easy installation with npx:

1. **Prepare for npm:**
   ```bash
   cd skills
   npm login
   ```

2. **Update package.json:**
   - Set correct repository URL
   - Update author information
   - Increment version for updates

3. **Publish:**
   ```bash
   npm publish --access public
   ```

4. **Users install with:**
   ```bash
   npx @anthropic-ai/claude-code-skills add @causalgraph/causal-inference-llm
   ```

### Method 3: Direct File Sharing

Share the packaged `.skill` file directly:

1. **Upload to:**
   - GitHub Releases
   - Cloud storage (Google Drive, Dropbox)
   - Organization file server

2. **Users install with:**
   ```bash
   # Download the .skill file
   unzip causal-inference-llm.skill -d ~/.claude/skills/
   ```

## Version Management

### Semantic Versioning

Follow semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes to API or skill structure
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, documentation updates

### Creating Releases

```bash
# Update version in package.json
vim package.json

# Rebuild skill package
zip -r causal-inference-llm.skill causal-inference-llm/

# Tag release
git tag -a v0.1.0 -m "Initial release: causal inference skill"
git push origin v0.1.0

# Create GitHub release with .skill file attached
```

## Distribution Checklist

Before distributing:

- [ ] Test all example scripts work
- [ ] Verify SKILL.md triggers correctly in Claude Code
- [ ] Check all file paths in documentation are correct
- [ ] Update version numbers in package.json
- [ ] Add LICENSE file if not present
- [ ] Test installation from scratch in clean environment
- [ ] Update repository URL in package.json
- [ ] Create GitHub release with changelog
- [ ] Package skill file: `zip -r causal-inference-llm.skill causal-inference-llm/`

## Documentation Requirements

Ensure these files are included and up-to-date:

1. **SKILL.md** - Core skill instructions with frontmatter
2. **README.md** - Overview and quick start
3. **INSTALL.md** - Detailed installation instructions
4. **references/** - API docs and theoretical background
5. **scripts/** - Working example scripts
6. **package.json** - npm metadata
7. **LICENSE** - License information

## Testing Before Release

```bash
# Test skill structure
unzip -t causal-inference-llm.skill

# Test installation locally
rm -rf ~/.claude/skills/causal-inference-llm
unzip causal-inference-llm.skill -d ~/.claude/skills/

# Test scripts
cd ~/.claude/skills/causal-inference-llm/scripts
python basic_analysis.py
python quick_relationship_check.py "smoking" "lung cancer"

# Test in Claude Code
# Start Claude Code and verify skill triggers on relevant queries
```

## npm Publishing Workflow

```bash
# Initial setup (once)
npm login
npm init --scope=@causalgraph

# For each release
cd skills
npm version patch  # or minor, major
zip -r causal-inference-llm.skill causal-inference-llm/
npm publish --access public

# Verify published
npm view @causalgraph/claude-skills
```

## GitHub Release Workflow

```bash
# Create release
git tag -a v0.1.0 -m "Release v0.1.0: Causal inference skill"
git push origin v0.1.0

# On GitHub:
# 1. Go to Releases → Create new release
# 2. Select tag v0.1.0
# 3. Upload causal-inference-llm.skill as release asset
# 4. Add release notes
```

## Maintenance

### Updating Skills

When updating the skill:

1. Make changes to source files in `causal-inference-llm/`
2. Test changes thoroughly
3. Update version in package.json
4. Repackage: `zip -r causal-inference-llm.skill causal-inference-llm/`
5. Create new release

### Handling Issues

For user-reported issues:

1. Check GitHub Issues for bug reports
2. Reproduce issue in clean environment
3. Fix and update skill
4. Release patch version
5. Update INSTALL.md if needed

## Support Resources

Add these to your repository:

- **CONTRIBUTING.md** - Contribution guidelines
- **CODE_OF_CONDUCT.md** - Community standards
- **CHANGELOG.md** - Version history
- **GitHub Issues template** - Bug reports and feature requests

## Security Considerations

Before release:

- Review API key handling in examples
- Ensure no hardcoded credentials
- Validate user inputs in scripts
- Document security best practices
- Add security policy (SECURITY.md)

## Analytics (Optional)

Consider adding:

- Download tracking via GitHub Insights
- npm download stats
- User feedback mechanism
- Usage examples from community
