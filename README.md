## ===============================================
## Secure Notes Web Application - README
## ===============================================

**Name:** Konstanty Litwinow  
**Student ID:** 23437073  
**Programme:** MSc Cybersecurity  
**Module:** Secure Web Development (H9SWD)  
**Assessment:** CA2 - Secure Web Application  
**Framework:** Flask (Python 3.12)  
**Repository:** [https://github.com/Kostek02/CA2](https://github.com/Kostek02/CA2)

---

## -----------------------------------------------
## 1. Overview
## ===============================================

The **Secure Notes Web Application** demonstrates the **Secure Software Development Lifecycle (SSDLC)** through a practical Flask implementation.  
It begins as an intentionally insecure note-management system and evolves into a **security-hardened**, OWASP Top 10-aligned web application.  
The project highlights best practices for authentication, authorization, data validation, and secure design.

---

## -----------------------------------------------
## 2. Project Objectives
## ===============================================

1. **Demonstrate Secure Development Principles**  
   Showcase end-to-end secure coding practices using Flask and Python 3.12.

2. **Build a Functional Web Platform**  
   Implement a note system with authentication, CRUD features, and role-based access control.

3. **Simulate & Mitigate Vulnerabilities**  
   Introduce and later remediate issues such as SQLi, XSS, CSRF, and IDOR.

4. **Validate Security Improvements**  
   Use Bandit, Semgrep, and pytest to demonstrate measurable improvements.

---

## -----------------------------------------------
## 3. Secure SDLC Structure
## ===============================================

| Phase | Description | Output |
|------|-------------|--------|
| **Phase 0 – Planning** | Define PRD, development plan, and repository setup. | `docs/prd.md`, `docs/dev_plan.md` |
| **Phase 1 – Scaffold** | Create Flask base and configuration. | Flask app factory, config setup |
| **Phase 2 – Insecure Build** | Intentionally insecure MVP. | Tags: `v1.0–v1.3` |
| **Phase 3 – Security Refactor** | Add secure coding controls (bcrypt, CSRF, RBAC). | Tags: `v2.0–v2.3` |
| **Phase 4 – Verification** | Testing and documentation. | Reports, evidence |

---

## -----------------------------------------------
## 4. Security Requirements Overview
## ===============================================

| ID | Requirement | Control |
|----|--------------|---------|
| **SR1** | Password Hashing | Flask-Bcrypt |
| **SR2** | CSRF Protection | Flask-WTF |
| **SR3** | Session Security | Flask-Login + secure cookies |
| **SR4** | Input Sanitisation | Jinja2 validation |
| **SR5** | RBAC | Flask role decorators |
| **SR6** | Secure Headers | Flask-Talisman |
| **SR7** | Rate Limiting | Flask-Limiter |
| **SR8** | Audit Logging | CRUD + auth logs |
| **SR9** | Error Management | Custom 403/404/500 templates |

---

## -----------------------------------------------
## 5. Application Setup
## ===============================================

### Requirements
- Python 3.12+
- SQLite (preinstalled on macOS/Linux)
- Dependencies from `requirements.txt`

### Environment Files
- `.env` for runtime variables  
- `.env.example` as template  

### Configuration
- `config.py` handles environment variable loading.

---

## -----------------------------------------------
## 6. Installation & Execution Guide
## ===============================================

### macOS / Linux
```bash
chmod +x run_app.sh
./run_app.sh
```

### Windows (PowerShell)
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\run_app.ps1
```

The app will run locally at:
http://127.0.0.1:5000

## -----------------------------------------------
## 7. Project Structure
## ===============================================

CA2/
├── app/
│   ├── __init__.py
│   ├── auth/
│   ├── notes/
│   ├── admin/
│   ├── templates/
│   └── static/
│
├── docs/
│   ├── prd.md
│   ├── dev_plan.md
│   └── evidence/
│
├── tests/
├── config.py
├── requirements.txt
├── run.py
├── run_app.sh
├── run_app.ps1
├── README.md
├── .env
├── .env.example
└── .gitignore

## -----------------------------------------------
## 8. Version History
## ===============================================

| Version       | Description                                 |
| ------------- | ------------------------------------------- |
| **v0.0**      | Repository initialization and internal docs |
| **v0.1**      | Flask setup and environment scripts         |
| **v0.2**      | Blueprints and route structure              |
| **v1.0–v1.3** | Insecure MVP                                |
| **v1.4–v1.5** | Static + dynamic testing                    |
| **v2.0–v2.6** | Secure and final release                    |

## -----------------------------------------------
## 9. Testing & Verification
## ===============================================

- **Bandit:** Detect Python security flaws
- **Semgrep:** OWASP rule scanning
- **pytest:** Route and functional validation
- **Manual Tests:** Confirm CSRF tokens, secure cookies, RBAC

Final verification ensures all SR1–SR9 are fully implemented.

## -----------------------------------------------
## 10. Evidence & Reporting
## ===============================================

# Evidence is stored under docs/evidence/:
- Flask run confirmation
- Bandit & Semgrep results
- Pytest logs
- Screenshots of vulnerabilities before/after fixes

# The technical report includes:
- GitHub repo link
- Video presentation link (Unlisted YouTube)
- Final documentation and appendices

## -----------------------------------------------
## 11. Notes
## ===============================================

- Application designed for **local use only** (assessment scope).
- Focus on demonstrating **secure development practices** over production deployment.
- Evidence, commits, and documentation show full **SSDLC traceability**.

## ----------------------------------------------- 
## 12. Author 
## =============================================== 
**Konstanty Litwinow** MSc Cybersecurity, National College of Ireland 
**GitHub:** https://github.com/Kostek02 
**Email:** x234073473@student.ncirl.ie