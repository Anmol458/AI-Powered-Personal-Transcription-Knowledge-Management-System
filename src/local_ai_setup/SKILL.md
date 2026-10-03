# Trigger: 
When user says "Hey organise my thoughts" or "Hey organise my transcripts" start the Extraction Process.

---

# Extraction Process

When processing a transcription, perform the following steps:

## Step 1 — Read the Entire Transcription

Start by reading the markdown file present in the RAW folder named with today's date. Read files of other dates when the user asks explicitly. Read the file completly, do not classify based only on the first few sentences. Understand the overall context before extracting information.

## Step 2 — Identify Topic Boundaries

A single transcription may contain multiple unrelated subjects.

Example:

> "I was thinking about my electronics project. Also I need to study VHDL tonight. Oh and I had this weird conversation with my friend about whether success actually matters."

Treat these as three separate knowledge units:

1. Electronics project
2. VHDL study task
3. Philosophical/conversational thought about success

Do not force them into one note. Refer to different ways of processing different topics which are discussed in this file down below.

## Step 3 — Extract Meaningful Information

Look for:
Ideas
Insights
Questions
Tasks
Projects
Goals
Plans
Decisions
Problems
Learnings
Observations
Philosophical thoughts
Personal reflections
Conversations
References
Potential YouTube ideas

## Step 4 — Determine Importance

Classify extracted information as:

high
medium
low

Use this only internally or in metadata when useful.

High importance:

- Significant project idea
- Strong recurring thought
- Important decision
- Valuable learning
- Strong YouTube idea
- Important unresolved question

Medium importance:

- Useful observation
- Interesting idea
- Minor learning
- Potential future project

Low importance:

- Passing comment
- Casual observation
- Temporary thought
- Information unlikely to be useful later

Do not create permanent notes for most low-importance information.

---

# Processing Workflow

When asked to process new transcriptions:

1. Find unprocessed transcription files.
2. Read them completely.
3. Identify topic boundaries.
4. Extract meaningful thoughts.
5. Classify each thought.
6. Search the vault for related notes.
7. Detect duplicates.
8. Update existing notes where appropriate.
9. Create new notes only when useful.
10. Add backlinks to the source transcription.
11. Update the daily summary.
12. Identify potentially important recurring themes.
13. Report what was processed.

---
# YouTube Idea Processing

YouTube ideas are especially important.

When the user expresses a potential video idea, create or update a note under Ideas/YouTube/ folder.

Use this structure:

```markdown

type: youtube_idea
created:
source:
tags:

# TITLE

## Core Idea

What is the video actually about?

## Why It Could Be Interesting

Why might someone want to watch this?

## Possible Hook

What question, surprising fact, problem, or statement could open the video?

## Possible Structure

1.
2.
3.
4.

## Things To Research

-

## Related Ideas

-

## Original Thought

> Preserve the important part of the user's original wording here.

## Source

[[Link to Original Transcription here]]

```

Do not turn every passing mention of YouTube into a full video note.

Only create a YouTube note when there is a genuine potential topic.

---

# Project Ideas Processing

When the user describes something they want to build, investigate, or accomplish, classify it as a project if it requires multiple steps.

Use:

```markdown
type: project
created:
source:
tags:

# Project Name

## Objective

What is the user trying to accomplish?

## Why

Why does the user want to do this?

## Current State

What has already been done?

## Next Actions

- [ ]

## Ideas

-

## Problems

-

## Questions

-

## Related Notes

-

## Source

[[Original Transcription]]
```
---

# Creative Ideas Processing

Any creative ideas that the user says he wants to work on or feels should be worked on needs to go here.

Statements like "an app that tracks your mental health would be cool" is an idea that should be put under creative ideas.

Use:

```markdown
type: creative idea
created:
source:

# Idea

A clear description of the idea and what triggered the idea if it is in the transcript.
```
---

# Work To Do Processing

These are tasks that represent actionable work.

Use:

```markdown
type: todo
created:
source:

# ToDo

## Action

A clear description of what needs to be done.

## Context

Why this task exists.

## Source

[[Original Transcription]]
```

"I need to study VHDL tonight" is a task.

Do not invent deadlines.

If the user says:

> "I need to finish this tomorrow"

you may record:

```yaml
due: tomorrow
```

If they don't provide a deadline, do not create one.

---

# Question Processing

Questions that the user genuinely wants answered should be captured.

Example:

> "I wonder whether an ESP32 can process audio locally."

Create:

```markdown
type: question

# Can an ESP32 Process Audio Locally?

## Question

Can an ESP32 realistically perform the required audio processing locally?

## Context

The question came up while designing the personal transcriber.

## Related Topics

- ESP32
- DSP
- Audio processing
- Embedded systems

## Source

[[Original Transcription]]
```

---

# Learning/Class Notes

When the transcription contains educational material, distinguish between:

1. Something the user learned
2. A formal class note
3. A technical concept
4. A question about something they don't understand

Do not rewrite technical material beyond what is necessary for organization.

When useful, structure technical notes as:

```markdown
type: technical_note
created:
source:
tags:

# Concept

## What It Is

Simple explanation.

## Key Points

-

## Example

-

## Questions

-

## Related Concepts

-

## Source

[[Original Transcription]]
```

---

# Learnt Something New Processing

When the user states that he learned something new from the internet or a book or anywhere else, write it here.

Use:


```markdown
type: new_fact
created:
source:
tags:

# Fact

## What It Is

Simple explanation of what the user learnt.
```

---

# Philosophical Thoughts

Philosophical thoughts should preserve uncertainty.

Use:

```markdown
type: philosophical_thought
created:
source:
tags:


# Thought / Question

## Original Thought

> Preserve the user's important wording. Write the philosphical excerpt exactly here.

## Source

[[Original Transcription]]
```

Do not present interpretations and Do not perform psychological analysis.

---

# Conversations

When the transcription contains a meaningful conversation with another person, capture the useful information without unnecessarily documenting every sentence.

Use:

```markdown
type: conversation
created:
participants:
source:
tags:

# Conversation — Topic

## Context

Briefly describe what the conversation was about.

## Important Points

-

## Ideas Raised

-

## Questions

-

## Decisions

-

## Follow-up

-

## Source

[[Original Transcription]]
```

Do not infer what another person believes unless the transcript clearly states it.

---


# Reflection of the Day

When the user talks about his day and what he did in the day and how he felt, write about it here

Use:

```markdown
type: conversation
created:
source:
tags:

## Original Thought

> Preserve important wording.

## Thoughts
What did the user feel and talk about?

## Source

[[Original Transcription]]
```

---

# Daily Notes

For each day with processed transcriptions, maintain a daily note in Daily Notes Folder.

Example:

```markdown
type: daily_summary
date: 2026-08-31

# 31 August 2026

## Main Themes

- Building personal technology
- AI
- Electronics
- Learning
- Philosophy

## Ideas

- [[Idea 1]]
- [[Idea 2]]

## YouTube Ideas

- [[YouTube Idea 1]]

## Things Learned

- [[Concept 1]]

## Questions

- [[Question 1]]

## Tasks

- [ ] Task 1
- [ ] Task 2

## Conversations

- [[Conversation — Topic]]

## Philosophical Thoughts

- [[Thought — Topic]]

## Recurring Themes

Brief description of ideas that appeared repeatedly.

## Interesting Connections

Connections between today's thoughts and older notes.
```

The daily note should summarize rather than duplicate the entire day's transcriptions.

---

# RAW
When something does not belong in a folder but is worth noting, add it in the RAW folder.

# Linking Strategy

Obsidian becomes significantly more useful when related ideas are connected.

Create `[[wikilinks]]` when there is a clear relationship.

Example:

```markdown
[[Artificial Intelligence]]
[[Human Memory]]
[[Externalized Cognition]]
```

Do not create links merely because two notes contain the same word.

A link should represent a meaningful relationship.

Useful relationship types include:

related to
caused by
example of
contradicts
extends
inspired by
depends on
part of

When appropriate, explicitly describe the relationship:

```markdown
This connects to [[Externalized Memory]] because both ideas
explore technology as an extension of human cognition.
```

---

# Duplicate Detection

Before creating a new permanent note:

1. Search for an existing note covering the same concept.
2. If one exists, update it instead of creating a duplicate.
3. If the new thought adds a substantially different perspective, add it as a new section.
4. If uncertain, place the information in RAW folder

Never create:

```text
CPU Architecture
CPU Architecture 2
CPU Architecture New
CPU Architecture Final
```

---


# Connecting Old and New Thoughts

When processing a new transcription, compare important ideas against existing notes.

Look for:

- Similar ideas
- Contradictions
- Extensions
- Earlier versions of the same idea
- Unfinished projects
- Previously unanswered questions
- Related YouTube ideas
- Knowledge that could inform a project

Example:

New thought:

> "Maybe I should make a small AI that organizes my transcriptions."

Existing note:

```text
[[Personal Knowledge Agent]]
```

Instead of creating another project, update the existing note.

---

# Contradictions

Do not automatically resolve contradictions.

If the user previously wrote:

> "I think social media is mostly harmful."

and later writes:

> "Social media has actually helped me discover a lot of useful ideas."

Do not decide which statement is correct.

Record both.

If appropriate, add:

```markdown
## Evolution / Contradiction

This thought differs from the earlier note [[...]].
```

Contradictions can be valuable because they show how thinking changes over time.

---

# What NOT To Do

Never:

- Delete raw transcriptions.
- Rewrite history.
- Invent facts.
- Invent deadlines.
- Invent beliefs.
- Invent motivations.
- Create unnecessary notes.
- Create excessive tags.
- Create duplicate notes.
- Turn every sentence into a task.
- Turn every question into a project.
- Treat speculation as fact.
- Treat casual conversation as a serious belief.
- Automatically psychoanalyze the user.
- Replace the user's voice with overly academic language.
- Automatically resolve contradictions.
- Create new top-level folders without permission.
