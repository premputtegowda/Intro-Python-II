# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    
    def move(self,direction):
      
        if getattr(self.current_room,f"{direction}_to"):
            self.current_room = getattr(self.current_room,f"{direction}_to")
        else:
            print("You can't move in that direction")
    def on_take(self, take_item):
        # check if the item is in the room?
        # if it's in the room then remove it from room items? 
        # only if you are successfull add it to he player item
        for item in self.current_room.items:
            if item.name == take_item:
                self.current_room.items.remove(item)
                self.items.append(item)
                return f"You have picked up item {take_item}"
        return f"This room doesnt' contain {take_item}"
       
    def on_drop(self,item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                self.current_room.items.append(item)
                return f"You have dropped the item {item_name}"
        return f"This player doesnt' have the item {item_name}"

    
        
       
        