-- AppleScript to create PowerPoint presentations for NoLock Social
-- Creates both simplified and detailed presentations

on run
	-- Define paths and filenames
	set marketingDir to "/Users/alexanderfedin/Projects/nolock.social/marketing"
	set basePath to marketingDir & "/pitch-decks/customer-partner"
	set simplifiedDir to basePath & "/slides-simplified"
	set detailedDir to basePath & "/slides"
	set imagesDir to basePath & "/images"
	
	set simplifiedOutput to marketingDir & "/NoLock_Partner_Simplified.pptx"
	set detailedOutput to marketingDir & "/NoLock_Partner_Detailed.pptx"
	
	-- Create simplified presentation
	createPresentation(simplifiedDir, imagesDir, simplifiedOutput, "simplified")
	
	-- Create detailed presentation
	createPresentation(detailedDir, imagesDir, detailedOutput, "detailed")
	
	display dialog "PowerPoint presentations created successfully!" buttons {"OK"} default button "OK"
end run

on createPresentation(slidesDir, imagesDir, outputPath, presentationType)
	tell application "Microsoft PowerPoint"
		-- Create a new presentation
		set newPresentation to make new presentation
		
		-- Delete the default first slide
		if (count of slides of newPresentation) > 0 then
			delete slide 1 of newPresentation
		end if
		
		-- Process all 21 slides
		repeat with slideNum from 1 to 21
			-- Format the slide number with leading zero
			set slideNumStr to my formatSlideNumber(slideNum)
			
			-- Define the slide content markdown file path
			set slideFilePath to slidesDir & "/slide" & slideNumStr & ".md"
			
			-- Read and parse the slide content
			set slideContent to my readFile(slideFilePath)
			
			-- Extract the title, content, design elements, and pitch notes
			set slideTitle to my extractTitle(slideContent)
			set slideText to my extractContent(slideContent)
			set designElements to my extractDesignElements(slideContent)
			set pitchNotes to my extractPitchNotes(slideContent)
			
			-- Get the image file path (try both .png and .jpg extensions)
			set imageNum to slideNum as string
			set imagePath to imagesDir & "/slide" & imageNum & ".png"
			
			-- Create a new slide
			set newSlide to make new slide at end of slides of newPresentation
			
			-- Add the title
			set titleShape to make new shape at newSlide with properties {auto shape type:rectangle shape}
			set text frame of titleShape to make new text frame at titleShape with properties {text:slideTitle}
			tell text frame of titleShape
				set text range start 1 end (count of characters) text font size to 28
				set text range start 1 end (count of characters) text font bold to true
			end tell
			set top of titleShape to 30
			set left of titleShape to 40
			set width of titleShape to 640
			set height of titleShape to 50
			
			-- Add the content
			set contentShape to make new shape at newSlide with properties {auto shape type:rectangle shape}
			set text frame of contentShape to make new text frame at contentShape with properties {text:slideText}
			tell text frame of contentShape
				set text range start 1 end (count of characters) text font size to 24
			end tell
			set top of contentShape to 90
			set left of contentShape to 40
			set width of contentShape to 640
			set height of contentShape to 200
			
			-- Try to add the image if it exists
			try
				set picturePath to POSIX file imagePath
				set pictureShape to make new picture at newSlide with properties {file:picturePath}
				set top of pictureShape to 300
				set left of pictureShape to 200
				set width of pictureShape to 320
				set height of pictureShape to 220
			on error
				-- Image might not exist, just continue
			end try
			
			-- Add notes with design elements and pitch notes
			set notesText to "DESIGN ELEMENTS:" & return & return & designElements & return & return & "PITCH NOTES:" & return & return & pitchNotes
			set notes text of newSlide to notesText
		end repeat
		
		-- Save the presentation
		save newPresentation in outputPath
		
		-- Close the presentation
		close newPresentation saving yes
		
		return true
	end tell
end createPresentation

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
	set theFile to open for access fileRef
	set fileContents to read theFile
	close access theFile
	return fileContents
end readFile

-- Helper function to extract the title from markdown content
on extractTitle(markdownContent)
	set AppleScript's text item delimiters to return
	set lines to text items of markdownContent
	
	-- Look for the title line (starts with # Slide)
	repeat with i from 1 to (count of lines)
		set currentLine to item i of lines
		if currentLine starts with "# Slide" then
			-- Extract the title after the colon
			set titleParts to my splitString(currentLine, ":")
			if (count of titleParts) ≥ 2 then
				set titleText to item 2 of titleParts
				-- Clean up the title (remove trailing parentheses if present)
				if titleText contains "(" then
					set titleText to my trimString(text 1 thru ((offset of "(" in titleText) - 1) of titleText)
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
		
		-- Look for content block, which is between ```
		if currentLine is "```" then
			if inContentBlock then
				set inContentBlock to false
			else
				set inContentBlock to true
			end if
		else if inContentBlock then
			-- Inside content block, add the line to content
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
		
		-- Look for design elements section
		if currentLine is "## Design Elements" then
			set inDesignSection to true
		else if inDesignSection and currentLine starts with "## " then
			-- We've reached the next section
			set inDesignSection to false
		else if inDesignSection and currentLine is not "" and currentLine is not "## Design Elements" then
			-- Inside design elements section, add the line
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
		
		-- Look for pitch notes section
		if currentLine is "## Pitch Notes" then
			set inPitchSection to true
		else if inPitchSection and currentLine starts with "## " then
			-- We've reached the next section
			set inPitchSection to false
		else if inPitchSection and currentLine starts with "<!--" then
			-- We've reached the navigation footer
			set inPitchSection to false
		else if inPitchSection and currentLine is not "" and currentLine is not "## Pitch Notes" then
			-- Inside pitch notes section, add the line
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
	-- Remove leading and trailing whitespace
	set theString to do shell script "echo " & quoted form of theString & " | sed 's/^[ \t]*//;s/[ \t]*$//'"
	return theString
end trimString