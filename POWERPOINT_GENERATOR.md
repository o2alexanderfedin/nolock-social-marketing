# NoLock Social PowerPoint Generator

This tool automatically generates PowerPoint presentations from the markdown slides in the NoLock Social pitch decks.

## Features

- **Dual Presentation Generation**: Creates both simplified and detailed presentations
- **Presentation Notes**: Includes design elements and pitch notes in presenter view
- **Bullet Point Formatting**: Properly formats bullet points for clean slides
- **Image Integration**: Incorporates images from the image directory
- **Title Slide**: Adds a professional title slide with generation date

## Requirements

- macOS operating system
- Microsoft PowerPoint installed
- NoLock Social pitch deck files in the correct directory structure

## Usage

To generate the PowerPoint presentations, run the following command from the terminal:

```bash
cd /Users/alexanderfedin/Projects/nolock.social/marketing
./generate_powerpoint.sh
```

This will create two PowerPoint files in the marketing directory:
- `NoLock_Partner_Simplified.pptx` - Optimized for live presentations with reduced text
- `NoLock_Partner_Detailed.pptx` - Complete documentation with full details

## Advanced Options

If you encounter issues with the enhanced version, you can use the basic generator:

```bash
./generate_powerpoint.sh --basic
```

## Output Files

The generated PowerPoint files will be placed in:
- `/Users/alexanderfedin/Projects/nolock.social/marketing/NoLock_Partner_Simplified.pptx`
- `/Users/alexanderfedin/Projects/nolock.social/marketing/NoLock_Partner_Detailed.pptx`

## Presentation Best Practices

When presenting with these decks:

1. **Use Presenter View**: Access your pitch notes during the presentation
2. **Simplified Deck for Live Presentations**: Use the simplified deck when presenting live
3. **Detailed Deck for Documentation**: Share the detailed deck as leave-behind material
4. **Customize as Needed**: Edit the generated presentations to customize for specific audiences

## Troubleshooting

If the script fails to generate the presentations:

1. Ensure Microsoft PowerPoint is installed and accessible
2. Check that the slide markdown files are in the correct directory structure
3. Try running with the `--basic` flag for a simpler generation approach
4. Verify that you have read/write permissions in the marketing directory

## How It Works

The generator uses AppleScript to:
1. Read the markdown files from the slides directories
2. Extract titles, content, design elements, and pitch notes
3. Create PowerPoint slides with appropriate layouts
4. Format content including bullet points and text
5. Add images where available
6. Include design elements and pitch notes in the presenter notes
7. Save the presentations in the marketing directory

## Source Files

The generator consists of:
- `generate_powerpoint.sh`: Main shell script to run the generator
- `generate_powerpoint_enhanced.applescript`: Enhanced PowerPoint generation script
- `generate_powerpoint_presentations.applescript`: Basic PowerPoint generation script