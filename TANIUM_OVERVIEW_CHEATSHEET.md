# Tanium Overview & Console Cheat Sheet

This guide distills the two supplied Tanium training transcripts: a platform overview and a console walkthrough focused on Interact, reports, and dashboards. Console labels and available data can vary by Tanium version and organization.

## Tanium at a glance

Tanium is an endpoint management and security platform for asking questions about managed devices and, through its modules, taking action on them. Its central value in the overview is getting fresh endpoint information on demand rather than relying only on inventory collected hours or days earlier.

Common uses described in the overview include:

- Discovering devices, installed software, users, and other endpoint properties.
- Investigating vulnerabilities, compliance, and endpoint security.
- Supporting asset inventory and improving the freshness of CMDB data.
- Using platform modules for endpoint management and remediation.

## The basic workflow

1. **Ask a question** in Interact, using natural language or a saved question.
2. **Choose the right scope**, such as a computer group or operating-system subset.
3. **Check the response and freshness** before treating results as complete.
4. **Filter, sort, and drill down** to find the endpoints or records of interest.
5. **Export or report** the results when needed.
6. **Remediate with care** using the appropriate module and approved change process.

## Interact: questions and results

Interact is the console area used in the walkthrough to ask endpoint questions and inspect responses.

### Getting a question started

- Try a plain-language question first; the natural-language parser can suggest a formatted question.
- Use a saved question when it matches the need or when repeatable, recent results are useful.
- Narrow broad questions with operating-system or computer-group criteria.
- Use the result columns to understand what each row represents; hidden columns can sometimes distinguish otherwise similar-looking rows.

Example questions:

- “Get installed applications from our machines.”
- “Get installed applications from Windows computers.”
- “Show endpoints with a particular application or version.”
- “Show patches installed in the last 7 or 30 days.”
- “Show patch status by source.”

Question and sensor availability depends on the modules and content configured in your environment.

### High-level read-only patch queries

The following examples use the domain, hostname, sensor, and KB criteria supplied for this guide. Confirm that these sensors and filter operators are available in your Tanium environment before saving or running the questions.

**Domain-controller and domain scope**

```text
from all entities with (
  Is DC equals true
  and AD Domain matches *centene.*|*fideliscare.*|*wellcare.*|*wc.*|*wcdev.*|*caidan.*|*healthnet.*|*dmz.*|*hhs.*|*uafc.*|*care1st.*
)
```

**Optional hostname scope** for the listed servers:

```text
Computer Name matches .*dev-esbapp0001.*|.*cncpxhnww1003.*|.*cncpxhnww1002.*|.*cncpxhnws1001.*|.*dev-esbapp0002.*|.*cncpxhnww1000.*|.*cncpxhnww1005.*|.*cncpxhnww1001.*|.*cncpxhnws1002.*|.*cncuxhnww1000.*|.*cncpxhnws1000.*|.*cncpxhnww1004.*
```

**Confirm the target systems and operating systems**

```text
Get Computer Name and Operating System from all entities with (
  Is DC equals true
  and AD Domain matches *centene.*|*fideliscare.*|*wellcare.*|*wc.*|*wcdev.*|*caidan.*|*healthnet.*|*dmz.*|*hhs.*|*uafc.*|*care1st.*
)
```

**Check for a specific installed patch**

```text
Get Computer Name and Installed Patches from all machines with (
  Is DC equals true
  and Installed Patches contains "KB5126646"
)
```

To restrict this check to the named domains, add the `AD Domain matches ...` condition above. To restrict it to the listed servers as well, add the hostname condition. Confirm the resulting target list before using it for any follow-up action.

**Review patch installation history**

```text
Get Computer Name and Operating System and Patch Installation History[30,0,1,1,1,1,0] from all entities with (
  Is DC equals true
  and AD Domain matches *centene.*|*fideliscare.*|*wellcare.*|*wc.*|*wcdev.*|*caidan.*|*healthnet.*|*dmz.*|*hhs.*|*uafc.*|*care1st.*
)
```

The history sensor's bracketed parameters are environment-specific; verify their meaning and supported values in the Question Builder or sensor documentation. These are inventory and audit questions only—they do not install or remove patches.

### Result freshness and coverage

The walkthrough distinguishes these result views:

| View | What it represents |
|---|---|
| **Current** | Live responses arriving from endpoints that answer the question. |
| **Recent** | Previously collected results for offline systems; the example describes a 7-day window and availability when a saved question exists. |
| **Cached** | Tracked data that may be available for offline systems; the example describes a 30-day window. |

These windows and options are examples from the training environment, not universal guarantees. Check the console’s labels and timestamps. A partial response may mean some endpoints have not responded or are offline; do not assume that missing results mean no matching endpoints exist.

The walkthrough also demonstrates pausing and resuming the stream of live results.

### Filtering, sorting, and drilling down

- **Quick text filter:** convenient for a quick on-screen search.
- **Filter builder:** use for explicit conditions and grouped Boolean logic, especially when preparing filtered results for export.
- **Computer-group filter:** limit results to a configured group, such as a patch group.
- **Sort:** click a column header; use Shift-click to add secondary sort fields.
- **Drill down:** select a result to inspect the associated systems and ask follow-up questions.
- **Columns:** show or hide available columns to examine details or understand why records appear as separate rows.

Before applying a multi-condition filter, read its Boolean logic carefully—for example, `application contains Firefox AND (version starts with 108 OR version starts with 109)`.

## Reports and dashboards

- **Reports** present saved or prepared views of endpoint data.
- **Dashboards** bring related report panels together for a quick overview.
- In the walkthrough, selecting a dashboard panel opens its associated report for more detail.
- **Labels** can organize reports by topic and filter the report list.
- A dashboard can be selected for the home page using the dashboard-list edit control shown in the training.
- Some reports include endpoint names or health indicators to help identify the affected systems.

Treat sample dashboards and report names in the transcript as examples; your organization may have different content or naming.

## Quick interpretation checklist

Before you share or act on a result, confirm:

- **Question:** Does it ask for the property you actually need?
- **Scope:** Is the correct computer group, OS, or other target included?
- **Freshness:** Are you looking at current, recent, or cached data?
- **Coverage:** How many endpoints responded, and could offline endpoints affect the conclusion?
- **Filters:** Are the conditions and AND/OR groups correct?
- **Rows:** Could hidden columns or distinct property values explain duplicate-looking entries?
- **Action:** If remediation is needed, are the target set, change approval, and impact understood?

## Terms

| Term | Plain-language meaning |
|---|---|
| **Endpoint** | A managed device, such as a desktop, laptop, or server. |
| **Question** | A request for endpoint data in Interact. |
| **Sensor** | An endpoint data source/property used to answer a question. |
| **Computer group** | A named set of endpoints that can be used to scope questions or actions. |
| **Saved question** | A reusable question that can support repeatable queries and, in the walkthrough, recent results. |
| **Report** | A saved or prepared view of results. |
| **Dashboard** | A collection of report panels for at-a-glance monitoring. |

## Reference

The source walkthrough points users to [Tanium documentation](https://docs.tanium.com/) for current console guidance, configuration requirements, troubleshooting, and module-specific details.
