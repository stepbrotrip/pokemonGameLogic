sectorMapping = {

    "area1" :  [["xi","x","x","G"],
                ["x","x","x","G"],
                ["x","x","x","G"],
                ["x","x","x","G"]]

        }

encounterMapping = {
        "area1" : ["grogle"]
    }

allMonsters = {
        "grogle" : {
            "hp": 50,
            "maxHp" : 50,
            "moves": {
                "15" : ["water spout", "cleaning shot", "waterbed", "surf"],
                "40" : ["bloody water", "taming blade", "floating wave"],
                "100" : ["thunderstorm", "raining shot"]
            }
        }
    }

moves = {
    "water spout" : [35, 95, None],
    "cleaning shot" : [50, 80, None],
    "waterbed" : [0, 100, "sleep"],
    "surf" : [45, 100, None],
    "bloody water" : [75, 95, "bleed"],
    "taming blade" : [50, 100, "sleep"],
    "floating wave" : [95, 100, None],
    "thunderstorm" : [100, 65, None],
    "raining shot" : [50, 100, "multishot"],
    "haunting stare" : [25, 100, None],
    "needle barrage" : [30, 100, "multishot"],
    "scare" : [40, 95, "shiver"],
    "tree bash" : [65, 85, None]

}




