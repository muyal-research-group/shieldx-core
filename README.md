# ShieldX - Core

This repository contains all the common modules between ```shieldx-client``` and ```shieldx-backend```.

## 📦 Publishing a New Version

This repository uses **Poetry** for packaging and **GitHub Actions** to automate publishing to **TestPyPI** and **PyPI** when a **Git tag is pushed**.

---

### ✅ Steps to Publish a New Version

#### 1️⃣ **Update the Version**

Update the version in `pyproject.toml`:
```toml
[project]
name = "shieldx-core"
version = "0.0.1a1"
```

Follow **Semantic Versioning (SemVer)**:
- `MAJOR.MINOR.PATCH` → e.g. `1.2.3`

#### 2️⃣ **Commit the Change**

```bash
git add pyproject.toml
git commit -m "Bump version to 0.0.1a1"
```

#### 3️⃣ Create a Git Tag
Annotated tag (recommended):
```bash
git tag -a v0.0.1a1 -m "Release version 0.0.1a1"
```
#### 4️⃣ Push the Commit and Tag
```bash
git push origin master
git push origin v0.0.1a1
```
### ✅ What Happens Next?
When the tag is pushed:

- GitHub Actions triggers the release workflow located at: ```.github/workflows/shieldx-core.yml```

- The package is built via Poetry

- It is published to:

    - ✅ TestPyPI if configured for testing