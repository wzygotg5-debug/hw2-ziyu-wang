# Evaluation Set

For this evaluation set, I tried to include different situations instead of using only clean examples. In real business or project discussions, notes are often short, incomplete, or unclear. Because of that, I wanted to test not only whether the model can summarize, but also whether it can stay careful when information is missing or uncertain.

## Case 1: Clear project discussion
**Input**  
Project discussion notes:
- The team will submit the draft on Thursday
- The budget section needs one more revision
- The data part is already finished
- The group agreed to move the final check-in to Friday afternoon

**What a good output should do**  
The output should give a short summary, identify the decision about moving the check-in, and list the remaining tasks clearly.

---

## Case 2: Short and messy notes
**Input**  
notes:
draft thurs
budget part revise again
data done
final check fri afternoon?
client feedback maybe still waiting

**What a good output should do**  
The model should organize the notes into something readable, but it should not turn uncertain points into confirmed facts.

---

## Case 3: Missing responsibility
**Input**  
Discussion notes:
- Update the introduction part
- Prepare the comparison table by Tuesday
- Confirm the final version before submission

**What a good output should do**  
The output should list the tasks clearly, but it should not guess who will do them.

---

## Case 4: Decision is clear but details are incomplete
**Input**  
Team meeting notes:
- The group decided to shorten the final presentation
- More support is needed for the market analysis part
- The recommendation section should be rewritten

**What a good output should do**  
The model should clearly capture the decision, summarize the next steps, and avoid adding details that were not mentioned.

---

## Case 5: Client-related uncertainty
**Input**  
Client discussion notes:
- The client was not satisfied with the current timeline
- Maybe send a revised version this week
- There was also some concern about the cost
- Not sure whether the current plan can still be used

**What a good output should do**  
The output should keep the uncertainty in the notes. It should not present the revised version or the current plan as confirmed, and it should show that the situation still needs follow-up.

---

## Case 6: Risky case that may need human review
**Input**  
Call notes:
- The other side asked whether the fee can be reduced
- A change to the agreement was mentioned
- Follow-up is needed soon
- No final answer was given during the call

**What a good output should do**  
This case should be handled carefully. The model should not present any price change or agreement change as a final decision, and it should make clear that more confirmation is needed.