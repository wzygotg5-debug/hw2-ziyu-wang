# Report

## What I made this time
In this assignment, I built a relatively small workflow that turns raw discussion notes into a clearer summary. The notes can come from client communication, project discussions, or more general business conversations. I chose this task because I think this kind of situation is very common. In real life, people often take notes while listening, so the content can be fragmented and incomplete. Sometimes only a few key words are written down, and when people look back later, the notes are not always easy to understand. Because of that, I wanted to test whether a language model could help turn messy original notes into a clearer first draft.

## Why I chose this direction
I chose this direction mainly because it feels practical and easy to connect to real situations. Whether it is a group project or a more business-related discussion, people usually do not take perfectly complete notes. Most of the time, they just write down the main points as quickly as possible. That may be convenient in the moment, but it still takes time to organize everything later. The value of this workflow is that it can turn scattered notes into a more readable version and help users understand what was discussed and what should happen next. I also think this is a good task for testing model behavior, because the challenge is not only whether the model can summarize, but whether it can stay careful when the information is incomplete.

## The model I used and my overall approach
For this project, I used Gemini, got the API key from Google AI Studio, and built a simple prototype in Python. I chose this setup mainly because it was easy to start with and worked well for a small experiment like this assignment. My main focus was not to compare many different models, but to first build the workflow, then test it with a fixed evaluation set, and then improve the output step by step by changing the prompt. For that purpose, Gemini was enough for this task.

## How I changed my prompt step by step
At the beginning, my prompt was very simple. I only asked the model to turn the discussion notes into a summary with key points and action items. The result was generally readable, but sometimes it felt too general. In some cases, the model also sounded more certain than the original notes actually were.

The first change I made was to make the output format more structured. I divided the result into Summary, Key Points, Action Items, and Risks or Uncertainty. After doing this, the output looked clearer, and it also became easier to compare results across different cases.

In the final version, I added more direct restrictions, such as not adding information that was not in the original notes, not turning possible ideas into final decisions, and keeping uncertainty when the notes themselves were uncertain. After this change, the model handled cases with incomplete information or higher risk more carefully, and it was less likely to overstate things that were not fully confirmed.

## What I think really improved
In my opinion, the biggest improvement was not that the output became longer or more polished, but that it became more controlled. The earlier version sometimes sounded too smooth, and because of that, vague points could end up looking more confirmed than they actually were. The later version did a better job of avoiding that problem. This was especially important in cases where pricing, timelines, or follow-up actions were still not fully decided, because the final version stayed closer to the original notes.

## What is still not working well
Even after several rounds of prompt changes, the prototype still has limits. The most obvious problem is that if the original notes are too vague, the model may still produce an answer that looks reasonable but is not reliable enough. Another issue is that the model can sometimes make a messy discussion sound too neat, which makes the result easier to read but may hide the fact that the original information was incomplete. This risk becomes even bigger when the notes involve price changes, agreement changes, or unclear client attitudes.

## My final thoughts
Overall, I think this workflow is useful, but it is more suitable as a first-draft tool than a final decision tool. It can save time by helping people organize rough notes into a clearer structure, especially in lower-stakes internal situations. But if the content involves more sensitive decisions, or if the information itself is still uncertain, I think a person still needs to check it carefully. In other words, this workflow can improve efficiency, but it should not replace human judgment.