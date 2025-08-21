-- Enhanced AppleScript to create PowerPoint presentations for NoLock Social
-- Creates both simplified and detailed presentations with proper formatting

on run
	-- Define paths and filenames
	set marketingDir to "/Users/alexanderfedin/Projects/nolock.social/marketing"
	set basePath to marketingDir & "/pitch-decks/customer-partner"
	set simplifiedDir to basePath & "/slides-simplified"
	set detailedDir to basePath & "/slides"
	set imagesDir to basePath & "/images"
	
	set simplifiedOutput to marketingDir & "/NoLock_Partner_Simplified.pptx"
	set detailedOutput to marketingDir & "/NoLock_Partner_Detailed.pptx"
	
	-- Create presentations
	my createPresentation(simplifiedDir, imagesDir, simplifiedOutput, "Simplified Partner Deck")
	my createPresentation(detailedDir, imagesDir, detailedOutput, "Detailed Partner Deck")
	
	display dialog "PowerPoint presentations created successfully!" buttons {"OK"} default button "OK"
end run

-- Main function to create a presentation
on createPresentation(slidesDir, imagesDir, outputPath, deckTitle)
	tell application "Microsoft PowerPoint"
		-- Create a new presentation using a blank template
		set newPresentation to make new presentation
		
		-- Set the theme to a clean, professional design
		set theme of newPresentation to theme "Wisp"
		
		-- Delete the default first slide if it exists
		if (count of slides of newPresentation) > 0 then
			delete slide 1 of newPresentation
		end if
		
		-- Process all 21 slides
		repeat with slideNum from 1 to 21
			-- Format slide number with leading zero
			set slideNumStr to my formatSlideNumber(slideNum)
			set slideFilePath to slidesDir & "/slide" & slideNumStr & ".md"
			
			-- Read and parse slide content
			set slideContent to my readFile(slideFilePath)
			set slideTitle to my extractTitle(slideContent)
			set slideText to my extractContent(slideContent)
			set designElements to my extractDesignElements(slideContent)
			set pitchNotes to my extractPitchNotes(slideContent)
			
			-- Determine layout based on slide content
			set layoutType to my determineLayoutType(slideText)
			
			-- Create a new slide with appropriate layout
			set newSlide to make new slide at end of slides of newPresentation with properties {layout:layoutType}
			
			-- Add the title
			set shape range of title placeholder of newSlide to slideTitle
			
			-- Handle content based on type (bullets or regular text)
			if my contentHasBullets(slideText) then
				-- Format as bullet points
				set bulletPoints to my extractBulletPoints(slideText)
				
				-- Get the content placeholder and add bullet points
				set contentShape to content placeholder of newSlide
				set tf to text frame of contentShape
				
				-- Clear existing text in the placeholder
				set text of tf to ""
				
				-- Add each bullet point
				repeat with i from 1 to length of bulletPoints
					set bulletPoint to item i of bulletPoints
					
					-- Add the bullet point text (trim leading bullet character if present)
					if bulletPoint starts with "•" or bulletPoint starts with "-" then
						set bulletText to text 2 thru -1 of bulletPoint
						set bulletText to my trimString(bulletText)
					else
						set bulletText to bulletPoint
					end if
					
					-- Add the text and set bullet format
					set newPara to make new paragraph at end of paragraphs of tf with properties {text:bulletText}
					
					-- Apply bullet formatting
					set bullet of newPara to true
					set bullet character of newPara to 8226 -- Unicode for bullet point •
				end repeat
			else
				-- Regular text, not bullets
				set content shape of newSlide to slideText
			end if
			
			-- Try to add the image if it exists
			set imageNum to slideNum as string
			set imagePath to imagesDir & "/slide" & imageNum & ".png"
			
			try
				set picturePath to POSIX file imagePath
				set pictureShape to make new picture at newSlide with properties {file:picturePath}
				
				-- Position the picture appropriately
				set width of pictureShape to 280
				set height of pictureShape to 200
				
				-- Position in bottom right
				set top of pictureShape to 300
				set left of pictureShape to 400
			end try
			
			-- Add notes with design elements and pitch notes
			set notesText to "DESIGN ELEMENTS:" & return & return & designElements & return & return & "PITCH NOTES:" & return & return & pitchNotes
			set notes text of newSlide to notesText
		end repeat
		
		-- Add a cover slide at the beginning
		set coverSlide to make new slide at beginning of slides of newPresentation with properties {layout:title slide}
		set title of coverSlide to "NoLock Social"
		set subtitle of coverSlide to deckTitle & return & "Generated on " & (current date) as string
		
		-- Save the presentation
		save newPresentation in outputPath
		
		-- Close the presentation
		close newPresentation saving yes
	end tell
end createPresentation

-- Determine appropriate slide layout based on content
on determineLayoutType(contentText)
	if contentText contains "•" or contentText contains "-" then
		return title and content
	else
		return title and text
	end if
end determineLayoutType

-- Check if content has bullet points
on contentHasBullets(contentText)
	if contentText contains "•" or contentText contains "-" then
		return true
	else
		return false
	end if
end contentHasBullets

-- Extract bullet points from content text
on extractBulletPoints(contentText)
	set AppleScript's text item delimiters to return
	set lines to text items of contentText
	set bulletPoints to {}
	
	repeat with i from 1 to (count of lines)
		set currentLine to item i of lines
		if currentLine is not "" then
			set end of bulletPoints to currentLine
		end if
	end repeat
	
	return bulletPoints
end extractBulletPoints

-- Helper function to format slide numbers with leading zeros
on formatSlideNumber(num)
	if num < 10 then
		return "0" & num as string
	else
		return num as string
	end if
end formatSlideNumber

-- Helper function to read a file
on readFile(filePath)
	set fileRef to POSIX file filePath
	
	try
		set theFile to open for access fileRef
		set fileContents to read theFile
		close access theFile
		return fileContents
	on error errMsg
		try
			close access theFile
		end try
		return "Error reading file: " & errMsg
	end try
end readFile

-- Helper function to extract the title from markdown content
on extractTitle(markdownContent)
	set AppleScript's text item delimiters to return
	set lines to text items of markdownContent
	
	repeat with i from 1 to (count of lines)
		set currentLine to item i of lines
		if currentLine starts with "# Slide" then
			set titleParts to my splitString(currentLine, ":")
			if (count of titleParts) ≥ 2 then
				set titleText to item 2 of titleParts
				if titleText contains "(" then
					set titleText to text 1 thru ((offset of "(" in titleText) - 1) of titleText
				end if
				return my trimString(titleText)
			else
				return "Slide " & i
			end if
		end if
	end repeat
	
	return "NoLock Social"
end extractTitle

-- Helper function to extract the content from markdown content
on extractContent(markdownContent)
	set AppleScript's text item delimiters to return
	set lines to text items of markdownContent
	set contentText to ""
	set inContentBlock to false
	
	repeat with i from 1 to (count of lines)
		set currentLine to item i of lines
		
		if currentLine is "```" then
			if inContentBlock then
				set inContentBlock to false
			else
				set inContentBlock to true
			end if
		else if inContentBlock and currentLine is not "" then
			if contentText is not "" then set contentText to contentText & return
			set contentText to contentText & currentLine
		end if
	end repeat
	
	return contentText
end extractContent

-- Helper function to extract design elements from markdown content
on extractDesignElements(markdownContent)
	set AppleScript's text item delimiters to return
	set lines to text items of markdownContent
	set designText to ""
	set inDesignSection to false
	
	repeat with i from 1 to (count of lines)
		set currentLine to item i of lines
		
		if currentLine is "## Design Elements" then
			set inDesignSection to true
		else if inDesignSection and currentLine starts with "## " then
			set inDesignSection to false
		else if inDesignSection and currentLine is not "" and currentLine is not "## Design Elements" then
			if designText is not "" then set designText to designText & return
			set designText to designText & currentLine
		end if
	end repeat
	
	return designText
end extractDesignElements

-- Helper function to extract pitch notes from markdown content
on extractPitchNotes(markdownContent)
	set AppleScript's text item delimiters to return
	set lines to text items of markdownContent
	set pitchText to ""
	set inPitchSection to false
	
	repeat with i from 1 to (count of lines)
		set currentLine to item i of lines
		
		if currentLine is "## Pitch Notes" then
			set inPitchSection to true
		else if inPitchSection and currentLine starts with "## " then
			set inPitchSection to false
		else if inPitchSection and currentLine starts with "<!--" then
			set inPitchSection to false
		else if inPitchSection and currentLine is not "" and currentLine is not "## Pitch Notes" then
			if pitchText is not "" then set pitchText to pitchText & return
			set pitchText to pitchText & currentLine
		end if
	end repeat
	
	return pitchText
end extractPitchNotes

-- Helper function to split a string by delimiter
on splitString(theString, theDelimiter)
	set oldDelimiters to AppleScript's text item delimiters
	set AppleScript's text item delimiters to theDelimiter
	set theArray to every text item of theString
	set AppleScript's text item delimiters to oldDelimiters
	return theArray
end splitString

-- Helper function to trim whitespace from a string
on trimString(theString)
	set trimmedString to theString
	
	-- Remove leading whitespace
	repeat while trimmedString begins with " " or trimmedString begins with tab
		set trimmedString to text 2 thru -1 of trimmedString
	end repeat
	
	-- Remove trailing whitespace
	repeat while trimmedString ends with " " or trimmedString ends with tab
		set trimmedString to text 1 thru -2 of trimmedString
	end repeat
	
	return trimmedString
end trimString