# 05 Skills and States

This database file lists all combat skills by character class and the various positive and negative status effects (buffs/debuffs) available in the game.

## Combat Skills (By Class)

### Swordsman

| Skill Name      | Description / Effect                                    | Element    |
|-----------------|---------------------------------------------------------|------------|
| Strong Attack   | Delivers a heavy physical strike                        | Physical   |
| Slash           | Executes a basic sword technique                        | Physical   |
| Double Slash    | Hits the enemy twice in succession                      | Physical   |
| Wide Swing      | Deals physical damage to all enemies                    | Physical   |
| Armor Break     | Damages an enemy and lowers their defense               | Debuff   |
| Blade Bash      | Strikes with the flat of the blade with a chance to stun| Physical / Stun|
| Focus           | Increases the critical hit rate                         | Buff     |
| Parry           | Greatly increases evasion                               | Buff     |
| Sonic Wave      | Deals ranged wind damage                                | Wind       |
| Wind Slash      | Performs a wind elemental physical attack               | Wind       |
| Power Break     | Damages an enemy and lowers their attack                | Debuff   |
| Mind Break      | Damages an enemy and lowers their magic attack          | Debuff   |
| Berserk Stance  | Increases attack but lowers defense                     | Buff / Debuff |
| Cross Cut       | Performs two intersecting slashes                       | Physical   |
| Omnislash       | Executes rapid strikes against random targets           | Physical   |

### Sorcerer

| Skill Name      | Description / Effect                                    | Element    |
|-----------------|---------------------------------------------------------|------------|
| Fire            | Deals minor fire magic damage to one enemy              | Fire       |
| Fire II         | Deals moderate fire magic damage                        | Fire       |
| Fire III        | Deals high fire magic damage                            | Fire       |
| Ice             | Deals minor ice magic damage                            | Ice        |
| Ice II          | Deals moderate ice magic damage                         | Ice        |
| Ice III         | Deals high ice magic damage                             | Ice        |
| Thunder         | Deals minor lightning magic damage                      | Thunder    |
| Thunder II      | Deals moderate lightning magic damage                   | Thunder    |
| Thunder III     | Deals high lightning magic damage                       | Thunder    |
| Flare           | Deals massive non-elemental magic damage                | Non-Ele    |
| Freeze          | Deals ice damage with a high chance to stun             | Ice / Stun |
| Shock           | Deals lightning damage with a chance to paralyze        | Thunder/Para|
| Magic Drain     | Absorbs mana from the target                            | Utility    |
| Concentrate     | Drastically multiplies magic attack for the next spell  | Buff       |
| Meteor Swarm    | Deals massive fire and earth damage to all enemies      | Fire/Earth |

### Priest

| Skill Name          | Description / Effect                                    | Element    |
|---------------------|---------------------------------------------------------|------------|
| Heal                | Restores a minor amount of health to an ally            | Light/Heal |
| Heal II             | Restores a moderate amount of health                    | Light/Heal |
| Heal III            | Restores a high amount of health                        | Light/Heal |
| Party Heal          | Restores health to the entire party                     | Light/Heal |
| Cure Poison         | Removes poison from an ally                             | Cleanse    |
| Cure Blind          | Removes blindness from an ally                          | Cleanse    |
| Cure Silence        | Removes silence from an ally                            | Cleanse    |
| Panacea             | Removes all negative status effects from one ally       | Cleanse    |
| Raise               | Revives a knocked-out ally                              | Revival    |
| Holy Light          | Deals light magic damage to undead enemies              | Light      |
| Protect             | Increases an ally's physical defense                    | Buff       |
| Shell               | Increases an ally's magic defense                       | Buff       |
| Regenerate          | Grants continuous health regeneration                   | Buff       |
| Purify              | Damages an enemy and removes their buffs                | Cleanse    |
| Divine Intervention | Fully heals the party and revives all dead allies       | Ultimate   |

### Knight

| Skill Name          | Description / Effect                                    | Element    |
|---------------------|---------------------------------------------------------|------------|
| Provoke             | Forces enemies to target the player                     | Taunt      |
| Shield Bash         | Deals physical damage with a chance to stun             | Phys/Stun  |
| Cover               | Takes damage in place of a low-health ally              | Defense    |
| Guard Ally          | Protects a selected ally from all physical attacks      | Defense    |
| Iron Defense        | Greatly increases defense                               | Buff       |
| Shield Wall         | Increases the entire party's defense                    | Buff       |
| Fortify             | Reduces damage taken by the user while skipping a turn  | Defense    |
| Sentinel            | Counter attacks whenever hit physically                 | Stance     |
| Justice Strike      | Deals damage based on the user's current defense        | Physical   |
| Heavy Charge        | Delivers a high-damage but low-precision strike         | Physical   |
| Taunt               | Lowers enemy attack but forces aggro on the user        | Taunt/Debuff|
| Unbreakable Will    | Grants immunity to status ailments                      | Buff       |
| Phalanx             | Increases physical and magic defense for the user       | Buff       |
| Retribution         | Reflects a portion of physical damage to the attacker   | Stance     |
| Castle of Stone     | Makes the party immune to all damage for a turn         | Ultimate   |

### Martial Artist

| Skill Name          | Description / Effect                                    | Element    |
|---------------------|---------------------------------------------------------|------------|
| Punch               | Deals basic blunt damage                                | Physical   |
| Kick                | Deals basic blunt damage                                | Physical   |
| Triple Kick         | Hits a target multiple times                            | Physical   |
| Roundhouse          | Hits all enemies with physical damage                   | Physical   |
| Chakra              | Restores the user's health and cures basic ailments     | Self-Heal  |
| Meditate            | Restores the user's tactical points                     | Utility    |
| Pressure Point      | Ignores enemy defense                                   | Pierce     |
| Earth Splitter      | Performs an earth elemental physical attack             | Earth      |
| Gale Palm           | Wind strike that pushes the turn order back             | Wind/Delay |
| Spirit Wave         | Deals ranged non-elemental damage                       | Non-Ele    |
| Counter             | High chance to counter-attack physical hits             | Stance     |
| Leg Sweep           | Chance to lower enemy agility                           | Debuff     |
| Fists of Fury       | Rapid punches against one target                        | Physical   |
| Chi Blast           | Uses player's health to deal massive damage             | Sacrificial|
| Seven Star Strike   | Heavy hits with guaranteed criticals                    | Ultimate   |

### Magic Swordsman

| Skill Name          | Description / Effect                                    | Element    |
|---------------------|---------------------------------------------------------|------------|
| Fire Blade          | Adds fire element to physical attack                    | Fire/Phys  |
| Ice Blade           | Adds ice element to physical attack                     | Ice/Phys   |
| Thunder Blade       | Adds lightning element to physical attack               | Thunder    |
| Wind Blade          | Adds wind element to physical attack                    | Wind/Phys  |
| Drain Blade         | Damages an enemy and restores the user's health         | Lifesteal  |
| Aspir Blade         | Damages enemy mana to restore the user's mana           | Manasteal  |
| Magic Barrier       | Grants magic reflection to the user                     | Buff       |
| Enchant Weapon      | Buffs an ally's weapon with fire                        | Buff       |
| Dispel Strike       | Removes enemy buffs on hit                              | Debuff     |
| Elemental Burst     | Consumes all mana to deal damage                        | Magic/Phys |
| Arcane Slash        | Deals magic damage capable of critical hits             | Magic      |
| Spell Shield        | Grants immunity to the next magic spell received        | Buff       |
| Mystic Thrust       | Pierces magical defenses                                | Pierce     |
| Teleport Strike     | Executes a high-evasion attack                          | Evasion    |
| Rune Breaker        | Massive non-elemental magic slash damage                | Ultimate   |

### Hunter

| Skill Name          | Description / Effect                                    | Element    |
|---------------------|---------------------------------------------------------|------------|
| Aim                 | Guarantees the next attack will hit and critically strike| Buff       |
| Power Shot          | Deals high damage after a charge turn                   | Physical   |
| Rapid Fire          | Shoots multiple arrows at random targets                | Physical   |
| Poison Arrow        | Inflicts Poison status on hit                           | Poison     |
| Sleep Arrow         | Inflicts Sleep status on hit                            | Sleep      |
| Blind Arrow         | Inflicts Blind status on hit                            | Blind      |
| Silence Arrow       | Inflicts Silence status on hit                          | Silence    |
| Arrow Rain          | Deals physical damage to all enemies                    | Physical   |
| Eagle Eye           | Increases precision and critical rate                   | Buff       |
| Beast Slayer        | Deals massive damage against animals                    | Specific   |
| Piercing Shot       | Ignores enemy defense                                   | Pierce     |
| Camouflage          | Lowers the user's aggro                                 | Stealth    |
| Trap Set            | Damages enemies who physically attack the user          | Trap       |
| Snipe               | Deals high damage to low-health enemies                 | Execute    |
| Hail of Arrows      | Heavy damage to all enemies and lowers their agility    | Ultimate   |

### Bandit

| Skill Name          | Description / Effect                                    | Element    |
|---------------------|---------------------------------------------------------|------------|
| Steal               | Temporarily reduces enemy stats and buffs the user      | Steal/Buff |
| Mug                 | Deals physical damage and drains enemy statistics       | Steal      |
| Sneak Attack        | Deals high damage if used at the start of battle        | Burst      |
| Poison Edge         | Adds a toxic effect to the dagger                       | Poison     |
| Sand Throw          | Inflicts blindness on one enemy                         | Blind      |
| Smoke Bomb          | High chance to flee battle or blind all enemies         | Escape     |
| Backstab            | High critical chance                                    | Critical   |
| Sprint              | Greatly increases agility                               | Buff       |
| Gold Snatch         | Steals coins from the enemy                             | Thief      |
| Venom Strike        | Deals heavy damage to poisoned targets                  | Execute    |
| Shadow Step         | Drastically increases evasion                           | Evasion    |
| Dirty Trick         | Chance to stun the enemy                                | Stun       |
| Twin Daggers        | Hits twice                                              | Multi-hit  |
| Lucky Strike        | Scales damage based on the luck stat                    | Unique     |
| Assassinate         | High chance to instantly kill non-boss enemies          | Ultimate   |

---

## Status Effects (States)

### Negative States (Debuffs)

| State Name  | Effect / Description                                        |
|-------------|-------------------------------------------------------------|
| Knockout    | Prevents character from acting until revived                |
| Poison      | Causes continuous damage at the end of every turn           |
| Blind       | Greatly reduces physical attack precision                   |
| Silence     | Prevents the usage of all magic skills                      |
| Confusion   | Forces character to attack random targets                   |
| Sleep       | Prevents character from acting until they take damage       |
| Paralysis   | Forces the character to skip their turn entirely            |
| Stun        | Makes character flinch and lose their current turn          |
| Bleed       | Deals physical damage over time and reduces healing received|
| Burn        | Deals fire damage over time and lowers attack power         |
| Freeze      | Prevents action until physical damage shatters the ice      |
| Slow        | Reduces agility; Action Gauge fills much slower             |
| Curse       | Doubles mana costs and prevents health regeneration         |
| Weakness    | Lowers all elemental resistances                            |
| Fear        | Prevents the use of special tactical skills                 |

### Positive States (Buffs)

| State Name     | Effect / Description                                       |
|----------------|------------------------------------------------------------|
| Regenerate     | Restores a portion of health at the end of every turn      |
| Haste          | Doubles agility to fill the action gauge faster            |
| Protect        | Reduces physical damage taken                              |
| Shell          | Reduces magic damage taken                                 |
| Focus          | Increases the critical hit rate                            |
| Magic Barrier  | Nullifies the next magical attack received                 |
| Attack Up      | Increases physical attack power                            |
| Defense Up     | Increases physical defense power                           |
| Magic Up       | Increases magic attack power                               |
| Agility Up     | Increases speed                                            |
| Evasion Up     | Adds a chance to dodge physical attacks                    |
| Immortal       | Prevents health from dropping below 1 point                |
| Auto-Life      | Automatically revives a dead character once                |
| Reflect        | Bounces magic spells back at the caster                    |
| Counter Stance | Guarantees a counter-attack against physical hits          |
