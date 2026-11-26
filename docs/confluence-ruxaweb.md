# Draft | RUXAL > RUXAWeb: Web accessibility tickets to SIP grid | Proof Of Concept

## Why

Accessibility defects were recorded twice: as Jira tickets for the team, and again in the audit grid for the SIP. The two drifted apart (duplicates, fixes not reflected, wording differences).

RUXAWeb removes the double entry. **Jira is the single source of non-conformities.** The tool reads the tickets, places them in the RAWeb 1.1 grid (simplified audit selection of the SIP), fills in the **official SIP grid** and writes two Word reports: one for the SIP (French), one for the team (English).

RUXAWeb is part of the RUXAL family, next to RUXAWeb (standalone web audit) and RUXAAM (mobile apps). It is a pre-diagnostic, not a compliance audit, and produces no accessibility statement.

## How it works

This is not a linear process. Tickets are created on the fly during the audit and the fixes, and the import can run as often as needed.

| When | What | Tool |
|---|---|---|
| Once | Create the project: name, Jira address, JQL filter; then tabs (simple audit on the 3 screens of the SIP sample, full audit, scenarios) with screens picked from the tickets | RUXAWeb |
| During the audit | Each observation becomes a Jira ticket in the team format | Copilot agent **[A11Y] Obs. -> Jira & RAWeb** |
| Any time | Export the tickets from Jira (CSV), convert them, import them | Copilot agent **[A11Y] Jira -> RUXAWeb**, then RUXAWeb |
| End of a cycle | Set C or NA on the remaining criteria; download the filled official SIP grid and the reports | RUXAWeb, tab summary |

Same interface as RUXAWeb: tabs at the top, the criteria grid with its criterion sheets, and a right panel with milestones and a "How to test" guide (dry run, standard use and responsive views, code and tools, screen reader, keyboard), to read, not to tick.

The guide, test good practices and user manual stay available at any time in the tool.

## Import from Jira

1. In RUXAWeb, Project page: **Open the filter in Jira** opens the Jira search with the project's whole JQL filter. Always export all the tickets of the filter. In Jira: Export, CSV (all fields).
2. In Copilot, open **[A11Y] Jira -> RUXAWeb** and attach the file. The agent writes one short French comment per screen for the SIP grid. Save its answer as a text file.
3. In RUXAWeb, **Import tickets** and pick the file.

The Jira key identifies each ticket, so a known ticket is updated, never duplicated. A known ticket missing from the file (deleted in Jira or out of the filter) is flagged as absent. Statuses set in the grid are never changed by an import. Editing a ticket by hand in Jira is fine: the next import takes the new version.

Without the agent, the Jira CSV can be imported directly; comments then stay in English and are flagged "to translate".

## Status rules

| Ticket or grid | Status of the screen × criterion |
|---|---|
| Open ticket on this screen (or "All") | NC |
| Fixed ticket | NT, to retest, until a status is set after the fix |
| Rejected ticket (Won't Do, Duplicate...) | Ignored |
| C or NA set in the grid | That status |
| Content absent from the screen (switch in the project) | NA |
| Nothing | NT |

A criterion's global status follows the SIP rule: the worst wins (NC, then NT).

An NC only comes from a ticket: the NC button of the grid reminds you to create the ticket in Jira, then import. To change an NC, fix or close the ticket in Jira and import again. A retest that fails means reopening the ticket in Jira.

## Rates

- **SIP selection rate**: criteria of the SIP simplified audit, comparable with a SIP simplified audit.
- **Extended rate**: adds the criteria outside the SIP selection.
- Good practices count in no rate. A rate is provisional while criteria remain untested (NT).

## Full audit

A full audit tab covers all 136 RAWeb 1.1 criteria on a representative sample (no maximum, starting from the screens named in the tickets). Each criterion sheet shows the official SIP tests. One rate, following the SIP testing methodology: criteria validated on every screen / criteria applicable on at least one screen, with the resulting compliance status (fully, partially, not compliant) and a rate per screen. Processes (a criterion is validated on a step only if it is validated on every step), exempted and derogated content, and an audit report: an HTML page to print as PDF, with the summary, sample, results per screen and per topic, exemptions, derogations, the auditor's opinion and the non-conformities with the ticket keys. The official SIP grid and SIP report stay with the simple audit.

## Good practices outside RAWeb

Three good practices complete the grid: BP1 target size, BP2 closing a modal (visible button and Escape), BP3 focus return after a modal. A ticket references one with `Good practice BP1: ...` in Reference, only when no RAWeb criterion covers the defect. They appear in the grid and the team report, never in a rate, the SIP grid or the SIP report.

## Scenarios and POUR / UX reading

A scenario follows a journey (sign up, purchase...): a tab whose screens receive the tickets that name them. Each scenario shows its SIP selection rate and a qualitative reading:

- **POUR**: tickets per principle (Perceivable, Operable, Understandable, Robust), deduced from the criterion.
- **UX**: Nielsen usability heuristics affected, suggested by the agent.

This reading never enters a rate or the SIP grid. It has its own Excel export.

## Ticket conventions (reminder)

- Title: `[A11Y] | <Application> | <Theme> | <Location>: <defect>`
- Location: `Screen[type "label"]`; a defect on every screen uses `All` (e.g. `All.footer[links]`); several screens are separated by semicolons.
- Body headings (Heading 2; older tickets in Heading 1 are still read): Flow(s) / Screen(s) / Element(s) in concern, Actual behavior / Impact, Expected behavior, Recommendations, Reference.
- Reference: `RAWeb 1.1, Criterion X.Y` with the official title, or `Good practice BP1` for a good practice. This line is what RUXAWeb reads to place the ticket in the grid.
- Screen names must match the project's screen names in RUXAWeb.

## Jira conventions

- Label **Accessibility** on every accessibility ticket, plus design and/or code.
- **Epic**: one per RUXAL theme, English name (e.g. Colors & contrast).
- **Priority**: Critical, Major, Medium, Minor.
- Screens named in tickets are added to the project automatically.

## Exports

- **Official SIP grids**: the blank SIP grid (simplified audit, 3 pages; or full RAWeb 1.1 audit, 15 pages, copies in the repository `sip/` folder) is loaded, its version checked (different version: warning, filling continues), and filled for the sample pages: status, detected problems in French with the Jira key, sample pages. SIP formulas stay intact.
- **Audit report (Word, French)**: one report for simple and full audits, following the structure of the SIP RAWeb audit report template (no branding): introduction (context, sample, rate), non-conformities by RAWeb theme with their stakes and Jira keys (no recommendations: they are in the team report and the tickets), auditor's opinion and prioritisation, results appendix. A simple audit only fills what applies to it.
- **Team report (Word, English)**: what to fix first by epic, retests, user journeys.
- **Full grid of all screens (Excel)**.
- **POUR / UX reading (Excel)**: one ticket per line.
- **Project backup (.json)**.

## Links

- Tool and documentation: https://github.com/lijko/ruxaweb
- Copilot agents: https://github.com/lijko/ruxaweb/tree/main/agents/copilot
- RAWeb 1.1: https://accessibilite.public.lu/en/raweb1.1/
