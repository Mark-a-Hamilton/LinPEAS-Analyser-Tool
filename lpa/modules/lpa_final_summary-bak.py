#!/usr/bin/env python3

"""
lpa_final_summary.py

Final summary / report orchestration.

This module aggregates all findings collected by the engine and produces
a structured final summary section.

It does NOT analyse linpeas output directly. Instead, it consumes the
engine's aggregated findings via `context["all_findings"]`.
"""

def process(section_id, subsection_id, context):
    """
    section_id: "final_summary"
    subsection_id: None
    context: {
        "pkb": dict,
        "skb": dict,
        "content": raw linpeas text,
        "section_text": unused,
        "all_findings": list of dicts from all modules
    }

    Returns: list of structured summary blocks
    """

    findings = context.get("all_findings", [])

    # ----------------------------------------------------------------------
    # 1. Severity roll-up
    # ----------------------------------------------------------------------
    severity_count = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
        "info": 0,
        "unknown": 0
    }

    for f in findings:
        sev = f.get("severity", "unknown").lower()
        severity_count[sev] = severity_count.get(sev, 0) + 1

    # ----------------------------------------------------------------------
    # 2. Top 5 risks (sorted by severity → impact length)
    # ----------------------------------------------------------------------
    severity_order = {
        "critical": 5,
        "high": 4,
        "medium": 3,
        "low": 2,
        "info": 1,
        "unknown": 0
    }

    sorted_findings = sorted(
        findings,
        key=lambda f: (
            severity_order.get(f.get("severity", "unknown").lower(), 0),
            len(f.get("impact", ""))
        ),
        reverse=True
    )

    top_5 = sorted_findings[:5]

    top_items = []
    for f in top_5:
        top_items.append({
            "severity": f.get("severity"),
            "category": f.get("category"),
            "source": f.get("source"),
            "why": f.get("why"),
            "impact": f.get("impact"),
            "recommendation": f.get("recommendation")
        })

    # ----------------------------------------------------------------------
    # 3. Recommended next steps
    # ----------------------------------------------------------------------
    next_steps = []

    if severity_count["critical"] > 0:
        next_steps.append("Address CRITICAL issues immediately — they provide direct privilege escalation paths.")

    if severity_count["high"] > 0:
        next_steps.append("Resolve HIGH severity issues next — they are reliable escalation vectors.")

    if severity_count["medium"] > 0:
        next_steps.append("Review MEDIUM issues — often chaining points for escalation.")

    if severity_count["low"] > 0:
        next_steps.append("LOW severity issues should be cleaned up to reduce attack surface.")

    if not next_steps:
        next_steps.append("No significant issues detected.")

    # ----------------------------------------------------------------------
    # 4. Build final summary block
    # ----------------------------------------------------------------------
    summary_block = {
        "section": "final_summary",
        "severity": "info",
        "category": "summary",
        "source": "lpa_final_summary",
        "why": "High-level roll-up of all findings from the LPA scan.",
        "impact": "Provides an operator-facing overview of system risk.",
        "recommendation": "Review critical and high severity issues first.",
        "items": [
            {"key": "total_findings", "value": len(findings)},
            {"key": "critical", "value": severity_count["critical"]},
            {"key": "high", "value": severity_count["high"]},
            {"key": "medium", "value": severity_count["medium"]},
            {"key": "low", "value": severity_count["low"]},
            {"key": "info", "value": severity_count["info"]},
            {"key": "unknown", "value": severity_count["unknown"]},
            {"key": "top_5_risks", "value": top_items},
            {"key": "recommended_next_steps", "value": next_steps}
        ]
    }

    return [summary_block]
