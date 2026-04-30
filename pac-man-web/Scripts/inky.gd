extends CharacterBody2D
class_name Inky

@export var movSpeed: float = 12
@onready var nav: NavigationAgent2D = $Nav
@export var threshold: float = 25
@export var allPoints: Array[Marker2D] = []
@export var preferedPoints: Array[Marker2D] = []
var prefered_chance: float = 45.0
var in_loop: bool = false
var val: int = 0:
	set(max):
		val = clamp(max, 0, 3)

func _ready() -> void:
	_upd_next_loc(allPoints[randi_range(0,67)].global_transform.origin)

func _physics_process(delta: float) -> void:
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
