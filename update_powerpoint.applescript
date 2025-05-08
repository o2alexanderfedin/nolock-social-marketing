-- AppleScript to update PowerPoint presentation with new text
-- This script will update the PowerPoint slides with content from markdown files

on run
	tell application "Microsoft PowerPoint"
		activate
		set pptFilePath to "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
		
		-- Open the presentation
		open pptFilePath
		delay 2
		
		set activePresentation to active presentation
		
		-- Update slide 1 (Title slide)
		log "Updating slide 1..."
		-- Read content from markdown file
		set slideContent to read file "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides/slide01.md"
		tell slide 1 of activePresentation
			-- Update title text
			tell shape 1
				if has text frame then
					tell text frame
						tell text range
							set content to "NoLock Social"
						end tell
					end tell
				end if
			end tell
			-- Update subtitle text
			tell shape 2
				if has text frame then
					tell text frame
						tell text range
							set content to "Rebuild Trust in the Digital Space"
						end tell
					end tell
				end if
			end tell
		end tell
		
		-- Update slide 2 (Problem I)
		log "Updating slide 2..."
		-- Read content from markdown file
		set slideContent to read file "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides/slide02.md"
		tell slide 2 of activePresentation
			-- Update title
			tell shape 1
				if has text frame then
					tell text frame
						tell text range
							set content to "The Problem I"
						end tell
					end tell
				end if
			end tell
			-- Update subtitle
			tell shape 2
				if has text frame then
					tell text frame
						tell text range
							set content to "Distrust in Digital Space"
						end tell
					end tell
				end if
			end tell
		end tell
		
		-- Save the presentation
		save activePresentation
		
		-- Provide user feedback
		display dialog "PowerPoint presentation has been updated successfully!" buttons {"OK"} default button "OK"
		
	end tell
end run

on readMarkdownContent(filePath)
	-- Helper function to read markdown file content
	set contentFile to open for access filePath
	set markdownContent to read contentFile
	close access contentFile
	return markdownContent
end readMarkdownContent