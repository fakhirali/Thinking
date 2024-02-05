# Thought Process

### TODO:
- [ ] Canvas html app
- [ ] Flask backend
- [ ] Better methods for storing the graph
- [ ] Extended descriptions of statements
- [ ] Simple LLM reasoning agent example

I want to make an app that allows me to think through 
decisions logically. Instead of pros and cons it 
should be premise conclusion.

There can be:
- fact with referenced evidence.
- Premise
- Conclusion given premise(s) with reasoning

Each of these can be voted on to say if you agree or disagree.
Statements can be refuted by giving counter evidence or reasoning.
There is a case where premises and conclusions are probable.
Meaning they could be true or not based on some probability. 
Assumptions would be used to handle such cases.

- LLM warns when going off topic
- When premises do not support conclusion
- When evidence is not relevant

Note:
This may also help LLM reasoning.