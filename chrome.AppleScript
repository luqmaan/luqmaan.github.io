

tell application "System Events"
    tell process "Chrome"
        keystroke "r" using {command down}
    end tell
end tell

-- tell application "Chrome"
--    activate
-- end tell