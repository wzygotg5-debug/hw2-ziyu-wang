# Prompt Iteration

## Initial Version
Turn the discussion notes into a summary with key points and action items.

### Why I started with this
At first, I just wanted to use a very simple prompt to see the model’s basic response.

### What happened
The result was understandable, but it felt a little too general. In some cases, the model also sounded more certain than the notes actually were.

---

## Revision 1
Turn the discussion notes into a structured summary.

Please use these sections:
- Summary
- Key Points
- Action Items
- Risks or Uncertainty

### What I changed
I added a clearer structure for the output.

### Why I changed it
I wanted the result to look more organized and easier to read. I also thought this would make it easier to compare outputs across different cases.

### What improved
After this change, the output became more consistent. It was easier to identify the main points and next steps.

---

## Revision 2
You help organize discussion notes into a clearer summary.

Please write the result in these four parts:

Summary:
Key Points:
Action Items:
Risks or Uncertainty:

Please keep these things in mind:
- Only use information that is in the notes.
- If something is not clear, do not make it sound certain.
- If an idea is only a possibility, do not write it like a final decision.
- Keep the writing clear and easy to follow.

### What I changed
In this version, I added more specific instructions about uncertainty and not making assumptions.

### Why I changed it
Some of my evaluation cases include unclear or incomplete notes, so I wanted the model to be more careful and not turn possible ideas into confirmed facts.

### What improved
This version worked better for cases with uncertainty. The output stayed closer to the original notes, and it was less likely to overstate something that was not fully confirmed.