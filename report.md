# Report

## What I made this time
In this assignment, I made a relatively small workflow, whose main function was to organize the original discussion notes into a clearer summary. notes here can come from customer communication, project discussions, or more mundane business conversation. I did this because I think this scenario is very common. In reality, a lot of notes are memorized while listening, and the content is often fragmented. If you only remember the key words, it is not so easy to understand them when you look back later. So I wanted to try to see if the big model could sort out the messy original notes into a clearer first draft.

## Why did I choose this direction
I chose this direction mainly because it's more practical and easier to apply to real-world use cases. Whether it is a group project or a more business-related discussion, the way people take notes is usually not particularly complete, and most of the time they just write down the key points. While this is convenient right now, it will take time to organize later. The value of this workflow is that it can first turn these pieces of content into a more readable version, or at least help users quickly understand what's discussed and what to do next. In addition, I think this is a good task to test models on, because the hard part is not just "can I summarize?" but "can I guess when I have incomplete information?"

## The models I used and the overall approach
This time I used Gemini, got the API key from Google AI Studio, and made a simple prototype in Python. I chose this combination mainly because it is easier to get started with and more suitable for small experiments such as this assignment. My focus this time was not really to compare many different models, but to set up the workflow first, then use a fixed evaluation set to see the effect, and then improve the output step by step by changing the prompt. So for me, Gemini is more than enough for this task.

## How did I change my prompt step by step
I started with a simple prompt, telling the model to turn the discussion notes into a summary with key points and follow-through items. The result is mostly readable, but the problem is that it can sometimes be a bit more generic, and the model can be a bit more certain than the original notes on things that are inherently less certain.

The first change I made was to fix the output format. I have divided the results into Summary, Key Points, Action Items and Risks or Uncertainty sections. After doing this, the output will look clearer and it will be easier for me to compare different cases.

In the last edition, I added more explicit restrictions, such as not adding information that wasn't in the original notes, not writing "possible thoughts" as "already decided," and keeping uncertainty in the notes if there was uncertainty. With this change, the model will be able to handle cases with incomplete information or higher risk, or at least be less prone to saying the wrong thing.

## What I think is really getting better
In my opinion, the most noticeable change is not that the output is longer, or that the text looks better, but that the output is a little more "curled up" than it was at the beginning. The previous version can sometimes feel easy to write, but the problem is that it is too smooth, and it is easy to clean up what should be vague as if it has been confirmed. Later versions are much better at controlling this, especially in cases where pricing, timing, or follow-up actions are not yet determined, and it's closer to the original notes.

## What's wrong with the prototype today
Although prompt has gone through several rounds, the prototype still has limitations. The most obvious one is that as long as the original notes themselves are too vague, the model may still output a "reasonable looking" version, but that version may not be reliable enough. In another case, the model will try to smooth out a messy discussion too much, which may make it clearer, but may also blind you to the fact that the original information is incomplete. This risk is even greater when notes involve price adjustments, agreement changes, or customer attitudes themselves are not clear.

## My final thoughts
Overall, I found the workflow useful, but more appropriate as a first draft tool than a final word. It's a great way to save people time organizing their notes and get things into a clearer frame first, especially in low-stakes internal scenarios. But as long as the content involves more sensitive decisions, or the information itself has not been confirmed, I think someone has to look at it again. In other words, the workflow can help improve efficiency, but it is not a direct replacement for human judgment.