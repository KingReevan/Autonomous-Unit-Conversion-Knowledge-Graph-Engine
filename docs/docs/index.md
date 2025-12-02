# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

# Extract Units

`ExtractUnits` is the DSPy module used to convert natural-language questions
into clean `(from_unit, to_unit)` pairs.

## Source Code

```python
class ExtractUnits(dspy.Module):
    def __init__(self):
        super().__init__()
        self.extract = dspy.Predict("question -> from_unit, to_unit")

    def forward(self, question: str):
        raw = self.extract(question=question)
        ext = ExtractedUnits.model_validate(raw.toDict())
        return ext
