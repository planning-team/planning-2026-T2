# Planning Algorithms in AI and Robotics course T2 2026-27

The Planning Algorithms in AI and Robotics course, during T2, 2026-2027.

This repository includes all material used during the course: seminars and problem sets. Lecture notes and Unedited videos will be shared on telegram.

> * Instructor: Gonzalo Ferrer
> * Teaching Assistant: Anastasija Cvijovic
> * Teaching Assistant: Egor Krasnoschekov

## Lectures

| Date       | Lecture                                  |
| ---------- | ---------------------------------------- |
| 28-10-2026 | [L01: Introduction. What is planning?]() |
|            | [L02: Discrete Planning]()               |
| 30-10-2026 | PS1 python check                    |
| 4-11-2026  | Holiday                                  |
| 6-11-2026  | [L03: Configuration Space]()             |
| 11-11-2026 | S1: Distances                            |
| 13-11-2026 | [L04: Sampling-based Planning]()         |
| 18-11-2026 | S2: Sampling                             |
| 20-11-2026 | [L05: Discrete Optimal Planning]()       |
| 25-11-2026 | [L06: Optimal Control and Planning]()    |
| 27-11-2026 | [L07: Markov Decision Process]()         |
| 2-12-2026  | [L08: TBD]()       |
| 4-12-2026  | [L09: TBD]()                              |
| 9-12-2026  | [L10: TBD]()                              |
| 16-12-2026 | Final Project Presentation               |

## Important Deadlines


Deadline dates for submitting problem sets, in the folder `PS*`:

- PS1: Discrete planning (15-November-2026)
- PS2: Sampling-based planning (29-November-2026)
- PS3: TBD (6-December-2026)

 
## Final Course Project

The final project could be either of the following, where in each case the topic should be closely related to the course:

 * An algorithmic or theoretical contribution that extends the current state-of-the-art.
 * An implementation of a state-of-the-art algorithm. Ideally, the project covers interesting new ground and might be the basis for a future conference paper submission or product.
 
You are encouraged to come up with your own project ideas, yet make sure to pass them by Prof. Ferrer before you submit your abstract


 * Ideally 3-5 students per project (the scope of multi-body projects must be commensurate).
 * Proposal: 1 page description of project + goals for milestone. This document describes the initial proposal and viability of the project.
 * Presentations: The presentation needs to be 12 minutes long; There will be a maximum of 3 minutes for questions after the presentation.If your presentation lasts more than 12 minutes, it will be stopped. So please make sure the presentation does not go over.
 * Paper: This should be a IEEE conference style paper, i.e., focus on the problem setting, why it matters and what is interesting/novel about it, your approach, your results, analysis of results, limitations, future directions. Cite and briefly survey prior work as appropriate but do not re-write prior work when not directly relevant to understand your approach.
 * Evaluation: Each team will evaluate their colleagues’ presentations by asking questions to other teams.


 # Virtual Environment Setup

1. Make sure Python 3.8 or newer is installed (`python3 --version`).
2. From the project root, create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```
3. Activate it:
   - macOS/Linux: `source .venv/bin/activate`
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
4. Install the project in editable mode with dependencies (run this from the repository root where `pyproject.toml` lives):
   ```bash
   python -m pip install --upgrade pip
   pip install -e .
   ```
5. When finished, deactivate with `deactivate`.



