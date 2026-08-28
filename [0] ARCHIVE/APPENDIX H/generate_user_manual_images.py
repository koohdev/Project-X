import os
import math
from PIL import Image, ImageDraw, ImageFont

def generate_all_figures():
    workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(workspace_dir, 'APPENDIX H', 'images')
    new_app_img_dir = os.path.join(workspace_dir, 'NEW APPENDIX', 'images')
    appendix_d_dir = os.path.join(workspace_dir, 'APPENDIX D')
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(new_app_img_dir, exist_ok=True)
    
    font_path_reg = r'C:\Windows\Fonts\times.ttf'
    RED_COLOR = (192, 0, 0)
    
    def wrap_text(text, font, max_width):
        words = text.split(' ')
        lines = []
        cur_line = []
        for w in words:
            test_line = ' '.join(cur_line + [w])
            bbox = font.getbbox(test_line)
            if (bbox[2] - bbox[0]) <= max_width:
                cur_line.append(w)
            else:
                if cur_line:
                    lines.append(' '.join(cur_line))
                    cur_line = [w]
                else:
                    lines.append(w)
                    cur_line = []
        if cur_line:
            lines.append(' '.join(cur_line))
        return lines

    def render_figure(
        src_filename,
        out_filename,
        callouts,
        side_margin=120,
        top_margin=25,
        box_height=65,
        box_gap_y=18,
        box_gap_x=30,
        bottom_padding=30,
        font_size=20
    ):
        src_path = os.path.join(appendix_d_dir, src_filename)
        raw_img = Image.open(src_path).convert('RGBA')
        orig_w, orig_h = raw_img.size
        
        # Scaling font and spacing for high-res images like the 2796x1290 mobile image
        if orig_w > 2000:
            scale_factor = orig_w / 1280.0
            side_margin = int(side_margin * scale_factor)
            top_margin = int(top_margin * scale_factor)
            box_height = int(box_height * scale_factor)
            box_gap_y = int(box_gap_y * scale_factor)
            box_gap_x = int(box_gap_x * scale_factor)
            bottom_padding = int(bottom_padding * scale_factor)
            font_size = int(font_size * scale_factor)
            line_width = int(2.5 * scale_factor)
            arrow_len = int(14 * scale_factor)
        elif orig_h < 100: # for small crop like 2-2 options
            side_margin = 40
            top_margin = 15
            box_height = 55
            bottom_padding = 20
            font_size = 16
            line_width = 2
            arrow_len = 10
        else:
            line_width = 2
            arrow_len = 12
            
        font_callout = ImageFont.truetype(font_path_reg, font_size)
        
        max_row = max(c['grid_pos'][0] for c in callouts) + 1
        total_bottom_h = max_row * box_height + (max_row - 1) * box_gap_y + bottom_padding * 2
        
        canvas_w = orig_w + 2 * side_margin
        canvas_h = orig_h + top_margin + total_bottom_h
        
        canvas = Image.new('RGB', (canvas_w, canvas_h), (255, 255, 255))
        draw = ImageDraw.Draw(canvas)
        
        img_x = side_margin
        img_y = top_margin
        canvas.paste(raw_img, (img_x, img_y), raw_img if raw_img.mode == 'RGBA' else None)
        
        # Outer border around image
        draw.rectangle([img_x - 1, img_y - 1, img_x + orig_w + 1, img_y + orig_h + 1], outline=(190, 190, 190), width=1)
        
        base_box_y = img_y + orig_h + int(20 * (orig_w / 1280.0 if orig_w > 2000 else 1.0))
        available_w = orig_w
        
        for c in callouts:
            row, col = c['grid_pos']
            ncols = c.get('total_cols', 2)
            col_w = (available_w - (ncols - 1) * box_gap_x) // ncols
            bx = img_x + col * (col_w + box_gap_x)
            by = base_box_y + row * (box_height + box_gap_y)
            bw = col_w
            bh = box_height
            
            # Draw box
            draw.rectangle([bx, by, bx + bw, by + bh], fill=(255, 255, 255), outline=RED_COLOR, width=line_width)
            
            # Draw text
            lines = wrap_text(c['text'], font_callout, bw - int(20 * (orig_w / 1280.0 if orig_w > 2000 else 1.0)))
            line_height = int(font_size * 1.25)
            total_text_h = len(lines) * line_height
            ty_start = by + (bh - total_text_h) // 2
            for i, line in enumerate(lines):
                bbox = font_callout.getbbox(line)
                lw = bbox[2] - bbox[0]
                lx = bx + (bw - lw) // 2
                draw.text((lx, ty_start + i * line_height), line, fill=(0, 0, 0), font=font_callout)
                
            # Arrow routing
            tx_img, ty_img = c['target_px']
            abs_tx = img_x + tx_img
            abs_ty = img_y + ty_img
            
            route = c.get('route', 'left_gutter')
            gutter_offset = int(c.get('gutter_offset', 35) * (orig_w / 1280.0 if orig_w > 2000 else 1.0))
            
            if route == 'left_gutter':
                start_pt = (bx, by + bh // 2)
                gutter_x = img_x - gutter_offset
                points = [
                    start_pt,
                    (gutter_x, by + bh // 2),
                    (gutter_x, abs_ty),
                    (abs_tx, abs_ty)
                ]
                arrow_angle = 0 # pointing right ->
            elif route == 'right_gutter':
                start_pt = (bx + bw, by + bh // 2)
                gutter_x = img_x + orig_w + gutter_offset
                points = [
                    start_pt,
                    (gutter_x, by + bh // 2),
                    (gutter_x, abs_ty),
                    (abs_tx, abs_ty)
                ]
                arrow_angle = math.pi # pointing left <-
            elif route == 'direct_up':
                start_pt = (bx + bw // 2, by)
                points = [
                    start_pt,
                    (bx + bw // 2, abs_ty + 15),
                    (abs_tx, abs_ty + 15),
                    (abs_tx, abs_ty)
                ]
                arrow_angle = -math.pi/2 # pointing up ^
                
            draw.line(points, fill=RED_COLOR, width=line_width)
            
            # Arrowhead
            a1 = (abs_tx - arrow_len * math.cos(arrow_angle - math.pi/6),
                  abs_ty - arrow_len * math.sin(arrow_angle - math.pi/6))
            a2 = (abs_tx - arrow_len * math.cos(arrow_angle + math.pi/6),
                  abs_ty - arrow_len * math.sin(arrow_angle + math.pi/6))
            draw.polygon([(abs_tx, abs_ty), a1, a2], fill=RED_COLOR)
            
        full_out_path = os.path.join(output_dir, out_filename)
        canvas.save(full_out_path, 'PNG', quality=95)
        
        new_app_out = os.path.join(new_app_img_dir, out_filename)
        canvas.save(new_app_out, 'PNG', quality=95)
        print(f"Generated: {out_filename}")

    # CALIBRATED CONFIGURATIONS FOR ALL 21 SCREENS

    # 1. Title Screen
    render_figure(
        '1 Title Screen.PNG',
        'Fig-H1-Title-Screen.png',
        [
            {'text': 'Click New Game to start a new campaign', 'target_px': (535, 425), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Click Continue to load saved progress', 'target_px': (745, 475), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Click Options to adjust sound & gameplay', 'target_px': (535, 525), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Click Exit to close the game application', 'target_px': (745, 575), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 2. Options Page 1
    render_figure(
        '2 - 1 Options.PNG',
        'Fig-H2-Options-General.png',
        [
            {'text': 'Toggle Always Dash to enable automatic running', 'target_px': (445, 300), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Toggle Touch UI to show controls on mobile devices', 'target_px': (835, 370), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Toggle Show HP Gauge to display health bars in combat', 'target_px': (445, 405), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Adjust BGM, BGS, and ME volume sliders for audio levels', 'target_px': (835, 475), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 3. Options Page 2 (SE Volume)
    render_figure(
        '2 - 2 Options.PNG',
        'Fig-H3-Options-SE.png',
        [
            {'text': 'Adjust SE Volume slider (0%–100%) to configure combat and math sound effects', 'target_px': (200, 25), 'grid_pos': (0, 0), 'total_cols': 1, 'route': 'left_gutter', 'gutter_offset': 20}
        ],
        side_margin=30,
        box_height=55
    )

    # 4. Load Screen
    render_figure(
        '3 Continue or Load Screen.PNG',
        'Fig-H4-Load-Game.png',
        [
            {'text': 'Select Autosave slot to restore automated checkpoint', 'target_px': (230, 200), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Preview party members and recorded playtime before loading', 'target_px': (1035, 310), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Select manual save slot (File 1–20) to load game progress', 'target_px': (230, 310), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Press X or click Cancel to return to Title Screen without loading', 'target_px': (1035, 680), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 5. Name Input Screen
    render_figure(
        '4 Name Input Screen.PNG',
        'Fig-H5-Name-Input.png',
        [
            {'text': 'Displays hero avatar and active protagonist name', 'target_px': (328, 170), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Click Page to toggle uppercase, lowercase, and symbols', 'target_px': (920, 575), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Select letters and numbers from on-screen keyboard grid', 'target_px': (328, 450), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Click OK or press Enter to confirm protagonist name', 'target_px': (920, 575), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 6. Overworld Exploration
    render_figure(
        '5 Game Example.PNG',
        'Fig-H6-Overworld-Exploration.png',
        [
            {'text': 'Use Arrow keys / WASD or tap screen to navigate character', 'target_px': (250, 360), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Tap Menu icon or press Escape / X to open Pause Menu', 'target_px': (1015, 95), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Press Z or Spacebar to examine objects and interact with NPCs', 'target_px': (280, 260), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Explore rooms to discover lore, math quests, and chests', 'target_px': (850, 520), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 7. Pause Menu
    render_figure(
        '6 Pause Menu.PNG',
        'Fig-H7-Pause-Menu.png',
        [
            {'text': 'View party status summary including Level, HP, MP, and TP', 'target_px': (228, 160), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Tap Back button or press X to close menu and resume game', 'target_px': (1115, 105), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Displays current accumulated Gold currency', 'target_px': (770, 620), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Select system command (Item, Skill, Equip, Status, Quests, Save)', 'target_px': (1034, 345), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 8. Items Menu
    render_figure(
        '7 Items Menu.PNG',
        'Fig-H8-Items-Menu.png',
        [
            {'text': 'View item description, healing properties, and combat effects', 'target_px': (236, 70), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Switch category tabs (Field, Combat, Recovery, Weapons, Armor)', 'target_px': (1042, 130), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Select item from inventory list and choose target party member', 'target_px': (236, 320), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Press Z to use item or press X to return to pause menu', 'target_px': (1042, 680), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 9. Skills Menu
    render_figure(
        '8 Character Skills Menu.PNG',
        'Fig-H9-Character-Skills-Menu.png',
        [
            {'text': 'Displays selected skill effect, power rating, and description', 'target_px': (228, 70), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Press Q / W or tap navigation arrows to switch party members', 'target_px': (1035, 70), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Select learned skill and verify required MP or TP cost', 'target_px': (228, 350), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Select skill category to filter between Magic and Special abilities', 'target_px': (1035, 160), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 10. Equipment Menu
    render_figure(
        '9 Character Equipment Menu.PNG',
        'Fig-H10-Equipment-Menu.png',
        [
            {'text': 'Displays equipment lore, stat bonuses, and element affinities', 'target_px': (228, 70), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Select Clear to unequip all items or Shift to unequip one slot', 'target_px': (1034, 130), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Preview real-time stat increases for Attack, Defense, and Agility', 'target_px': (228, 320), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Select gear slot to equip weapons, armor, shields, or accessories', 'target_px': (1034, 320), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 11. Status Menu
    render_figure(
        '10 Character Status Menu.PNG',
        'Fig-H11-Status-Menu.png',
        [
            {'text': 'Displays character name, class, level, EXP, and vital health gauges', 'target_px': (227, 70), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'View equipped gear set and active accessories', 'target_px': (1033, 320), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Displays detailed combat parameters including Attack & Defense', 'target_px': (227, 320), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'View character lore, class traits, passive perks, and affinities', 'target_px': (1033, 580), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 12. Formation Menu
    render_figure(
        '11 - Formation Menu.PNG',
        'Fig-H12-Formation-Menu.png',
        [
            {'text': 'Displays active party roster and combat battle order', 'target_px': (228, 160), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Select Formation command to initiate party member repositioning', 'target_px': (1034, 310), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Select first character card to prepare for tactical slot swap', 'target_px': (228, 315), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Select second character card to exchange battle positions', 'target_px': (830, 475), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 13. Quests Menu
    render_figure(
        '12 Quests Menu.PNG',
        'Fig-H13-Quests-Menu.png',
        [
            {'text': 'Tracks primary narrative objectives and main campaign missions', 'target_px': (235, 220), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Review active quest instructions and target room locations', 'target_px': (1041, 220), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Tracks active side quests, NPC commissions, and math tasks', 'target_px': (235, 500), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Press X or tap Back to return to the main pause menu', 'target_px': (1041, 680), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 14. Save Menu
    render_figure(
        '13 Save Menu.PNG',
        'Fig-H14-Save-Menu.png',
        [
            {'text': 'Select designated save slot (Autosave or File 1–20) to record state', 'target_px': (221, 200), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Preview saved character sprites, current location, and playtime', 'target_px': (1027, 310), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Press Z or tap slot to save; confirm overwrite dialog if prompted', 'target_px': (221, 310), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Press X or tap Back to cancel save and return to pause menu', 'target_px': (1027, 680), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 15. Pause Menu Exit Dialog
    render_figure(
        '14 Pause Menu Exit.PNG',
        'Fig-H15-Pause-Menu-Exit.png',
        [
            {'text': 'Select To Title to exit session and return to title screen', 'target_px': (512, 335), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Select Cancel to disregard exit request and return to game', 'target_px': (751, 380), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
        ],
        side_margin=120
    )

    # 16. Battle Menu Page 1
    render_figure(
        '15 Battle Menu.PNG',
        'Fig-H16-Battle-Menu-Page1.png',
        [
            {'text': 'Enemy combatants display real-time HP gauges and status icons', 'target_px': (150, 310), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Select Attack to execute basic strike with arithmetic challenge', 'target_px': (1034, 485), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Hero combat card shows active HP, MP, TP, and action gauge', 'target_px': (235, 590), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Select Special, Guard, or Item for tactical combat abilities', 'target_px': (1034, 545), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 17. Battle Menu Page 2
    render_figure(
        '16 Battle Menu 2nd page.PNG',
        'Fig-H17-Battle-Menu-Page2.png',
        [
            {'text': 'Select Fight to return to primary offensive combat commands', 'target_px': (830, 485), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Select Status to inspect active combatant attributes and conditions', 'target_px': (1034, 545), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Select Options to adjust sound and battle preferences mid-combat', 'target_px': (830, 605), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Select Escape to attempt tactical retreat from regular battles', 'target_px': (1034, 665), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 18. Battle Skills
    render_figure(
        '17 Battle Menu Skills.PNG',
        'Fig-H18-Battle-Skills.png',
        [
            {'text': 'Displays selected skill effect, power rating, and debuff details', 'target_px': (228, 70), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Press X or tap Back to return to primary battle command menu', 'target_px': (1034, 70), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Selecting skill pauses combat and triggers curriculum math equation', 'target_px': (228, 250), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Select tactical combat skill and verify required TP expenditure', 'target_px': (1034, 250), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 19. Battle Items
    render_figure(
        '18 Battle Menu Items.PNG',
        'Fig-H19-Battle-Items.png',
        [
            {'text': 'Displays consumable recovery effect and target condition cure', 'target_px': (225, 70), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Press X or tap Back to cancel item selection and return to battle', 'target_px': (1034, 70), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Select restorative item to open ally target selection', 'target_px': (225, 250), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Displays available inventory items and remaining stock quantities', 'target_px': (1034, 250), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 20. Battle Status
    render_figure(
        '19 Battle Menu Status.PNG',
        'Fig-H20-Battle-Status.png',
        [
            {'text': 'Displays real-time condition header (Normal, Poisoned, Blinded)', 'target_px': (228, 70), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 70},
            {'text': 'Tap < or > arrows to inspect status attributes of other party members', 'target_px': (1034, 70), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 70},
            {'text': 'Displays hero portrait, level, class, and vital health gauges', 'target_px': (228, 300), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 35},
            {'text': 'Displays comprehensive combat stats including Attack & Agility', 'target_px': (1034, 300), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 35},
        ],
        side_margin=120
    )

    # 21. Math Battle System & Virtual Keypad
    render_figure(
        'mobile-virtual-keypad-in-combat.jpg',
        'Fig-H21-Math-Combat-Keypad.png',
        [
            {'text': 'Displays curriculum-aligned arithmetic problem prompt', 'target_px': (1045, 425), 'grid_pos': (0, 0), 'route': 'left_gutter', 'gutter_offset': 80},
            {'text': 'Content-Aware Timer bar (pauses during input, tracks answer speed)', 'target_px': (1720, 240), 'grid_pos': (0, 1), 'route': 'right_gutter', 'gutter_offset': 80},
            {'text': 'Tap virtual keypad numbers (0–9) or physical keys to input answer', 'target_px': (1045, 715), 'grid_pos': (1, 0), 'route': 'left_gutter', 'gutter_offset': 40},
            {'text': 'Tap DEL to clear digit; tap OK to submit answer and trigger attack', 'target_px': (1720, 885), 'grid_pos': (1, 1), 'route': 'right_gutter', 'gutter_offset': 40},
        ],
        side_margin=150
    )

    print('All 21 figures regenerated with calibrated coordinates.')

if __name__ == '__main__':
    generate_all_figures()
