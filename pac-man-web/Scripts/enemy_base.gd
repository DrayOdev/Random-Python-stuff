extends CharacterBody2D
class_name Blinky

@onready var ray: RayCast2D = $ray
@export var movSpeed: float = 12
@onready var nav: NavigationAgent2D = $Nav
@export var threshold: float = 25
@export var allPoints: Array[Marker2D] = []
@export var preferedPoints: Array[Marker2D] = []
@export var PacMan: player
var SeenPac: bool = false
var prefered_chance: float = 45.0
var in_loop: bool = false
var val: int = 0:
	set(max):
		val = clamp(max, 0, 3)

func _ready() -> void:
	_upd_next_loc(allPoints[randi_range(0,67)].global_transform.origin)

func _physics_process(delta: float) -> void:
	var target = -(global_transform.origin - PacMan.global_transform.origin)
	ray.target_position = target
	ray.force_raycast_update()
	$Label.text = str(SeenPac)
	
	var cur_location: Vector2 = global_transform.origin
	var next_location: Vector2 = nav.get_next_path_position()
	var new_vel = (next_location - cur_location).normalized() * movSpeed
	if global_transform.origin.distance_to(nav.target_position) < threshold:
		_on_nav_target_reached()
		
	velocity = new_vel
	move_and_slide()

func _upd_next_loc(target_loc:Vector2) -> Vector2:
	nav.target_position = target_loc
	return nav.get_next_path_position()

func _on_nav_target_reached() -> void:
	if !ray.get_collider():
		_on_player_detect_body_entered(PacMan)
	if SeenPac:
		_upd_next_loc(PacMan.global_transform.origin)
		return
	print("a")
	if in_loop:
		val += 1
		_upd_next_loc(preferedPoints[val].global_transform.origin)
		if val == 3:
			val = 0
			in_loop = false
		return
	if prefered_chance > randi_range(0,100):
		in_loop = true
		_upd_next_loc(preferedPoints[0].global_transform.origin)
	_upd_next_loc(allPoints[randi_range(0,67)].global_transform.origin)

func die():
	## return to spawn transform
	pass

func _on_player_detect_body_entered(body: Node2D) -> void:
	if ray.is_colliding():
		SeenPac = false
	else:
		SeenPac = true
		_upd_next_loc(PacMan.global_transform.origin)
	


func _on_player_detect_body_exited(body: Node2D) -> void:
	SeenPac = false
