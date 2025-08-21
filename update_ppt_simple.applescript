-- Simple AppleScript to directly update PowerPoint slides

tell application "Microsoft PowerPoint"
	activate
	-- Open the presentation
	set pptPath to "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
	open pptPath
	delay 2
	
	-- Update slide 2
	tell slide 2 of active presentation
		-- Update title (shape 1)
		tell shape 1
			set text frame text to "The Problem I"
		end tell
		
		-- Update subtitle (shape 2)
		tell shape 2
			set text frame text to "Distrust in Digital Space"
		end tell
	end tell
	
	-- Save the presentation
	save active presentation
	
	-- Display confirmation
	display dialog "Slide 2 has been updated!" buttons {"OK"} default button "OK"
end tell