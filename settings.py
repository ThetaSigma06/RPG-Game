WIDTH=1280
HEIGHT=720
FPS=60
TILE_SIZE=64
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}

BAR_HEIGHT=20
HEALTH_BAR_WIDTH=200
MANA_BAR_WIDTH=140
ITEM_BOX_SIZE=80
UI_FONT='Graphics/font/joystix.ttf'
UI_FONT_SIZE=18

WATER_COLOUR='#71ddee'
UI_BG_COLOUR='#222222'
UI_BORDER_COLOUR='#111111'
TEXT_COLOUR='#EEEEEE'

HEALTH_COLOUR='red'
MANA_COLOUR='blue'
UI_BORDER_COLOUR_ACTIVE='gold'

TEXT_COLOUR_SELECTED = '#111111'
BAR_COLOUR = '#EEEEEE'
BAR_COLOUR_SELECTED = '#111111'
UPGRADE_BG_COLOUR_SELECTED = '#EEEEEE'


weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'Graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'Graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'Graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'Graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'Graphics/weapons/sai/full.png'}}

magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':'Graphics/particles/flame/fire.png'},
	'heal' : {'strength': 20,'cost': 10,'graphic':'Graphics/particles/heal/heal.png'}
}

monster_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'Audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'Audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'Audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'Audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}