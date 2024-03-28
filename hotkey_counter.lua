-- Définir la version du script
__version__ = "1.1.0"

-- Création de la classe TextContent
TextContent = {}
TextContent.__index = TextContent

function TextContent.new(source_name, text_string)
    local self = setmetatable({}, TextContent)
    self.source_name = source_name or nil
    self.text_string = text_string or "This is default text"
    self.counter = 0
    return self
end

function TextContent:update_text(counter_text, counter_value)
    counter_value = counter_value or 0
    local source = obslua.obs_get_source_by_name(self.source_name)
    if source then
        local settings = obslua.obs_data_create()
        self.counter = counter_value == 1 and self.counter + 1 or (counter_value == -1 and self.counter - 1 or (counter_value == 0 and 0 or self.counter))
        if type(counter_value) == "string" then
            self.counter = tonumber(counter_value)
        end
        self.text_string = counter_text .. self.counter
        obslua.obs_data_set_string(settings, "text", self.text_string)
        obslua.obs_source_update(source, settings)
        obslua.obs_data_release(settings)
        obslua.obs_source_release(source)
    end
end

-- Création de la classe Driver qui hérite de TextContent
Driver = setmetatable({}, {__index = TextContent})

function Driver.new(source_name, text_string)
    local self = TextContent.new(source_name, text_string)
    setmetatable(self, {__index = Driver})
    return self
end

function Driver:increment()
    self:update_text(self.counter_text, 1)
end

function Driver:decrement()
    self:update_text(self.counter_text, -1)
end

function Driver:reset()
    self:update_text(self.counter_text, 0)
end

function Driver:do_custom(val)
    self:update_text(self.counter_text, tostring(val))
end

-- Création de la classe Hotkey
Hotkey = {}
Hotkey.__index = Hotkey

function Hotkey.new(callback, _id)
    local self = setmetatable({}, Hotkey)
    self.callback = callback
    self._id = _id
    self:register_hotkey()
    return self
end

function Hotkey:register_hotkey()
    local description = "Htk " .. self._id
    self.hotkey_id = obslua.obs_hotkey_register_frontend("htk_id_" .. self._id, description, self.callback)
end

-- Instanciation des objets Driver
hotkeys_counter_1 = Driver.new()
hotkeys_counter_2 = Driver.new()
hotkeys_counter_3 = Driver.new()
hotkeys_counter_4 = Driver.new()
hotkeys_counter_5 = Driver.new()

-- Fonctions de rappel pour les hotkeys
function callback_up1(pressed)
    if pressed then hotkeys_counter_1:increment() end
end

function callback_down1(pressed)
    if pressed then hotkeys_counter_1:decrement() end
end

function callback_reset1(pressed)
    if pressed then hotkeys_counter_1:reset() end
end



function callback_up2(pressed)
    if pressed then hotkeys_counter_2:increment() end
end

function callback_down2(pressed)
    if pressed then hotkeys_counter_2:decrement() end
end

function callback_reset2(pressed)
    if pressed then hotkeys_counter_2:reset() end
end




function callback_up3(pressed)
    if pressed then hotkeys_counter_3:increment() end
end

function callback_down3(pressed)
    if pressed then hotkeys_counter_3:decrement() end
end

function callback_reset3(pressed)
    if pressed then hotkeys_counter_3:reset() end
end




function callback_up4(pressed)
    if pressed then hotkeys_counter_4:increment() end
end

function callback_down4(pressed)
    if pressed then hotkeys_counter_4:decrement() end
end

function callback_reset4(pressed)
    if pressed then hotkeys_counter_4:reset() end
end




function callback_up5(pressed)
    if pressed then hotkeys_counter_5:increment() end
end

function callback_down5(pressed)
    if pressed then hotkeys_counter_5:decrement() end
end

function callback_reset5(pressed)
    if pressed then hotkeys_counter_5:reset() end
end




-- Fonctions requises par les scripts OBS
function script_description()
    return [[
<h2>Version : ]] .. __version__ .. [[</h2>
<a href="https://github.com/kjarret/Obs-multi-counter">Link Github</a>
<h3 style="color:orange">Authors</h3>
<a href="https://github.com/upgradeQ">upgradeQ</a><br>
<h3 style="color:red">Contributor</h3>
<a href="https://github.com/kjarret">kjarret</a><br>
Released under MIT license
]]
end



function script_update(settings)
    -- Mise à jour des noms de source et des textes de compteur pour chaque instance Driver
    if hotkeys_counter_1 then
        hotkeys_counter_1.source_name = obslua.obs_data_get_string(settings, "source1")
        hotkeys_counter_1.counter_text = obslua.obs_data_get_string(settings, "counter_text1")
    end
    if hotkeys_counter_2 then
        hotkeys_counter_2.source_name = obslua.obs_data_get_string(settings, "source2")
        hotkeys_counter_2.counter_text = obslua.obs_data_get_string(settings, "counter_text2")
    end
    if hotkeys_counter_3 then
        hotkeys_counter_3.source_name = obslua.obs_data_get_string(settings, "source3")
        hotkeys_counter_3.counter_text = obslua.obs_data_get_string(settings, "counter_text3")
    end
    if hotkeys_counter_4 then
        hotkeys_counter_4.source_name = obslua.obs_data_get_string(settings, "source4")
        hotkeys_counter_4.counter_text = obslua.obs_data_get_string(settings, "counter_text4")
    end
    if hotkeys_counter_5 then
        hotkeys_counter_5.source_name = obslua.obs_data_get_string(settings, "source5")
        hotkeys_counter_5.counter_text = obslua.obs_data_get_string(settings, "counter_text5")
    end

end



function script_properties()
    local props = obslua.obs_properties_create()

    for i = 1, 5 do
        local counter_text_key = string.format("counter_text%d", i)
        local counter_value_key = string.format("counter_%d", i)
        local source_key = string.format("source%d", i)

        obslua.obs_properties_add_text(props, counter_text_key, "[" .. i .. "] Set counter text", obslua.OBS_TEXT_DEFAULT)
        local counter_value_prop = obslua.obs_properties_add_int(props, counter_value_key, "Set custom value", -999999, 999999, 1)
        
        local source_prop = obslua.obs_properties_add_list(props, source_key, "[" .. i .. "] Text Source", obslua.OBS_COMBO_TYPE_EDITABLE, obslua.OBS_COMBO_FORMAT_STRING)
    end

    local sources = obslua.obs_enum_sources()
    if sources ~= nil then
        for _, source in ipairs(sources) do
            local source_id = obslua.obs_source_get_unversioned_id(source)
            if source_id == "text_gdiplus" or source_id == "text_ft2_source" then
                local name = obslua.obs_source_get_name(source)
                for i = 1, 5 do
                    local prop = obslua.obs_properties_get(props, string.format("source%d", i))
                    obslua.obs_property_list_add_string(prop, name, name)
                end
            end
        end
        obslua.source_list_release(sources)
    end

    return props
end


function script_save(settings)
    obslua.obs_data_set_int(settings, "counter1", hotkeys_counter_1.counter)
    obslua.obs_data_set_int(settings, "counter2", hotkeys_counter_2.counter)
    obslua.obs_data_set_int(settings, "counter3", hotkeys_counter_3.counter)
    obslua.obs_data_set_int(settings, "counter4", hotkeys_counter_4.counter)
    obslua.obs_data_set_int(settings, "counter5", hotkeys_counter_5.counter)
end

function script_load(settings)
    hotkeys_counter_1.counter = obslua.obs_data_get_int(settings, "counter1")
    hotkeys_counter_2.counter = obslua.obs_data_get_int(settings, "counter2")
    hotkeys_counter_3.counter = obslua.obs_data_get_int(settings, "counter3")
    hotkeys_counter_4.counter = obslua.obs_data_get_int(settings, "counter4")
    hotkeys_counter_5.counter = obslua.obs_data_get_int(settings, "counter5")

    h01 = {}
    h01.htk_copy = Hotkey.new(callback_up1, "count_up1")
    h02 = {}
    h02.htk_copy = Hotkey.new(callback_down1, "count_down1");
    h03 = {}
    h03.htk_copy = Hotkey.new(callback_reset1, "count_reset1");

    h04 = {}
    h04.htk_copy = Hotkey.new(callback_up2, "count_up2")
    h05 = {}
    h05.htk_copy = Hotkey.new(callback_down2, "count_down2");
    h06 = {}
    h06.htk_copy = Hotkey.new(callback_reset2, "count_reset2");


    h07 = {}
    h07.htk_copy = Hotkey.new(callback_up3, "count_up3")
    h08 = {}
    h08.htk_copy = Hotkey.new(callback_down3, "count_down3");
    h09 = {}
    h09.htk_copy = Hotkey.new(callback_reset3, "count_reset3");


    h10 = {}
    h10.htk_copy = Hotkey.new(callback_up4, "count_up4")
    h11 = {}
    h11.htk_copy = Hotkey.new(callback_down4, "count_down4");
    h12 = {}
    h12.htk_copy = Hotkey.new(callback_reset4, "count_reset4");

    h13 = {}
    h13.htk_copy = Hotkey.new(callback_up5, "count_up5")
    h14 = {}
    h14.htk_copy = Hotkey.new(callback_down5, "count_down5");
    h15 = {}
    h15.htk_copy = Hotkey.new(callback_reset5, "count_reset5");


end
