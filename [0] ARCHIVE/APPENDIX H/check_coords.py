import os
from PIL import Image, ImageDraw

def test_screen_coords():
    # Complete, measured coordinate table for all 21 screens in APPENDIX D
    coords = {
        '1 Title Screen.PNG': {
            'NewGame': (535, 435),    # Left edge of New Game
            'Continue': (745, 480),   # Right edge of Continue
            'Options': (535, 525),    # Left edge of Options
            'Exit': (745, 570),       # Right edge of Exit
        },
        '2 - 1 Options.PNG': {
            'AlwaysDash': (445, 330), # Left edge of Always Dash
            'TouchUI': (835, 420),    # Right edge of Touch UI
            'ShowHP': (445, 465),     # Left edge of Show HP Gauge
            'BGSVol': (835, 555),     # Right edge of BGS Volume
        },
        '2 - 2 Options.PNG': {
            'SEVol': (200, 25),       # Center of SE Volume bar
        },
        '3 Continue or Load Screen.PNG': {
            'Autosave': (185, 230),   # Left edge of Autosave slot
            'File1': (185, 340),      # Left edge of File 1 slot
            'Playtime': (1080, 340),  # Right edge of Playtime info
            'Cancel': (1080, 680),    # Right edge of Cancel prompt
        },
        '4 Name Input Screen.PNG': {
            'Avatar': (270, 150),     # Left edge of avatar box
            'GridKey': (270, 395),    # Left edge of keyboard grid
            'Page': (740, 595),       # Right edge of Page button
            'OK': (740, 595),         # Right edge of OK button
        },
        '5 Game Example.PNG': {
            'Hero': (630, 350),       # Protagonist sprite
            'Bookshelf': (420, 260),  # Interactive study bookshelf
            'MenuIcon': (1220, 40),   # Top-right touch menu icon
            'Room': (850, 260),       # Exploration area
        },
        '6 Pause Menu.PNG': {
            'AlphaCard': (155, 160),  # Left edge of Alpha summary card
            'ItemBtn': (770, 105),    # Right edge of Item button
            'FormationBtn': (770, 305),# Right edge of Formation button
            'GoldBox': (770, 575),    # Right edge of Gold display
        },
        '7 Items Menu.PNG': {
            'Desc': (185, 50),        # Left edge of item description
            'Categories': (1080, 100),# Right edge of category bar
            'ItemList': (185, 250),   # Left edge of item list
            'Controls': (1080, 680),  # Right edge of controls bar
        },
        '8 Character Skills Menu.PNG': {
            'Desc': (185, 50),        # Left edge of skill description
            'SkillTypes': (1080, 150),# Right edge of skill type selector
            'SkillList': (185, 350),  # Left edge of learned skills list
            'HeroSwitch': (1080, 50), # Right edge of character switch arrows
        },
        '9 Character Equipment Menu.PNG': {
            'Desc': (185, 50),        # Left edge of equipment lore
            'Slots': (1080, 250),     # Right edge of equipment slots
            'StatPreview': (185, 250),# Left edge of stat changes
            'ClearBtn': (1080, 120),  # Right edge of Clear command
        },
        '10 Character Status Menu.PNG': {
            'Profile': (185, 60),     # Left edge of profile header
            'Equip': (1080, 280),     # Right edge of equipped items
            'Stats': (185, 280),      # Left edge of combat parameters
            'Lore': (1080, 560),      # Right edge of class lore box
        },
        '11 - Formation Menu.PNG': {
            'Alpha': (185, 160),      # Left edge of Alpha card
            'Elara': (185, 315),      # Left edge of Elara card
            'FormationBtn': (770, 380),# Right edge of Formation button
            'Thorne': (185, 475),     # Left edge of Thorne card
        },
        '12 Quests Menu.PNG': {
            'MainStory': (185, 200),  # Left edge of main story quest
            'ActiveComm': (185, 480), # Left edge of active commission
            'QuestDesc': (1080, 200), # Right edge of quest details
            'Back': (1080, 680),      # Right edge of back control
        },
        '13 Save Menu.PNG': {
            'Autosave': (185, 190),   # Left edge of autosave slot
            'File1': (185, 290),      # Left edge of manual file 1
            'SlotInfo': (1080, 290),  # Right edge of playtime/sprites
            'Back': (1080, 680),      # Right edge of back control
        },
        '14 Pause Menu Exit.PNG': {
            'ToTitle': (408, 440),    # Left edge of To Title button
            'Cancel': (588, 485),     # Right edge of Cancel button
        },
        '15 Battle Menu.PNG': {
            'Enemy': (120, 300),      # Fairy monster battler
            'AttackBtn': (825, 485),  # Right edge of Attack button
            'HeroCard': (235, 620),   # Left edge of Garrick status card
            'SpecialBtn': (825, 540), # Right edge of Special button
        },
        '16 Battle Menu 2nd page.PNG': {
            'FightBtn': (825, 485),   # Right edge of Fight button
            'StatusBtn': (825, 540),  # Right edge of Status button
            'OptionsBtn': (825, 595), # Right edge of Options button
            'EscapeBtn': (825, 650),  # Right edge of Escape button
        },
        '17 Battle Menu Skills.PNG': {
            'Desc': (185, 50),        # Left edge of skill description
            'SkillList': (185, 250),  # Left edge of skill list
            'TPCost': (680, 250),     # Right edge of TP cost
            'Back': (1080, 50),       # Right edge of back control
        },
        '18 Battle Menu Items.PNG': {
            'Desc': (185, 50),        # Left edge of item description
            'ItemList': (185, 250),   # Left edge of item list
            'ItemQty': (680, 250),    # Right edge of item quantity
            'Back': (1080, 50),       # Right edge of back control
        },
        '19 Battle Menu Status.PNG': {
            'Condition': (185, 50),   # Left edge of condition header
            'HeroSwitch': (1080, 50), # Right edge of character switch arrows
            'HeroStats': (185, 250),  # Left edge of hero profile
            'CombatParams': (1080, 250), # Right edge of combat parameters
        },
        'mobile-virtual-keypad-in-combat.jpg': {
            'Equation': (1045, 425),  # Left edge of equation box
            'Timer': (1720, 240),     # Right edge of timer bar
            'Keypad1': (1045, 715),   # Left edge of numeric keypad
            'OK_DEL': (1720, 885),    # Right edge of DEL / OK buttons
        }
    }
    return coords

if __name__ == '__main__':
    c = test_screen_coords()
    print('Total configured screens:', len(c))
