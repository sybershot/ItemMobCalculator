from modifiers import ModifierMajor, ModifierMinor


class ItemBase:
    type_name = "item"

    def __init__(self, item_lvl=0, name="Undefined?", modifiers=None, rarity=0, use_speed=0, max_modifier=0):
        self._item_lvl = item_lvl
        self._name = name
        self._rarity = rarity
        self._use_speed = use_speed
        if modifiers is None:
            self._modifiers = []
        else:
            self._modifiers = modifiers
        self._max_modifier = max_modifier

    # region Getters/Setters
    @property
    def item_lvl(self):
        return self._item_lvl

    @item_lvl.setter
    def item_lvl(self, new_item_lvl):
        if type(new_item_lvl) is int:
            self._item_lvl = new_item_lvl
        else:
            raise ValueError("Item lvl is not int.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def rarity(self):
        return self._rarity

    @rarity.setter
    def rarity(self, new_rarity):
        self._rarity = new_rarity

    @property
    def use_speed(self):
        return self._use_speed

    @use_speed.setter
    def use_speed(self, new_use_speed):
        self._use_speed = new_use_speed

    @property
    def max_modifier(self):
        return self._max_modifier

    @max_modifier.setter
    def max_modifier(self, new_max_modifier):
        self._max_modifier = new_max_modifier

    # endregion
    def add_modifier(self, modifier):
        if len(self._modifiers) < self._max_modifier:
            self._modifiers.append(modifier)

    @property
    def full_name(self):
        accumulator = self.name
        for mod in self._modifiers:
            if type(mod) is ModifierMajor:
                accumulator = mod.name + ' ' + accumulator
            if type(mod) is ModifierMinor:
                accumulator = accumulator + ' ' + mod.name
        return accumulator

    def __repr__(self):
        return f"Name: {self.full_name}\n" \
            f" Item lvl: {self.item_lvl}\n" \
            f" Rarity: {self.rarity}\n" \
            f" Modifiers: {self._modifiers}\n"


class ItemWeapon(ItemBase):
    type_name = "weapon"

    def __init__(self, damage=0, damage_type="default", sockets=None, max_socket=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._damage = damage
        self._damage_type = damage_type
        if sockets is None:
            self._sockets = []
        else:
            self._sockets = sockets
        self._max_socket = max_socket

    def inset_to_socket(self, socket):
        if self.available_socket_slots > 0:
            self._sockets.append(socket)

    @property
    def available_socket_slots(self):
        return self._max_socket - len(self._sockets)

    # region Getters/Setters
    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, new_damage):
        self._damage = new_damage

    @property
    def damage_type(self):
        return self._damage_type

    @damage_type.setter
    def damage_type(self, new_damage_type):
        self._damage_type = new_damage_type

    # endregion
    def __repr__(self):
        return super().__repr__() + f"Damage: {self.damage}"


class ItemMelee(ItemWeapon):
    type_name = "melee"

    def __init__(self, use_range=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._use_range = use_range

    @property
    def use_range(self):
        return self._use_range

    @use_range.setter
    def use_range(self, new_use_range):
        self._use_range = new_use_range


class ItemRanged(ItemWeapon):
    type_name = "ranged"

    def __init__(self, use_range=100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._use_range = use_range

    @property
    def use_range(self):
        return self._use_range

    @use_range.setter
    def use_range(self, new_use_range):
        self._use_range = new_use_range
