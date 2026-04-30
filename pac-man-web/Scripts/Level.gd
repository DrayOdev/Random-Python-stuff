extends Node2D

var rightside: Vector2 = Vector2(224, 120)
var leftside: Vector2 = Vector2(14, 120)
@onready var win: Node2D = $Win/Win
@onready var points: Node = $Points
@onready var Player: CharacterBody2D = $Player
@onready var inky: Inky = $Ghosts/Inky
@onready var blinky: Blinky = $Ghosts/Blinky
@onready var clyde: Clyde = $Ghosts/Clyde
@onready var pinky: Pinky = $Ghosts/Pinky
var inky_spawn: Vector2 = Vector2(112, 128)
var blinky_spawn: Vector2 = Vector2(104, 128)
var clyde_spawn: Vector2 = Vector2(120, 128)
var pinky_spawn: Vector2 = Vector2(128, 128)
@onready var score: Label = $Control/HBoxContainer/Score
@onready var lives: Label = $Control/HBoxContainer/Lives

func _on_left_to_right_body_entered(body: Node2D) -> void:
	body.position = rightside

func _on_right_to_left_body_entered(body: Node2D) -> void:
	body.position = leftside

func _process(_delta: float) -> void:
	score.text = "Score: " + str(Player.score)
	lives.text = "Lives: " + str(Player.lives)
	if Player.score == 1590:
		get_tree().change_scene_to_file("res://Scenes/main_menu.tscn")

func death():
	inky.global_transform.origin = inky_spawn
	blinky.global_transform.origin = blinky_spawn
	clyde.global_transform.origin = clyde_spawn
	pinky.global_transform.origin = pinky_spawn
	get_tree().paused = true
	Player.visible = false
	await get_tree().create_timer(2).timeout
	Player.visible = true
	get_tree().paused = false
