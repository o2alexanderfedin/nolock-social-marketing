-- Simple AppleScript to create PowerPoint presentations
-- Creates both simplified and detailed presentations

on run
	display dialog "Creating NoLock Social PowerPoint presentations..." buttons {"Continue"} default button "Continue"
	
	-- Define paths
	set marketingDir to "/Users/alexanderfedin/Projects/nolock.social/marketing"
	set basePath to marketingDir & "/pitch-decks/customer-partner"
	
	-- Create simplified presentation
	tell application "Microsoft PowerPoint"
		-- Create a new presentation
		set simplifiedPresentation to make new presentation
		
		-- Add a title slide
		set titleSlide to make new slide at simplifiedPresentation with properties {layout:title slide}
		set shape range of title placeholder of titleSlide to "NoLock Social"
		set shape range of subtitle placeholder of titleSlide to "Simplified Partner Pitch Deck" & return & "For Presentation Use"
		
		-- Add content slides
		repeat with i from 1 to 21
			set slideNumStr to text -2 thru -1 of ("0" & i)
			
			set newSlide to make new slide at simplifiedPresentation with properties {layout:title and content}
			set shape range of title placeholder of newSlide to "Slide " & i
			
			-- Add bullet points (sample content - you'll need to replace this with actual content)
			if i = 1 then
				set contentText to "NOLOCK•SOCIAL" & return & return & "PARTNERSHIP OPPORTUNITIES" & return & return & "REBUILD TRUST TOGETHER"
			else if i = 2 then
				set contentText to "• ENHANCE solutions with trust verification" & return & "• REDUCE storage costs by 40%" & return & "• DIFFERENTIATE with premium features" & return & "• EXPAND into privacy-focused markets"
			else
				set contentText to "• Bullet point 1 for slide " & i & return & "• Bullet point 2 for slide " & i & return & "• Bullet point 3 for slide " & i
			end if
			
			set shape range of content placeholder of newSlide to contentText
			
			-- Add notes with pitch notes
			set notes text of newSlide to "Pitch notes for slide " & i & ":" & return & return & "Presentation tips and talking points will appear here."
		end repeat
		
		-- Save the presentation
		save simplifiedPresentation in (marketingDir & "/NoLock_Partner_Simplified.pptx")
		close simplifiedPresentation saving yes
		
		-- Create detailed presentation (similar approach)
		set detailedPresentation to make new presentation
		
		set titleSlide to make new slide at detailedPresentation with properties {layout:title slide}
		set shape range of title placeholder of titleSlide to "NoLock Social"
		set shape range of subtitle placeholder of titleSlide to "Detailed Partner Pitch Deck" & return & "For Documentation Use"
		
		repeat with i from 1 to 21
			set newSlide to make new slide at detailedPresentation with properties {layout:title and content}
			set shape range of title placeholder of newSlide to "Slide " & i & " (Detailed)"
			
			-- Different content for detailed slides
			set contentText to "Detailed content for slide " & i & ":" & return & return & "• More comprehensive information" & return & "• Technical specifications" & return & "• Implementation details" & return & "• Complete feature descriptions"
			
			set shape range of content placeholder of newSlide to contentText
			set notes text of newSlide to "Detailed presentation notes for slide " & i
		end repeat
		
		save detailedPresentation in (marketingDir & "/NoLock_Partner_Detailed.pptx")
		close detailedPresentation saving yes
	end tell
	
	display dialog "PowerPoint presentations created successfully!" buttons {"OK"} default button "OK"
end run