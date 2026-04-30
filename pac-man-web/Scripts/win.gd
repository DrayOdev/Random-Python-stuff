extends Node2D

func _on_button_pressed() -> void:
	print("a")
	get_tree().change_scene_to_file("res://Scenes/Level0.tscn")
