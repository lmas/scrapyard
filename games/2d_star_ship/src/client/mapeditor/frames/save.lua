
loveframes = require('libs.loveframes')


STATE = 'savemap'

local frame = loveframes.Create('frame')
frame:SetState(STATE)
frame:SetName('Save map to file')
frame:SetSize(500,60)
frame:Center()

local input = loveframes.Create('textinput', frame)
input:SetWidth(490)
input:SetPos(5, 30)
input:SetFocus(true)
input.OnEnter = function(obj, text)
    tilemap:save_map(text)
    obj:Clear()
    loveframes.SetState('main')
end


return {
    state = STATE,
    frame = frame,
    input = input,
}
