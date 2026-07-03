# **Privilege Escalation Principles**  
### *Independent Reference — Conceptual Model for Understanding Escalation Paths*

---

## **Purpose**  
This document condenses Privilege Escalation understanding into a clear, structured model that removes noise and focuses on the **core principles** behind all escalation paths.  
It is designed to be both:

- a **teaching resource** for learning PrivEsc fundamentals  
- an **analysis template** for interpreting LPA output  

By internalising the **Base Principles**, the **Extended Principles** become intuitive and predictable.

---

## **Overview**  
Privilege escalation is not a random collection of tricks — it is a small set of repeatable patterns that all derive from a handful of foundational concepts.

This document presents:

1. **Base Principles** — the conceptual foundation  
2. **Extended Principles** — reordered by danger level  
3. **A visual diagram** showing how base → extended principles relate  

Once the Base Principles are understood, the Extended Principles become easy to reason about, easy to teach, and easy to identify in real systems.

---

# **Base Principles (Foundation)**  
These are the *keystone concepts*.  
Every extended principle is just a specific manifestation of these.

### **Privilege Boundaries**  
Escalation happens when user, group, or root boundaries collapse.

### **Execution Context**  
Processes inherit privileges from owners, groups, environment, and capabilities.

### **Ownership & Group Membership**  
Privileged files or directories writable by lower‑privilege users create escalation paths.

### **Trust Relationships**  
Scripts, binaries, libraries, and services trust the resources they reference.

### **Resource Access**  
Privileged processes reading or executing attacker‑controlled content is dangerous.

### **Chaining Logic**  
Many escalations are indirect: group → writable privileged resource → root.

Internalise these, and PrivEsc becomes predictable.

---

# **Mermaid Diagram — How Base Principles Relate to Extended Principles**

This diagram shows the conceptual flow:

- Base Principles form the foundation  
- Extended Principles branch from them  
- SUID/SGID sit at the top due to direct boundary collapse  
- Everything else is a variation of the same underlying concepts  

```
flowchart TD

    subgraph BASE["Base Principles (Foundation)"]
        PB["Privilege Boundaries"]
        EC["Execution Context"]
        OG["Ownership & Group Membership"]
        TR["Trust Relationships"]
        RA["Resource Access"]
        CL["Chaining Logic"]
    end

    subgraph HIGH["High-Impact Principles"]
        SUID["SUID (Direct Root Escalation)"]
        SGID["SGID (Group Escalation → Chain → Root)"]
    end

    subgraph MEDIUM["Medium-Impact Principles"]
        SUDO["sudo Misconfigurations"]
        CAP["Linux Capabilities"]
        PATH["PATH Hijacking"]
        ENV["Environment Variable Abuse"]
        PERM["Weak File Permissions"]
        CRON["cron Hijacking"]
        SYSTEMD["systemd Service Hijacking"]
    end

    subgraph LOWER["Lower-Impact / Contextual Principles"]
        LIB["Shared Libraries / Plugins"]
        DAEMON["Local Services / Daemons"]
        NFS["NFS / Remote Mounts"]
        CONT["Container Escapes"]
        CREDS["Passwords / Keys / Tokens"]
        KERNEL["Kernel Exploits"]
    end

    PB --> SUID
    PB --> SGID
    PB --> SUDO
    PB --> CAP

    EC --> SUID
    EC --> SGID
    EC --> PATH
    EC --> ENV

    OG --> SUID
    OG --> SGID
    OG --> PERM
    OG --> NFS

    TR --> LIB
    TR --> DAEMON
    TR --> SYSTEMD

    RA --> CRON
    RA --> SYSTEMD
    RA --> CONT
    RA --> CREDS

    CL --> SGID
    CL --> CAP
    CL --> CONT
    CL --> KERNEL
```

This diagram is the **visual keystone** of the entire document.

---

# **Extended Principles (Reordered by Danger Level)**  
### *From most dangerous → least dangerous*

---

## **1. SUID Principle (Highest Impact)**  
Direct privilege boundary collapse.  
SUID binaries run with the file owner’s privileges — usually root.

Any user‑controlled input or dependency becomes a direct root escalation.

---

## **2. SGID Principle (High Impact)**  
Group boundary collapse.  
SGID escalates to the group, not root — but chaining often leads to full root.

---

## **3. sudo Principle**  
Misconfigured sudo rules allow indirect root execution.

---

## **4. Linux Capabilities Principle**  
Capabilities grant partial root privileges that can be chained.

---

## **5. PATH Manipulation Principle**  
Privileged processes must not rely on user‑controlled search paths.

---

## **6. Environment Variables Principle**  
Privileged programs must not trust user‑controlled environment variables.

---

## **7. File Permissions & Ownership Principle**  
Writable privileged resources allow content hijacking.

---

## **8. cron / at Principle**  
Root cron jobs referencing writable scripts allow direct escalation.

---

## **9. systemd Services Principle**  
Writable service resources allow hijacking of root‑run services.

---

## **10. Shared Libraries & Plugins Principle**  
Privileged binaries loading attacker‑controlled libraries = escalation.

---

## **11. Local Services & Daemons Principle**  
Root‑run services with insecure IPC or plugin loading can be exploited.

---

## **12. NFS / Remote Mounts Principle**  
Misconfigured NFS (e.g., `no_root_squash`) allows remote root impersonation.

---

## **13. Containers Principle**  
Privileged containers or exposed Docker sockets allow host‑level root.

---

## **14. Passwords, Keys & Tokens Principle**  
Readable secrets allow direct impersonation of privileged accounts.

---

## **15. Kernel / Local Exploits Principle**  
Kernel vulnerabilities bypass all user‑space controls.

---

# **Why This Document Works**  
### **It removes noise**  
No CVEs, no exploit lists — just the principles.

### **It teaches the fundamentals**  
Base Principles → Extended Principles → Real‑world understanding.

### **It mirrors how LPA works**  
Your modules map directly to these principles.

### **It becomes an analysis template**  
You can follow the ordered list top → bottom when reviewing LPA output.

---
