extends CharacterBody2D
class_name player

var tile_size: int = 16
var inputs = {"right": Vector2.RIGHT,
			"left": Vector2.LEFT,
			"up": Vector2.UP,
			"down": Vector2.DOWN}
@onready var ray: RayCast2D = $ray
var anim_speed: float = 1.5
@onready var sprite: AnimatedSprite2D = $Sprite
@export var score: int = 0

var dir_store
var poweredUp: bool = false
var lives: int = 3:
	set(val):
		lives = clamp(val, 0, 3)

func _ready() -> void:
	resetPos()

func _physics_process(_delta: float) -> void:
	if dir_store == null:
		return
	
	if inputs[dir_store] == Vector2.RIGHT:
		sprite.rotation = deg_to_rad(0)
	elif inputs[dir_store] == Vector2.LEFT:
		sprite.rotation = deg_to_rad(180)
	elif inputs[dir_store] == Vector2.UP:
		sprite.rotation = deg_to_rad(270)
	elif inputs[dir_store] == Vector2.DOWN:
		sprite.rotation = deg_to_rad(90)
	
	
	if !ray.is_colliding():
		move(dir_store)
	else:
		velocity = Vector2.ZERO
		dir_store = null
	move_and_slide()


func _unhandled_input(event: InputEvent) -> void:
	for dir in inputs.keys():
		if event.is_action_pressed(dir):
			move(dir)
			dir_store = dir

func move(dir):
	ray.target_position = inputs[dir] * 8
	ray.force_raycast_update()
	velocity = inputs[dir] * tile_size * anim_speed

func _on_collection_area_entered(area: Area2D) -> void:
	if area.is_in_group("Point"):
		area.queue_free()
		score += 10

func die() -> void:
	## play death anim
	## await death anim finished
	if lives != 0:
		lives -= 1
		resetPos()
	else:
		get_tree().change_scene_to_file("res://Scenes/main_menu.tscn")

func resetPos():
	position = Vector2(111, 141)
	position = position.snapped(Vector2.ONE * tile_size)
	position += Vector2.ONE * tile_size/2

func _on_collection_body_entered(body: Node2D) -> void:
	if poweredUp or !body.is_in_group("Enemy"):
		return
	die()
	if lives != 0:
		get_parent().death()
