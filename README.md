# Golden Ratio Lab

An interactive Python project that explores the golden ratio (φ ≈ 1.618):
the math behind it, how to visualize it, and how to test the popular claim
that it appears "everywhere" in art and nature.

> 🚧 **Status:** work in progress. See the [roadmap](#roadmap).

**Live app:** _link coming soon (Streamlit Community Cloud)_

<!-- Add a screenshot or GIF here when the app is ready:
![Screenshot of the app](docs/screenshot.png)
-->

## What you can do in the app

- **Fibonacci:** compare three ways to compute it (loop, recursion, Binet's formula) and see F(n+1)/F(n) converge to φ.
- **Spiral:** draw a golden spiral over Fibonacci rectangles.
- **Sunflower:** generate a phyllotaxis pattern with the golden angle (≈ 137.5°) and use a slider to see the pattern break with other angles.
- **Image analyzer:** upload an image and overlay a golden grid or the rule of thirds.

## Myth vs. fact

The golden ratio is often said to be hidden in the Parthenon, the Mona Lisa, human faces and seashells. Many of these claims are exaggerated or based on loose measurements.

| Claim | Reality |
|-------|---------|
| Fibonacci ratios converge to φ | ✅ **Fact.** This is a mathematical result. |
| Some plants use the golden angle | ✅ **Mostly fact.** It helps pack seeds efficiently, but many plants do not follow it. |
| The Parthenon / Mona Lisa follow φ | ⚠️ **Weak evidence.** Results depend on where you choose to measure. |
| Nautilus shells are golden spirals | ❌ **Myth.** Their growth ratio is usually different from φ. |
| Beautiful faces follow φ | ⚠️ **Not supported** by strong evidence. |

_Sources and references will be added as I research each claim._

## Project structure

```
golden-ratio-lab/
├── app.py                  # Streamlit main page
├── pages/                  # Streamlit pages (one per topic)
├── golden/                 # Pure logic (does not import Streamlit)
│   ├── fibonacci.py
│   ├── geometry.py
│   └── image_tools.py
├── tests/                  # pytest tests
├── requirements.txt
└── README.md
```

**Design principle:** the math and image logic live in `golden/`, separate from the interface. This makes the code easier to test and reuse.

## Installation

Requires Python 3.10+ (macOS / Linux).

```bash
git clone https://github.com/danielpetla/Golden-Ratio-Lab.git
cd golden-ratio-lab
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Running the tests

```bash
pytest
```

## Roadmap

- [ ] Fibonacci: loop, recursion, Binet's formula, performance comparison
- [ ] Plot of F(n+1)/F(n) converging to φ
- [ ] Golden spiral over Fibonacci rectangles
- [ ] Phyllotaxis with an adjustable angle slider
- [ ] Image analyzer with golden grid and rule-of-thirds overlays
- [ ] Tests with pytest
- [ ] Deploy on Streamlit Community Cloud
- [ ] Extras: continued fractions, Newton and bisection methods

## Tech stack

Python · NumPy · Matplotlib · Pillow / OpenCV · Streamlit · pytest

## About

I am building this project to learn Python and data visualization, and to show how I structure and test code.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.