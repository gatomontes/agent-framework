# Profession-to-Routing Mapping

## Installed Skills (OpenClaw)

| Profession | Skill | Mode | Notes |
|------------|-------|------|-------|
| **Critic / Attack Analyst** | `blackquill` | Skill activation | Uncensored critique, challenges assumptions |
| **Researcher / Evidence Gatherer** | `researcher` | Skill activation | Bias-controlled fact gathering |
| **Direct-Response Copywriter** | `direct-response-copywriter` | Skill activation | Conversion-focused copy |
| **CRO Strategist** | `cro-strategist` | Skill activation | Experiment design, funnel optimization |
| **Full-Stack Growth Engineer** | `full-stack-growth-engineer` | Skill activation | Tracking, analytics, tech growth |
| **Symfony Architect** | `symfony-architect` | Skill activation | Enterprise PHP architecture |
| **Pitchman / Sales Copy** | `pitchman` | Skill activation | Billy Mays style sales copy |
| **Design System Extractor** | `design-system-extractor` | Skill activation | UI/UX pattern documentation |
| **Web Design Orchestrator** | `web-design-orchestrator` | Skill activation | Multi-persona site design |
| **YouTube Comment Miner** | `yt-comment-friction-miner` | Skill activation | Audience pain/confusion mining |
| **Lyric Generator** | `b-lyrics` | Skill activation | Bureau-native lyric writing |
| **Title Ideation** | `b-title` | Skill activation | Song title generation |
| **Reminder Handler** | `reminder` | Skill activation | Natural language reminders |
| **Chat Gateway Bot Designer** | `chat-gateway` | Skill activation | Bot workflow design |

## Subagent Routing (Session Spawn)

Use `sessions_spawn` when:
- No skill matches the profession slot
- Task needs isolated execution context
- Task requires specific model capability
- Task is complex enough to warrant fresh session

### Subagent Configuration Patterns

**Research Subagent:**
```json
{
  "runtime": "subagent",
  "mode": "run",
  "task": "[research prompt]",
  "model": "qwen2.5:7b"
}
```

**Code Implementation Subagent:**
```json
{
  "runtime": "subagent",
  "mode": "run",
  "task": "[implementation prompt]",
  "model": "qwen2.5-coder:7b"
}
```

**Persistent Session (thread-bound):**
```json
{
  "runtime": "acp",
  "mode": "session",
  "thread": true,
  "agentId": "[specific agent if needed]"
}
```

## Planning Runtime Direct Execution

Route to Planning Runtime (exit CEO mode) when:
- Simple single-step task
- Quick file operation
- Direct question/answer
- User explicitly says "just do it"
- Task doesn't warrant specialist overhead

## Fallback Decision Tree

```
1. Check installed skills → match?
   ├─ Yes → Skill activation
   └─ No → Continue

2. Check subagent routing → warrants isolated context?
   ├─ Yes → sessions_spawn
   └─ No → Continue

3. Check complexity → warrants specialist?
   ├─ Yes → Ask user which route
   └─ No → Planning Runtime direct (exit CEO mode)
```
