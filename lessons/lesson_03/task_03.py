storage_width = 30
storage_length = 40
storage_height = 20
box_width = 5
box_length = 8
box_height = 4

storage_volume = storage_width * storage_length * storage_height
box_volume = box_width * box_length * box_height

box_count = storage_volume // box_volume

print(box_count)