# Secure Notes Web Application - Product Requirements Document

**Author:** Konstanty Litwinow
**Programme:** MSc Cybersecurity (National College of Ireland)
**Module:** Secure Web Development (H9SWD)
**Assessment:** CA2 - Secure Web Application
**Framework:** Flask (Python 3.12)
**Repository:** https://github.com/Kostek02/CA2

---

## 1. Introduction

The **Secure Notes Web Application** is a Flask-based system designed to demonstrate the full **Secure Software Development Lifecycle (SSDLC)** in practice.
It serves as both a functional note-management platform and an educational model showing how common vulnerabilities appear and how they can be mitigated using *secure coding principles*.

The application allows users to create and manage personal notes through a secure interface, supported by user authentication, session management, and administrative oversight.
Its key academic objective is to illustrate the transition from **insecure implementation** to **security-hardened production design**, aligning with OWASP Top 10 guidance.

---

## 2. Project Goals and Objectives

1. **Demonstrate Secure SDLC Principles**
    Apply secure design, implementation, testing, and verification practices across development stages.

2. **Develop a Functional Web Platform**
    Build a note-taking system with authentication, CRUD operations, and admin capabilities.

3. **Apply OWASP Top 10 Mitigations**
    Show how common flaws (SQLi, XSS, CSRF, IDOR, etc.) can be identified and remediated.

4. **Integrate Security Libraries and Tools**
    Use Flask extensions (WTF, Login, Bcrypt, Limiter, Talisman) and SAST tools (Bandit, Semgrep.)

5. **Deliver a Transparent Development Process**
    Maintain clear version control and documentation showing secure evolution over time.

---

## 3. Functional Requirements

| ID | Requirement | Description |
|----|--------------|-------------|
| **FR1** | User Registration | Users can register with a username and password. |
| **FR2** | User Login | Authenticated access to personal dashboards. |
| **FR3** | Notes Management | Create, view, edit, and delete personal notes. |
| **FR4** | Admin Dashboard | Administrators can manage users and notes with elevated privileges. |
| **FR5** | Logout | Securely end user sessions and clear cookies. |
| **FR6** | Error Handling | Display user-friendly 403, 404, and 500 pages. |
| **FR7** | Role Management | Support multiple access levels: User, Moderator, and Admin. |

Each requirement will later be validated through testing and verification during the *implementation* and *security hardening* phases.

---

## 4. Security Requirements

| ID | Requirement | Category | Description |
|----|--------------|-----------|-------------|
| **SR1** | Password Hashing | Authentication | All stored passwords are securely hashed using Flask-Bcrypt. |
| **SR2** | CSRF Protection | Input Validation | Every form includes a CSRF token via Flask-WTF. |
| **SR3** | Session Security | Session Management | Implement Flask-Login with secure cookies (`HttpOnly`, `SameSite`, `Secure`). |
| **SR4** | Input Sanitisation | XSS Prevention | Validate and sanitise all user input and template rendering. |
| **SR5** | Role-Based Access Control (RBAC) | Authorisation | Define and enforce User, Moderator, and Admin roles. |
| **SR6** | Secure Headers | Configuration | Apply CSP, HSTS, and X-Frame-Options headers via Flask-Talisman. |
| **SR7** | Rate Limiting | Brute-Force Prevention | Restrict login and registration attempts using Flask-Limiter. |
| **SR8** | Audit Logging | Monitoring | Record authentication and CRUD events for accountability. |
| **SR9** | Error Management | Error Handling | Suppress detailed stack traces in production and sanitise error outputs. |

These security requirements reflect the **OWASP Top 10 (2025)** and address both prevention and detection controls essential to secure web application design.

---

### 4.1 Alignment with OWASP Top 10 (2025)

The table below maps each implemented security requirement (SR1–SR9) to the corresponding **OWASP Top 10 (2025)** category.  
This ensures that the Secure Notes Web Application directly mitigates the most prevalent and high-impact vulnerabilities identified in current industry data.

| OWASP 2025 Category | Example CWEs (Excerpt) | Related Security Requirements | Mitigation Approach in Secure Notes |
|----------------------|-------------------------|-------------------------------|------------------------------------|
| **A01 – Broken Access Control** | CWE-284 (Improper Access Control), CWE-639 (IDOR) | SR5 – RBAC   SR4 – Input Validation | Enforce per-record ownership checks and route-level RBAC decorators. |
| **A02 – Security Misconfiguration** | CWE-16 (Configuration Errors) | SR6 – Secure Headers   SR9 – Error Management | Apply Flask-Talisman, disable debug mode, and control config via `.env`. |
| **A03 – Software Supply Chain Failures** | CWE-1104 (Use of Unmaintained Packages) | SR6 – Secure Headers | Use pinned, verified dependencies in `requirements.txt` and virtual environments. |
| **A04 – Cryptographic Failures** | CWE-327 (Weak Encryption)  CWE-319 (Cleartext Transmission) | SR1 – Password Hashing  SR3 – Session Security | Use bcrypt hashing and secure cookies with transport-level encryption support. |
| **A05 – Injection** | CWE-89 (SQL Injection)  CWE-79 (XSS) | SR4 – Input Sanitisation  SR2 – CSRF Protection | Employ parameterised queries and sanitised template rendering. |
| **A06 – Insecure Design** | CWE-209 (Information Exposure Through Error Messages) | SR9 – Error Management  SR4 – Input Validation | Apply secure-by-design controls and defensive validation. |
| **A07 – Authentication Failures** | CWE-287 (Improper Authentication) | SR1 – Password Hashing  SR3 – Session Security | Strengthen login flows with Flask-Login and hashed credentials. |
| **A08 – Software or Data Integrity Failures** | CWE-494 (Download of Code Without Integrity Check) | SR8 – Audit Logging  SR6 – Secure Headers | Use audit logs and header policies to maintain trust boundaries. |
| **A09 – Logging & Alerting Failures** | CWE-778 (Insufficient Logging) | SR8 – Audit Logging | Record all auth and CRUD events for visibility and accountability. |
| **A10 – Mishandling of Exceptional Conditions** | CWE-703 (Improper Check or Handling of Exceptional Conditions) | SR9 – Error Management | Handle errors gracefully through Flask’s custom error handlers. |

---

### 4.2 OWASP Alignment Summary

By embedding controls that map directly to OWASP Top 10 (2025) categories, this project ensures that each development phase explicitly mitigates modern web-application threats such as access control misuse, injection, and misconfiguration.  
This mapping will be referenced throughout implementation, testing, and documentation to demonstrate compliance with contemporary secure-development standards.

---

## 5. Non-Functional Requirements

| Category | Requirement |
|----------|-------------|
| **Performance** | Typical request/response time below 300ms on localhost |
| **Usability** | Intuitive interface with consent navigation and form feedback |
| **Reliability** | Local SQLite database with persistent session management |
| **Maintainability** | Modular blueprint for 'auth', 'notes', and 'admin' |
| **Portability** | Compatible with macOS, Linux, and Windows (via 'run_app.sh' / 'run_app.ps1') |
| **Security** | Must satisfy all SR1-SR9 controls prior to final release. |
| **Auditability** | Development evidence stored in Git with descriptive commit history |

---

## 6. Architecture Overview

The application follows a three-tier MVC-inspired structure to separate presentation, business logic, and data layers, ensuring maintainability and secure design.

### 6.1 System Components
- **Frontend:** HTML / CSS / Jinja2 templates
- **Backend:** Flask application using Python 3.12
- **Database:** SQLite (local persistent storage)
- **Security Libraries:**
    - Flask-Login (session)
    - Flask-WTF (validation + CSRF)
    - Flask-Bcrypt (hashing)
    - Flask-Talisman (secure headers)
    - Flask-Limiter (rate limiting)

### 6.2 Data Flow Summary
1. User submits credentials → validated → session created.
2. Authenticated user performs CRUD operations on their notes.
3. Admin/moderator views aggregated user data under protected routes.
4. Input passes through validation and sanitisation before database write.
5. Audit log records key security events (auth, CRUD, access failures).

*(Formal DFD and threat model diagrams in Appendix of final report.)*

---

## 7. Scope and Constraints

- Application will operate locally (no remote deployment).
- SQLite chosen for simplicity and reproducibility. 
- Emphasis is on demonstrating **security posture evolution**, not large-scale performance.
- No third-party API integration; all logic is self-contained.
- Focus limited to core OWASP categories relevant to web applications.

---

## 8. Success Criteria

1. Application meets all functional and security requirements (FR1-FR7, SR1-SR9).
2. Vulnerabilities present in early versions are fully mitigated in the final release.
3. Static and functional testing (Bandit, Semgrep, pytest) show measurable improvements.
4. GitHub repository provides verifiable commit progression.
5. Final report and demo video clearly evidence secure development outcomes.

---

## 9. References

- OWASP Foundation (2025) *OWASP Top 10: 2025 – The Ten Most Critical Web Application Security Risks.* Available at: <https://owasp.org/Top10/> (Accessed: November 2025)  
- *Flask Documentation – Security Best Practices*  
- *Python 3.12 Official Docs*  
- NCI Secure Web Development (H9SWD) CA2 Brief  
- *Bandit* and *Semgrep* tool guides  

---

*This document defines the functional, security, and architectural baseline for the Secure Notes Web Application as part of NCI MSc Cybersecurity – H9SWD CA2.*

---

**End of Document**