# Week 19 Wed: Feature brainstorming and hypothesis generation

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Agentic AI for Quant I: research automation, literature review, idea generation, and guardrails". Your objective is to understand, apply, and communicate feature brainstorming and hypothesis generation in a way a quant team would trust.

## Continuity Map
- Previous day focus: Literature summarization and idea extraction
- Today's focus: Feature brainstorming and hypothesis generation
- Next day bridge: Code review assistants and debugging workflow

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 60 min | Theory deep dive: definitions, intuition, and assumptions. |
| Session 2 | 60 min | Formula and workflow lab with topic-specific derivations. |
| Session 3 | 60 min | Worked examples with interpretation and failure-mode checks. |
| Session 4 | 60 min | Notebook implementation and output interpretation. |
| Session 5 | 60 min | Interview-style quiz and closed-book retrieval. |
| Session 6 | 60 min | Revision sprint, error-log update, and summary memo. |

## Why It Matters In Quant
Feature brainstorming and hypothesis generation is part of real quant work inside agentic ai for quant i: research automation, literature review, idea generation, and guardrails research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Signal-next-return association.
2. Technical frame: Build feature brainstorming and hypothesis generation from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Information Coefficient, Hit Rate, Label Horizon).
3. Market interpretation: Early hypothesis validation.. Run one compact, reproducible example for feature brainstorming and hypothesis generation and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Ignoring IC stability over time.

## Practice Problems
- Explain feature brainstorming and hypothesis generation in one paragraph without jargon.
- Write down one topic-specific formula or workflow for feature brainstorming and hypothesis generation from memory.
- Connect feature brainstorming and hypothesis generation to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind feature brainstorming and hypothesis generation?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Information Coefficient
$$IC=Corr(signal_t,r_{t+1})$$
Plain-English interpretation: Signal-next-return association.
Interview pitfall: Ignoring IC stability over time.

### Formula 2: Hit Rate
$$HR=\frac{\#(sign(\hat r)=sign(r))}{N}$$
Plain-English interpretation: Directional correctness ratio.
Interview pitfall: High hit-rate with poor payoff asymmetry.

### Formula 3: Label Horizon
$$y_t=sign(P_{t+h}-P_t)$$
Plain-English interpretation: Future target definition at horizon h.
Interview pitfall: Choosing h without turnover/cost implications.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Information Coefficient | Signal-next-return association. | Early hypothesis validation. | Ignoring IC stability over time. |
| Hit Rate | Directional correctness ratio. | Quick directional predictive quality check. | High hit-rate with poor payoff asymmetry. |
| Label Horizon | Future target definition at horizon h. | Align prediction objective with holding period. | Choosing h without turnover/cost implications. |

## Common Mistakes and Fixes
- Mistake: copying formulas without defining each symbol. Fix: annotate each term in plain language.
- Mistake: reporting one number without context. Fix: compare to benchmark or alternate scenario.
- Mistake: reading model output as certainty. Fix: include one failure mode and one robustness check.
- Mistake: skipping assumptions. Fix: list assumptions before interpretation.

## Revision Sprint
- Re-solve one earlier problem from memory before checking notes.
- Review yesterday's weak point and state whether it is fixed.
- Schedule the next spaced repetition date before ending the session.

## Real-World Data Lab
- Create a small citation table with source, claim, and verification status.
- Measure hallucination risk using unsupported-claim ratio on a short generated memo.
- Log at least one guardrail that prevented an incorrect conclusion.
- Tie the workflow back to feature brainstorming and hypothesis generation with one concrete business/research decision.

## Coding Task
Build a small AI-assisted workflow for feature brainstorming and hypothesis generation with explicit citation and hallucination checks.

## Interview Drill
- Q1: Explain feature brainstorming and hypothesis generation to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from feature brainstorming and hypothesis generation is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
