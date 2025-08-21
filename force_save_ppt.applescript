-- AppleScript to force save PowerPoint changes

tell application "Microsoft PowerPoint"
	activate
	
	-- Define presentation path
	set pptPath to "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
	
	-- Close any open presentations first
	if (count of presentations) > 0 then
		close active presentation saving no
	end if
	
	-- Open the presentation fresh
	open pptPath
	delay 3
	
	-- Make sure we have the active presentation
	set pres to active presentation
	
	-- Update slide 2
	tell slide 2 of pres
		-- Update title (shape 1)
		tell shape 1
			set content of text range to "THE PROBLEM I (UPDATED)"
		end tell
		
		-- Update subtitle (shape 2)
		tell shape 2
			set content of text range to "Distrust in Digital Space (UPDATED)"
		end tell
	end tell
	
	-- Force save with explicit path
	save pres in pptPath
	delay 2
	
	-- Display confirmation
	display dialog "Slide updated and saved to: " & pptPath buttons {"OK"} default button "OK"
end tell