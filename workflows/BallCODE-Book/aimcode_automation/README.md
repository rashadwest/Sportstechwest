# AIMCODE Automation System

Fully automated system using AIMCODE methodology to validate, generate, and manage BallCODE content.

## Installation

```bash
# No external dependencies required (uses standard library)
cd aimcode_automation
```

## Usage

### Validate a Story

```bash
python aimcode_story_validator.py --story ../book-1-story.md --episode 1
```

### Validate All Stories

```bash
for story in ../book-*-story.md; do
    python aimcode_story_validator.py --story "$story"
done
```

## Validators

- `aimcode_validators.py` - Core validation classes for all AIMCODE pillars
- `aimcode_story_validator.py` - Story validation script

## AIMCODE Pillars

1. **Zhang** - Story framework (basketball first)
2. **Resnick** - Building activities (hands-on creation)
3. **Reggio** - Multiple entry points (student choice)
4. **Hassabis** - Systematic progression (layer by layer)
5. **Jobs** - Simple design (it just works)

## Output

Validation results are saved as JSON files with detailed feedback for each pillar.



