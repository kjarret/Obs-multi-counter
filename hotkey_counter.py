import obspython as S

__version__ = "1.1.0"

class TextContent:
    def __init__(self, source_name=None, text_string="This is default text"):
        self.source_name = source_name
        self.text_string = text_string
        self.counter = 0

    def update_text(self, counter_text, counter_value=0):
        source = S.obs_get_source_by_name(self.source_name)
        settings = S.obs_data_create()
        if counter_value == 1:
            self.counter += 1
        if counter_value == -1:
            self.counter -= 1
        if counter_value == 0:
            self.counter = 0
        if isinstance(counter_value, str):
            self.counter = int(counter_value)

        self.text_string = f"{counter_text}{self.counter}"

        S.obs_data_set_string(settings, "text", self.text_string)
        S.obs_source_update(source, settings)
        S.obs_data_release(settings)
        S.obs_source_release(source)


class Driver(TextContent):
    def increment(self):
        self.update_text(self.counter_text, 1)

    def decrement(self):
        self.update_text(self.counter_text, -1)

    def reset(self):
        self.update_text(self.counter_text, 0)

    def do_custom(self, val):
        self.update_text(self.counter_text, str(val))


class Hotkey:
    def __init__(self, callback, obs_settings, _id):
        self.obs_data = obs_settings
        self.hotkey_id = S.OBS_INVALID_HOTKEY_ID
        self.hotkey_saved_key = None
        self.callback = callback
        self._id = _id

        self.load_hotkey()
        self.register_hotkey()
        self.save_hotkey()

    def register_hotkey(self):
        description = "Htk " + str(self._id)
        self.hotkey_id = S.obs_hotkey_register_frontend(
            "htk_id" + str(self._id), description, self.callback
        )
        S.obs_hotkey_load(self.hotkey_id, self.hotkey_saved_key)

    def load_hotkey(self):
        self.hotkey_saved_key = S.obs_data_get_array(
            self.obs_data, "htk_id" + str(self._id)
        )
        S.obs_data_array_release(self.hotkey_saved_key)

    def save_hotkey(self):
        self.hotkey_saved_key = S.obs_hotkey_save(self.hotkey_id)
        S.obs_data_set_array(
            self.obs_data, "htk_id" + str(self._id), self.hotkey_saved_key
        )
        S.obs_data_array_release(self.hotkey_saved_key)


class HotkeyDataHolder:
    def __init__(self):
        self.htk_copy = None  # this attribute will hold instance of Hotkey


hotkeys_counter_1 = Driver()
hotkeys_counter_2 = Driver()
hotkeys_counter_3 = Driver()
hotkeys_counter_4 = Driver()
hotkeys_counter_5 = Driver()

h01 = HotkeyDataHolder()
h02 = HotkeyDataHolder()
h03 = HotkeyDataHolder()
h04 = HotkeyDataHolder()
h05 = HotkeyDataHolder()
h06 = HotkeyDataHolder()
h07 = HotkeyDataHolder()
h08 = HotkeyDataHolder()
h09 = HotkeyDataHolder()
h10 = HotkeyDataHolder()
h11 = HotkeyDataHolder()
h12 = HotkeyDataHolder()
h13 = HotkeyDataHolder()
h14 = HotkeyDataHolder()
h15 = HotkeyDataHolder()
h16 = HotkeyDataHolder()

def callback_up1(pressed):
    if pressed:
        return hotkeys_counter_1.increment()


def callback_down1(pressed):
    if pressed:
        return hotkeys_counter_1.decrement()


def callback_custom1(*args):
    hotkeys_counter_1.do_custom(S.obs_data_get_int(args[2], "counter_1"))
    return True


def callback_reset1(pressed):
    if pressed:
        return hotkeys_counter_1.reset()


def callback_up2(pressed):
    if pressed:
        return hotkeys_counter_2.increment()


def callback_down2(pressed):
    if pressed:
        return hotkeys_counter_2.decrement()


def callback_reset2(pressed):
    if pressed:
        return hotkeys_counter_2.reset()


def callback_custom2(*args):
    hotkeys_counter_2.do_custom(S.obs_data_get_int(args[2], "counter_2"))
    return True


def callback_up3(pressed):
    if pressed:
        return hotkeys_counter_3.increment()


def callback_down3(pressed):
    if pressed:
        return hotkeys_counter_3.decrement()


def callback_reset3(pressed):
    if pressed:
        return hotkeys_counter_3.reset()


def callback_custom3(*args):
    hotkeys_counter_3.do_custom(S.obs_data_get_int(args[2], "counter_3"))
    return True


def callback_up4(pressed):
    if pressed:
        return hotkeys_counter_4.increment()


def callback_down4(pressed):
    if pressed:
        return hotkeys_counter_4.decrement()


def callback_reset4(pressed):
    if pressed:
        return hotkeys_counter_4.reset()


def callback_custom4(*args):
    hotkeys_counter_4.do_custom(S.obs_data_get_int(args[2], "counter_4"))
    return True


def callback_up5(pressed):
    if pressed:
        return hotkeys_counter_5.increment()


def callback_down5(pressed):
    if pressed:
        return hotkeys_counter_5.decrement()


def callback_reset5(pressed):
    if pressed:
        return hotkeys_counter_5.reset()


def callback_custom5(*args):
    hotkeys_counter_5.do_custom(S.obs_data_get_int(args[2], "counter_5"))
    return True


def script_description():
    return "COUNTER 2"


def script_update(settings):
    hotkeys_counter_1.source_name = S.obs_data_get_string(settings, "source1")
    hotkeys_counter_1.counter_text = S.obs_data_get_string(settings, "counter_text1")

    hotkeys_counter_2.source_name = S.obs_data_get_string(settings, "source2")
    hotkeys_counter_2.counter_text = S.obs_data_get_string(settings, "counter_text2")

    hotkeys_counter_3.source_name = S.obs_data_get_string(settings, "source3")
    hotkeys_counter_3.counter_text = S.obs_data_get_string(settings, "counter_text3")

    hotkeys_counter_4.source_name = S.obs_data_get_string(settings, "source4")
    hotkeys_counter_4.counter_text = S.obs_data_get_string(settings, "counter_text4")

    hotkeys_counter_5.source_name = S.obs_data_get_string(settings, "source5")
    hotkeys_counter_5.counter_text = S.obs_data_get_string(settings, "counter_text5")


def script_properties():
    props = S.obs_properties_create()

    for i in range(1, 6):
        counter_text_prop = S.obs_properties_add_text(
            props, f"counter_text{i}", f"[{i}] Set counter text", S.OBS_TEXT_DEFAULT
        )
        counter_value_prop = S.obs_properties_add_int(
            props, f"counter_{i}", "Set custom value", -999999, 999999, 1
        )
        S.obs_property_set_modified_callback(
            counter_value_prop, globals()[f'callback_custom{i}']
        )
        source_prop = S.obs_properties_add_list(
            props,
            f"source{i}",
            f"[{i}] Text Source",
            S.OBS_COMBO_TYPE_EDITABLE,
            S.OBS_COMBO_FORMAT_STRING,
        )

    sources = S.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = S.obs_source_get_unversioned_id(source)
            if source_id == "text_gdiplus" or source_id == "text_ft2_source":
                name = S.obs_source_get_name(source)
                for i in range(1, 6):
                    prop = S.obs_properties_get(props, f"source{i}")
                    S.obs_property_list_add_string(prop, name, name)

        S.source_list_release(sources)

    return props



def script_load(settings):
    hotkeys_counter_1.counter = S.obs_data_get_int(settings, "counter1")
    hotkeys_counter_2.counter = S.obs_data_get_int(settings, "counter2")
    hotkeys_counter_3.counter = S.obs_data_get_int(settings, "counter3")
    hotkeys_counter_4.counter = S.obs_data_get_int(settings, "counter4")
    hotkeys_counter_5.counter = S.obs_data_get_int(settings, "counter5")

    h01.htk_copy = Hotkey(callback_up1, settings, "count_up1")
    h02.htk_copy = Hotkey(callback_down1, settings, "count_down1")
    h03.htk_copy = Hotkey(callback_reset1, settings, "reset1")

    h11.htk_copy = Hotkey(callback_up2, settings, "count_up2")
    h12.htk_copy = Hotkey(callback_down2, settings, "count_down2")
    h13.htk_copy = Hotkey(callback_reset2, settings, "reset2")

    h04.htk_copy = Hotkey(callback_up3, settings, "count_up3")
    h05.htk_copy = Hotkey(callback_down3, settings, "count_down3")
    h06.htk_copy = Hotkey(callback_reset3, settings, "reset3")

    h14.htk_copy = Hotkey(callback_up4, settings, "count_up4")
    h15.htk_copy = Hotkey(callback_down4, settings, "count_down4")
    h16.htk_copy = Hotkey(callback_reset4, settings, "reset4")

    h07.htk_copy = Hotkey(callback_up5, settings, "count_up5")
    h08.htk_copy = Hotkey(callback_down5, settings, "count_down5")
    h09.htk_copy = Hotkey(callback_reset5, settings, "reset5")


def script_save(settings):
    S.obs_data_set_int(settings, "counter1", hotkeys_counter_1.counter)
    S.obs_data_set_int(settings, "counter2", hotkeys_counter_2.counter)
    S.obs_data_set_int(settings, "counter3", hotkeys_counter_3.counter)
    S.obs_data_set_int(settings, "counter4", hotkeys_counter_4.counter)
    S.obs_data_set_int(settings, "counter5", hotkeys_counter_5.counter)
    for h in [h01, h02, h03, h04, h05, h06, h07, h08, h09, h10, h11, h12, h13, h14, h15, h16]:
        if h.htk_copy:
            h.htk_copy.save_hotkey()


description = """
<h2>Version : {__version__}</h2>
<a href="https://github.com/upgradeQ/Obscounter"> Webpage </a>
<h3 style="color:orange">Authors</h3>
<a href="https://github.com/upgradeQ"> upgradeQ </a> <br>
""".format(
    **locals()
)


def script_description():
    print(description, "Released under MIT license")
    return description
