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

🚀 Pre-Release Versions (alpha, beta, rc)

You can mark versions as pre-releases by appending:

```sh
<MAJOR>.<MINOR>.<PATCH>-<stage>.<number>
```

✅ Common Stages:
| Stage                      | Meaning                                         | Example         |
| -------------------------- | ----------------------------------------------- | --------------- |
| **alpha**                  | Early stage, unstable, incomplete features      | `1.2.0-alpha.1` |
| **beta**                   | More stable, feature-complete but needs testing | `1.2.0-beta.1`  |
| **rc** (Release Candidate) | Final version unless critical bugs are found    | `1.2.0-rc.1`    |

✅ Poetry follows PEP 440 standards for versioning:

- ```alpha``` → ```a```

- ```beta``` → ```b```

- ```rc``` → ```rc```


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


