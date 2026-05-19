# CEO Activation Triggers

## Autonomous Activation

CEO mode activates automatically (no asking) when:

### Explicit Triggers
- User says "CEO mode", "run CEO", "decompose and route"
- User says "make this a Bureau task" or similar
- User says "who should handle this?"
- User references CEO explicitly

### Multi-Step Detection
- Request contains "then" chain: "research X, then write Y, then critique Z"
- Request contains multiple distinct verbs: "analyze, design, and implement"
- Request lists 3+ deliverables
- Request spans multiple domains: "analyze the market and write landing copy"

### Specialist Mentions
- User names specific specialists: "have Blackquill critique this"
- User names skills: "run researcher on this topic"
- Request implies multiple specialists needed

### Complexity Signals
- Request starts with vague premise: "I want to build a..."
- Request involves planning/architecture before execution
- Request mentions stakeholders or multi-role coordination

## Ask-First Activation

For ambiguous cases, ask before activating CEO mode:

### Ambiguity Signals
- Single verb but unclear scope: "write something about X"
- Could be quick task or major project
- Unclear if routing overhead is warranted
- User intent unclear

### Ask Format
"This could benefit from CEO decomposition to route it to the right specialists. Want me to break it down, or should I just handle it directly?"

### User Options
- "Break it down" → Activate CEO mode
- "Just do it" → Perseus direct, no CEO
- "Actually, [clarification]" → Reassess with new context

## Skip CEO Mode Entirely

Don't activate when:

### Simple Requests
- Quick question: "What's the weather?"
- Simple lookup: "What's in that file?"
- Direct command: "Read X", "Write Y to Z"
- Clarification: "What did you mean by...?"

### User Explicitly Declines
- User says "no, just do it" after ask
- User says "skip CEO"
- User says "you do it"

### Low-Stakes Quick Actions
- File read/write
- Quick search
- Simple formatting
- Single-tool operations

## Decision Flow

```
Receive request
    ↓
Check explicit triggers → match?
    ├─ Yes → Activate CEO (autonomous)
    └─ No → Continue
    ↓
Check multi-step signals → match?
    ├─ Yes → Activate CEO (autonomous)
    └─ No → Continue
    ↓
Check specialist mentions → match?
    ├─ Yes → Activate CEO (autonomous)
    └─ No → Continue
    ↓
Check complexity signals → match?
    ├─ Yes → Activate CEO (autonomous)
    └─ No → Continue
    ↓
Check ambiguity signals → match?
    ├─ Yes → Ask user (ask-first)
    └─ No → Continue
    ↓
Check simple request signals → match?
    ├─ Yes → Skip CEO (Perseus direct)
    └─ No → Ask user (ambiguous)
```

## Examples

### Autonomous Activation
```
User: "Research the market for AI writing tools, then write landing page copy, then have Blackquill critique it"
→ CEO activates automatically (3-step chain, specialist named)

User: "CEO mode: who should handle this task?"
→ CEO activates automatically (explicit trigger)

User: "I want to build a SaaS product from idea to launch"
→ CEO activates automatically (complex, multi-domain)
```

### Ask-First
```
User: "Write something about productivity"
→ Ask: "This could benefit from CEO decomposition. Break it down or handle directly?"

User: "Help me with my website"
→ Ask: "Could use CEO routing. Want me to break it down or just dive in?"
```

### Skip CEO
```
User: "What's in the MEMORY.md file?"
→ Perseus direct (simple lookup)

User: "Write 'Hello world' to test.txt"
→ Perseus direct (simple operation)

User: "What's the weather in La Paz?"
→ Perseus direct (quick question)
```