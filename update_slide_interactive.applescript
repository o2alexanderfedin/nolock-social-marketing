-- AppleScript to interactively update specific PowerPoint slides
-- This script prompts the user to select which slide to update

on run
	tell application "Microsoft PowerPoint"
		activate
		set pptFilePath to "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
		
		-- Open the presentation
		open pptFilePath
		delay 2
		
		set activePresentation to active presentation
		set slideCount to count of slides of activePresentation
		
		-- Ask user which slide to update
		display dialog "Enter the slide number to update (1-" & slideCount & "):" default answer "2"
		set slideNum to text returned of result as integer
		
		if slideNum < 1 or slideNum > slideCount then
			display dialog "Invalid slide number. Please enter a number between 1 and " & slideCount & "." buttons {"OK"} default button "OK"
			return
		end if
		
		-- Get slide content from investor pitch deck
		set slideNumString to text -2 thru -1 of ("0" & slideNum)
		set markdownPath to "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides/slide" & slideNumString & ".md"
		
		-- Check if markdown file exists
		tell application "System Events"
			if not (exists file markdownPath) then
				display dialog "Source content file not found: " & markdownPath buttons {"OK"} default button "OK"
				return
			end if
		end tell
		
		-- Read the markdown content
		set mdContent to do shell script "cat " & quoted form of markdownPath
		
		-- Extract title and subtitle using shell commands
		set titleText to do shell script "grep -m 1 '^# ' " & quoted form of markdownPath & " | sed 's/^# //'"
		set subtitleText to do shell script "grep -m 1 '^## ' " & quoted form of markdownPath & " | sed 's/^## //'"
		
		-- Show the content to the user and confirm update
		set confirmMsg to "Update slide " & slideNum & " with the following content?
Title: " & titleText & "
Subtitle: " & subtitleText
		
		display dialog confirmMsg buttons {"Cancel", "Update"} default button "Update"
		if button returned of result is "Cancel" then
			return
		end if
		
		-- Update the slide
		tell slide slideNum of activePresentation
			-- Update title
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
				display dialog "Error updating title: " & errMsg buttons {"OK"} default button "OK"
			end try
			
			-- Update subtitle
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
				display dialog "Error updating subtitle: " & errMsg buttons {"OK"} default button "OK"
			end try
		end tell
		
		-- Go to the updated slide
		tell activePresentation
			go to slide slideNum
		end tell
		
		-- Save the presentation
		save activePresentation
		
		-- Provide user feedback
		display dialog "Slide " & slideNum & " has been updated successfully!" buttons {"OK"} default button "OK"
		
	end tell
end run