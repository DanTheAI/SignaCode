# Hypergeometric Distribution Calculator (HDC) - Implementation Details

This folder contains the three evolutionary versions of the Hypergeometric Distribution Calculator, showing the progression from an AI-generated concept to a fully-featured application.

## Version Comparison

| Feature | v1_HDC.py | v2_HDC.py | v3_HDC.py |
|---------|-----------|-----------|-----------|
| Development | AI-generated via prompting | VS Code refinement | Advanced VS Code development |
| Interface | Basic 4-field form | Enhanced UI with game presets | Tabbed interface with multi-K support |
| Probability View | Single probability | Full probability table | Multi-card type tables |
| Card Game Support | Generic | Built-in game presets | Extended for complex analyses |
| Multi-card Tracking | No | No | Yes (up to 10 card types) |
| Results Display | Decimal probability | Percentage format | Multi-card percentages |

## Version Highlights

### v1_HDC.py - The Concept

The original AI-prompted version that implemented the core mathematical function:
- Basic 4-field input (N, K, n, k)
- Simple probability output
- No advanced features or styling
- Created entirely through prompting without modifications

### v2_HDC.py - The Enhancement

VS Code refinement with initial user experience improvements:
- Improved UI design and organization
- Added opening hand presets for popular card games
- Implemented probability tables showing exact, at-least, and at-most distributions
- Enhanced results display with percentage formatting
- Better instructions and user guidance

### v3_HDC.py - The Advanced Solution

Full-featured application with multi-card support:
- Support for up to 10 different card types (K values)
- Tabbed interface for complex analyses
- Dynamic form field generation
- Sophisticated probability tables with highlighting
- Comprehensive game support and advanced visualization

## Mathematical Core

All versions share the same core hypergeometric probability function:

```python
def hypergeometric_probability(N, K, n, k):
    try:
        return (comb(K, k) * comb(N - K, n - k)) / comb(N, n)
    except ValueError:
        return 0
```

This function calculates the probability of drawing exactly `k` cards of type `K` when drawing `n` cards from a deck of `N` total cards containing `K` desired cards.

## Usage Recommendations

- **For beginners**: Start with v1_HDC.py to understand the core concepts
- **For casual players**: v2_HDC.py provides a good balance of features and simplicity
- **For competitive players**: v3_HDC.py offers the full suite of analytical tools

## Development Process

Each version represents a distinct phase in the SignaCode development framework:
1. **v1**: Idea Expression → Code Realization via AI prompting
2. **v2**: Manual refinement with improved structuring and enhanced features
3. **v3**: Full logical abstraction with comprehensive functionality

See [../Documentation/SignaCodeProcess.md](../Documentation/SignaCodeProcess.md) for complete details on the development methodology.