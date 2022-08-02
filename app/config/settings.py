# game setup
WIDTH    = 1280	
HEIGHT   = 720
FPS      = 60
TILESIZE = 64

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# input actions


# weapons 
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'graphics/weapons/sai/full.png'}
}

# magic
magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':'graphics/particles/flame/fire.png'},
	'lesser-heal' : {'strength': 10,'cost': 5,'graphic':'graphics/particles/heal/heal.png'},
	'heal' : {'strength': 20,'cost': 10,'graphic':'graphics/particles/heal/heal.png'}
}

# enemy
monster_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}

# character data
CHARACTER_DATA = {
  "characters":[
  	{
		  "name": "Ian",
		  "class": "Ranger/Druid",
		  "race": "Fallen Aasimar",
		  "portrait": "Ian_Portrait_125px.png",
		  "asset_path": "ian",
		  "weapons":["Bone Bow","Lance"],
		  "spells":["Lesser Heal"],
		  "stats": {
				'health': 100,
				'energy':60,
				'attack': 10,
				'magic': 4,
				'speed': 5
		  },
		  "descriptions": ""
		},
		{
		  "name": "Bantsi Mordai",
		  "portrait": "Bantsi_Portrait_125px.png",
		  "asset_path": "bantsi",
		  "race": "Tiefling",
		  "class": "Sorcerer",
		  "weapons":["Sai"],
		  "spells":["Firebolt"],
		  "stats": {
				'health': 100,
				'energy':60,
				'attack': 10,
				'magic': 4,
				'speed': 5
		  },
		  "descriptions": ""
		},
		{
		  "name": "Adelheid Granmemere",
		  "race": "Aasimar",
		  "class": "Cleric",
		  "portrait": "Adel_Portrait_125px.png",
		  "asset_path": "adelheid",
		  "weapons":["Axe","Sheild"],
		  "spells": ["Lesser Heal"],
		  "stats": {
				'health': 100,
				'energy':60,
				'attack': 10,
				'magic': 4,
				'speed': 5
		  },
		  "descriptions": ""
		},
		{
		  "name": "Sieg",
		  "race": "Half Orc/Human",
		  "class": "Barbarian",
		  "portrait": "Sieg_Portrait_125px.png",
		  "asset_path": "sieg",
		  "weapons": ["rapier"],
		  "skills": ["Grumpy Choke"],
		  "stats": {
				'health': 100,
				'energy':60,
				'attack': 10,
				'magic': 4,
				'speed': 5
		  },
		  "descriptions": ""
		},
		{
		  "name": "Kilrock Ulgar",
		  "class": "Fighter",
		  "race": "Half Orc/Human",
		  "portrait": "Kilroc_Portrait_125px.png",
		  "asset_path": "kilrock",
		  "weapons": ["Sword"],
		  "skills": ["Sword Flurry"],
		  "stats": {
				'health': 100,
				'energy':60,
				'attack': 10,
				'magic': 4,
				'speed': 5
		  },
		  "descriptions": ""
		},
  ]
}
