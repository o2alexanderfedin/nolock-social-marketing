-- AppleScript to update PowerPoint presentation with text extracted from the slides export directory
-- This script provides more comprehensive content updates by using the exported slide content

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
			updateSlideWithExportedContent(i, activePresentation)
		end repeat
		
		-- Save the presentation
		save activePresentation
		
		-- Provide user feedback
		display dialog "PowerPoint presentation has been updated successfully!" buttons {"OK"} default button "OK"
		
	end tell
end run

on updateSlideWithExportedContent(slideNum, presentation)
	-- Function to update a specific slide using content from slides_export directory
	set slideNumString to text -2 thru -1 of ("0" & slideNum)
	set exportPath to "/Users/alexanderfedin/Projects/nolock.social/marketing/slides_export/slide" & slideNumString & "_export.md"
	
	-- Check if export file exists
	tell application "System Events"
		if exists file exportPath then
			log "Updating slide " & slideNum & " with content from " & exportPath
			
			-- Extract content sections from export file
			set exportContent to do shell script "cat " & quoted form of exportPath
			
			-- Extract different sections using shell commands
			set titleText to do shell script "grep -A 1 '## Title' " & quoted form of exportPath & " | tail -n 1"
			set subtitleText to do shell script "grep -A 1 '## Subtitle' " & quoted form of exportPath & " | tail -n 1"
			set summaryText to do shell script "grep -A 1 '## Summary' " & quoted form of exportPath & " | tail -n 1"
			
			-- Extract bullet points (if they exist)
			set bulletPointsExist to do shell script "grep -c '## Bullet Points' " & quoted form of exportPath
			set bulletPoints to ""
			if bulletPointsExist is not "0" then
				set bulletPoints to do shell script "awk '/## Bullet Points/{flag=1;next}/##/{if(flag==1)flag=0}flag' " & quoted form of exportPath
			end if
			
			log "Title: " & titleText
			log "Subtitle: " & subtitleText
			log "Summary: " & summaryText
			log "Has bullet points: " & (bulletPointsExist is not "0")
			
			-- Update the slide
			tell application "Microsoft PowerPoint"
				tell presentation
					tell slide slideNum
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
							log "Error updating title on slide " & slideNum & ": " & errMsg
						end try
						
						-- Update subtitle if it exists
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
						
						-- Update summary/content if a shape 3 exists
						try
							tell shape 3
								if has text frame then
									tell text frame
										tell text range
											if bulletPoints is not "" then
												set content to bulletPoints
											else
												set content to summaryText
											end if
										end tell
									end tell
								end if
							end tell
						on error errMsg
							log "Error updating content on slide " & slideNum & ": " & errMsg
						end try
					end tell
				end tell
			end tell
		else
			log "Export file not found for slide " & slideNum & ": " & exportPath
		end if
	end tell
end updateSlideWithExportedContent