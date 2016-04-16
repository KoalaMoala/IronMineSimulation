
#"Unloading Dock"
#position, temps de cycle (heure)
_ud = [{"x": 100, "y": 100}, 1]
#"Mixer"
_mx =[{"x": 350, "y": 150},2]
#"Mine"
_mi =[{"x": 100, "y": 400},1]
#"Ore Processing"
_op =[{"x": 350, "y": 350},2]
#"Loading Dock"
_ld =[{"x": 600, "y": 350},1]

#"Tank"
#Nom Produit, Capacity max, Quantity, Unit
_eta = ["Chemical mix", 300000, 0, 'L']
#"Pit 1"
_ep1 = ["Ore", 60, 0, 'T']
#"Pit 2"
_ep2 = ["Iron", 2100, 0, 'T']
#"Transit"
_etr = ["Chemical", 300000, 0, 'L']

#fps
_fps= 1/10
#vitesse 1/24 mean 1 day per second
_speed = 0 #1/24

#Mine distribution triangulaire
#min, mode, max
_mdt = [10,20,60]