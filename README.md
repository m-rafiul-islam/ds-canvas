# ds-canvas

This repository contains Canvas-compatible QTI quiz materials for data science topics.

## Contents

- `imsmanifest.xml` — QTI package manifest
- `seaborn_question_bank.xml` — Seaborn question bank with 50 mixed-format questions

## Quiz Topics

The Seaborn question bank covers:

- Seaborn basics
- Plot types and use cases
- Distribution plots
- Categorical plots
- Relational plots
- Regression plots
- Styling and themes
- Heatmaps and matrix visualizations
- Figure-level vs axes-level functions

## Question Types

The bank includes a mix of:

- Multiple choice
- True/false
- Matching
- Fill-in-the-blank

## Import Notes

This package is intended for Canvas import workflows.

Depending on your Canvas configuration, you may be able to import the QTI package into:

- a classic quiz question bank, or
- a New Quizzes-compatible workflow

If your institution uses New Quizzes, import behavior may vary slightly based on Canvas account settings.

## How to Use

1. Download or clone this repository.
2. Ensure the QTI files are placed in the correct package folder.
3. Zip the package contents.
4. Import the `.zip` file into Canvas.

## Recommended Package Structure

```text
QTI/
├── imsmanifest.xml
└── seaborn_question_bank.xml
```

## Status

This repository is set up to host a Seaborn question bank for Canvas.
