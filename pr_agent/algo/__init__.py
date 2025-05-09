MAX_TOKENS = {
    "o3-mini": 200000,
    "gpt-4.1-mini": 1047576,
    "DeepSeek-V3": 128000,
    "DeepSeek-R1": 128000,
    "gpt-4o-mini": 128000,
    "o4-mini": 200000,
    "text-embedding-3-large": 8191,
    "o1": 200000,
    "gpt-4.1": 1047576,
    "gpt-4o": 128000,
    "gpt-4.1-nano": 1047576,
    "o3": 200000,
    "o1-mini": 128000,
}

USER_MESSAGE_ONLY_MODELS = [
    "deepseek/deepseek-reasoner",
    "o1-mini",
    "o1-mini-2024-09-12",
    "o1-preview"
]

NO_SUPPORT_TEMPERATURE_MODELS = [
    "deepseek/deepseek-reasoner",
    "o1-mini",
    "o1-mini-2024-09-12",
    "o1",
    "o1-2024-12-17",
    "o3-mini",
    "o3",
    "o3-mini-2025-01-31",
    "o1-preview",
    "o3",
    "o3-2025-04-16",
    "o4-mini",
    "o4-mini-2025-04-16",
]

SUPPORT_REASONING_EFFORT_MODELS = [
    "o3-mini",
    "o3-mini-2025-01-31",
    "o3",
    "o3-2025-04-16",
    "o4-mini",
    "o4-mini-2025-04-16",
]

CLAUDE_EXTENDED_THINKING_MODELS = [
    "anthropic/claude-3-7-sonnet-20250219",
    "claude-3-7-sonnet-20250219"
]
