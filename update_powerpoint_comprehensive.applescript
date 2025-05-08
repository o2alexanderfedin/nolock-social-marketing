-- AppleScript to update PowerPoint presentation with new text from markdown files
-- This script updates all slides in the presentation based on content from the pitch-deck-investor-full directory

on run
	tell application "Microsoft PowerPoint"
		activate
		set pptFilePath to "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
		
		-- Open the presentation
		open pptFilePath
		delay 3 -- Allow time for the presentation to open
		
		set activePresentation to active presentation
		set slideCount to count of slides of activePresentation
		
		-- Log information about presentation
		log "Presentation opened: " & name of activePresentation
		log "Total slide count: " & slideCount
		
		-- Update each slide with content from corresponding markdown file
		repeat with i from 1 to slideCount
			updateSlide(i, activePresentation)
		end repeat
		
		-- Save the presentation
		save activePresentation
		
		-- Provide user feedback
		display dialog "PowerPoint presentation has been updated successfully!" buttons {"OK"} default button "OK"
		
	end tell
end run

on updateSlide(slideNum, presentation)
	-- Function to update a specific slide
	set slideNumString to text -2 thru -1 of ("0" & slideNum)
	set markdownPath to "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides/slide" & slideNumString & ".md"
	
	-- Check if markdown file exists
	tell application "System Events"
		if exists file markdownPath then
			log "Updating slide " & slideNum & " with content from " & markdownPath
			
			-- Extract title and subtitle from markdown file
			set mdContent to do shell script "cat " & quoted form of markdownPath
			
			set titlePattern to "# "
			set subtitlePattern to "## "
			
			set titleText to ""
			set subtitleText to ""
			
			-- Parse markdown content for title and subtitle
			set paragraphs to paragraphs of mdContent
			repeat with p in paragraphs
				set p to p as text
				if p starts with titlePattern and titleText is "" then
					set titleText to text (length of titlePattern + 1) thru -1 of p
				else if p starts with subtitlePattern and subtitleText is "" then
					set subtitleText to text (length of subtitlePattern + 1) thru -1 of p
				end if
			end repeat
			
			log "Title: " & titleText
			log "Subtitle: " & subtitleText
			
			-- Update the slide
			tell application "Microsoft PowerPoint"
				tell presentation
					tell slide slideNum
						-- Try to update title
						try
							tell shape 1
								if has text frame then
									tell text frame
										tell text range
											set content to titleText
										end tell
									end tell
								end if
							end tell
						on error errMsg
							log "Error updating title on slide " & slideNum & ": " & errMsg
						end try
						
						-- Try to update subtitle
						try
							tell shape 2
								if has text frame then
									tell text frame
										tell text range
											set content to subtitleText
										end tell
									end tell
								end if
							end tell
						on error errMsg
							log "Error updating subtitle on slide " & slideNum & ": " & errMsg
						end try
					end tell
				end tell
			end tell
		else
			log "Markdown file not found for slide " & slideNum & ": " & markdownPath
		end if
	end tell
end updateSlide