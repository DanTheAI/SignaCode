# Hypergeometric Distribution Calculator (HDC)

A specialized tool designed for competitive card game players to calculate draw probabilities using hypergeometric distribution functions.

![SignaCode Framework](https://img.shields.io/badge/Framework-SignaCode-blue)
![Python](https://img.shields.io/badge/Python-3.6%2B-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

The Hypergeometric Distribution Calculator (HDC) helps competitive card game players optimize deck building by calculating the probability of drawing specific cards or combinations from a deck. The application evolved through the SignaCode framework - a methodology for transforming ideas into code through structured symbolic layers.

## Features

- Calculate probability of drawing specific cards from a deck
- Multiple card type tracking (up to 10 different card types)
- Probability tables showing exact, at-least, and at-most probabilities
- Built-in presets for popular card games (Magic: The Gathering, Pokémon TCG, Yu-Gi-Oh!, etc.)
- Visual highlighting of target probabilities
- Tabbed interface for complex calculations

## Evolution Through SignaCode

The project demonstrates the SignaCode development methodology:

1. **v1_HDC.py** - Created via AI prompting with basic hypergeometric calculator
2. **v2_HDC.py** - Enhanced in VS Code with game presets and probability tables
3. **v3_HDC.py** - Advanced VS Code development with multiple card type tracking

## Usage

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/SignaCode.git

# Navigate to the project directory
cd SignaCode

# Run the latest version
python HDC/v3_HDC.py
```

### Basic Example

1. Enter your deck size (e.g., 60 for Magic: The Gathering)
2. Enter the number of draws (e.g., 7 for an opening hand)
3. Enter the number of desired cards in your deck (e.g., 4 copies of a specific card)
4. Enter how many of those cards you want in your opening hand (e.g., at least 1)
5. Click "Calculate" to see the probability or "Show Table" for a detailed breakdown

### Advanced Features

- Use "Show Multiple K" to calculate probabilities for different card types simultaneously
- Add up to 10 different card types with "Add K" button
- View tabbed probability tables showing distributions for all card types

## The SignaCode Framework

This project was developed using the SignaCode framework, a mental model for transforming ideas into code:

| Step | Description | Symbolic Layer |
|------|-------------|----------------|
| 1. | Idea Expression | Raw thought → s |
| 2. | Conversational Structuring | Shape into F(x) |
| 3. | Problem Statement Formation | Define scope |
| 4. | Logical Abstraction | Reduce to ∈ λ |
| 5. | Execution Mapping | System interface = Ξ |
| 6. | Code Realization | Generated output |

For more information about the SignaCode methodology, see [Documentation/SignaCodeProcess.md](Documentation/SignaCodeProcess.md).

## Mathematical Foundation

The core hypergeometric function used:

```python
def hypergeometric_probability(N, K, n, k):
    try:
        return (comb(K, k) * comb(N - K, n - k)) / comb(N, n)
    except ValueError:
        return 0
```

Where:
- N: Total deck size
- K: Number of desired cards
- n: Number of cards drawn
- k: Successful draws

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built using the SignaCode framework
- Created for the competitive card gaming community
- Special thanks to contributors of the math.comb function in Python