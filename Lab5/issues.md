# Static Code Analysis – Issue Documentation

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Weak MD5 hashing | Security – High | 39 | MD5 is a weak hashing algorithm. | Replace MD5 with SHA-256. |
| Unsafe subprocess execution | Security – High | 61 | shell=True can allow command injection. | Replace subprocess with shutil.copy2. |
| Hardcoded password | Security – Low | 8 | Admin password is stored directly in source code. | Remove the unused hardcoded password. |
| Mutable default argument | Bug | 12 | history=[] is shared across function calls. | Use None and initialize a new list. |
| Broad exception handling | Code quality | 23 | except Exception catches unrelated errors. | Catch KeyError specifically. |
| Missing docstrings | Code quality | Multiple | Functions and module lack documentation. | Add descriptive docstrings. |
| Naming convention violations | Code style | Multiple | camelCase names violate PEP 8. | Rename using snake_case. |
| Whitespace and line length | Formatting | 7, 43, 49, 77 | Formatting violations reported by Flake8. | Correct spacing and split long lines. |