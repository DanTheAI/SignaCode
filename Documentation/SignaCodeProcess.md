# SignaCode Build Process: Hypergeometric Distribution Calculator

SignaCodeGPT: https://chatgpt.com/g/g-67827be5d7b8819184aafbee9054f8e0-signacode

## Overview of SignaCode Framework
SignaCode is a mental framework for transforming ideas into code through structured symbolic layers:

| Step | Description | Symbolic Layer |
|------|-------------|----------------|
| 1. | Idea Expression | Raw thought → s |
| 2. | Conversational Structuring | Shape into F(x) |
| 3. | Problem Statement Formation | Define scope |
| 4. | Logical Abstraction | Reduce to ∈ λ |
| 5. | Execution Mapping | System interface = Ξ |
| 6. | Code Realization | Generated output |

## Application to HDC (Hypergeometric Distribution Calculator)

### 1. Idea Expression (s)
Raw thought conceptualization of a tool for competitive card game players to calculate draw probabilities:
- "Need a tool to calculate probability of drawing specific cards"
- "Must help optimize deck building strategies"
- "Should account for first/second player differences"

### 2. Conversational Structuring F(x)
Shaping the idea into a functional relationship:
- Input: Deck parameters (size, desired cards, draw amount)
- Output: Statistical probability
- F(deck_size, desired_cards, draw_amount, success_criteria) → probability

### 3. Problem Statement Formation
Defined in HDC.md:
```
Building a Hypergeometric Distribution Calculator for Competitive Deck Optimization
```
- Identified key use cases:
  - Probability of drawing specific card combinations
  - Optimization thresholds
  - First vs. second player scenarios

### 4. Logical Abstraction (∈ λ)
Reduced to mathematical formula using lambda calculus representation:

λN.λK.λn.λk. (K choose k)⋅(N−K choose n−k)/(N choose n)

Where:
- N: Total deck size
- K: Number of desired cards
- n: Number of cards drawn
- k: Successful draws

### 5. Execution Mapping (Ξ)
Interface design and system requirements:
- GUI with input fields
- Calculation function binding
- Result display
- Error handling
- Table visualization for probability distribution

### 6. Code Realization
Implementation in three progressive versions, showing the evolution of development environments:

#### v1_HDC.py (Created via AI Prompting)
- Basic functionality implemented entirely through conversational AI prompting
- Simple four-field interface
- Core probability calculation
- Limited to single probability output
- Formula implementation through direct AI code generation
- No modification to the initial AI output

#### v2_HDC.py (VS Code Refinement)
- Enhanced UI built upon v1's foundation
- Migrated development from AI prompting to VS Code
- Added opening hand presets
- Implemented probability table view 
- Game-specific templates
- Improved visual design
- Human-refined code structure and organization

#### v3_HDC.py (Advanced VS Code Development)
- Multiple K-value support
- Tabbed interface for complex calculations
- Advanced visualization components
- Optimized for competitive card game analysis
- Fully human-customized in VS Code environment
- Expanded feature set based on iterative testing and refinement

## Evolution Across Versions

### Mathematical Core
The core mathematical function remained consistent across all versions:
```python
def hypergeometric_probability(N, K, n, k):
    try:
        return (comb(K, k) * comb(N - K, n - k)) / comb(N, n)
    except ValueError:
        return 0
```

### Development Environment Evolution
- v1: Pure AI-generated code through conversational prompting
- v2: Initial VS Code refinement with human guidance
- v3: Full VS Code development with advanced features and human customization

### Interface Evolution
- v1: Basic four-field input form with minimal styling
- v2: Added game presets, improved aesthetics, and probability table
- v3: Implemented multiple card type tracking (K-values) with sophisticated UI components

### Functionality Expansion
- v1: Single probability calculation (AI-generated)
- v2: Added table view and game-specific templates (VS Code enhanced)
- v3: Support for multiple card types and interactive visualization (VS Code optimized)

## Conclusion
The SignaCode framework provided a structured approach to developing the Hypergeometric Distribution Calculator, moving from abstract mathematical concepts expressed through AI prompting to a fully-realized tool refined in VS Code. This hybrid development approach demonstrates how ideas can flow from conceptualization (AI prompting) to advanced implementation (VS Code refinement), resulting in a comprehensive application that addresses the needs of competitive deck builders.
