class ModifierBase:
    def __init__(self, name="Wrong", description="Hm, looks like something went wrong.",
                 effect_tip="This item might have unexpected behaviour.", damage_type="default",
                 effects=None):
        self._name = name
        self._description = description
        self._effect_tip = effect_tip
        self._damage_type = damage_type
        if effects is None:
            raise Exception("Invalid modifier data")
        self._effects = effects

    @property
    def name(self):
        return self._name


class ModifierMajor(ModifierBase):
    def __init__(self, name="Wrong", description="Hm, looks like something went wrong.",
                 effect_tip="This item might have unexpected behaviour.", damage_type="default", effects=None):
        super().__init__(name, description, effect_tip, damage_type, effects)


class ModifierMinor(ModifierBase):
    def __init__(self, name="Wrong", description="Hm, looks like something went wrong.",
                 effect_tip="This item might have unexpected behaviour.", damage_type="default", effects=None):
        super().__init__(name, description, effect_tip, damage_type, effects)
