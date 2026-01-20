"""
Command Pattern
---------------
Encapsulates a request as an object, thereby letting you parameterize clients with different requests,
queue or log requests, and support undoable operations.
"""

from abc import ABC, abstractmethod


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass


# Receiver
class Light:
    def __init__(self, location):
        self.location = location
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        return f"{self.location} light is ON"
    
    def turn_off(self):
        self.is_on = False
        return f"{self.location} light is OFF"


# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        return self.light.turn_on()
    
    def undo(self):
        return self.light.turn_off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        return self.light.turn_off()
    
    def undo(self):
        return self.light.turn_on()


# Another Receiver
class Television:
    def __init__(self):
        self.is_on = False
        self.volume = 0
    
    def power_on(self):
        self.is_on = True
        return "TV is ON"
    
    def power_off(self):
        self.is_on = False
        return "TV is OFF"
    
    def volume_up(self):
        if self.is_on:
            self.volume += 1
            return f"TV volume: {self.volume}"
        return "TV is OFF"
    
    def volume_down(self):
        if self.is_on and self.volume > 0:
            self.volume -= 1
            return f"TV volume: {self.volume}"
        return "TV is OFF or volume at minimum"


class TVOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv
    
    def execute(self):
        return self.tv.power_on()
    
    def undo(self):
        return self.tv.power_off()


class TVVolumeUpCommand(Command):
    def __init__(self, tv):
        self.tv = tv
    
    def execute(self):
        return self.tv.volume_up()
    
    def undo(self):
        return self.tv.volume_down()


# Invoker
class RemoteControl:
    def __init__(self):
        self.commands = {}
        self.history = []
    
    def set_command(self, slot, command):
        self.commands[slot] = command
    
    def press_button(self, slot):
        if slot in self.commands:
            result = self.commands[slot].execute()
            self.history.append(self.commands[slot])
            return result
        return "No command assigned to this slot"
    
    def press_undo(self):
        if self.history:
            command = self.history.pop()
            return command.undo()
        return "Nothing to undo"


# Macro Command
class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands
    
    def execute(self):
        results = []
        for command in self.commands:
            results.append(command.execute())
        return "\n".join(results)
    
    def undo(self):
        results = []
        for command in reversed(self.commands):
            results.append(command.undo())
        return "\n".join(results)


# Text Editor Example
class TextEditor:
    def __init__(self):
        self.text = ""
    
    def write(self, text):
        self.text += text
    
    def delete(self, length):
        self.text = self.text[:-length]
    
    def get_text(self):
        return self.text


class WriteCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text
    
    def execute(self):
        self.editor.write(self.text)
        return f"Written: '{self.text}'"
    
    def undo(self):
        self.editor.delete(len(self.text))
        return f"Undone: '{self.text}'"


class EditorHistory:
    def __init__(self):
        self.history = []
    
    def push(self, command):
        command.execute()
        self.history.append(command)
    
    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            return "Undo completed"
        return "Nothing to undo"


if __name__ == "__main__":
    # Smart Home Example
    print("=== Smart Home Remote Control ===")
    
    # Create receivers
    living_room_light = Light("Living Room")
    bedroom_light = Light("Bedroom")
    tv = Television()
    
    # Create commands
    living_room_on = LightOnCommand(living_room_light)
    living_room_off = LightOffCommand(living_room_light)
    bedroom_on = LightOnCommand(bedroom_light)
    tv_on = TVOnCommand(tv)
    tv_volume_up = TVVolumeUpCommand(tv)
    
    # Create remote
    remote = RemoteControl()
    remote.set_command(1, living_room_on)
    remote.set_command(2, living_room_off)
    remote.set_command(3, bedroom_on)
    remote.set_command(4, tv_on)
    remote.set_command(5, tv_volume_up)
    
    # Test commands
    print(remote.press_button(1))
    print(remote.press_button(4))
    print(remote.press_button(5))
    print(remote.press_button(5))
    print("\nUndo:")
    print(remote.press_undo())
    print(remote.press_undo())
    
    # Macro Command
    print("\n=== Macro Command (Party Mode) ===")
    party_mode = MacroCommand([
        living_room_on,
        bedroom_on,
        tv_on
    ])
    remote.set_command(9, party_mode)
    print(remote.press_button(9))
    print("\nUndo Party Mode:")
    print(remote.press_undo())
    
    # Text Editor Example
    print("\n=== Text Editor with Undo ===")
    editor = TextEditor()
    history = EditorHistory()
    
    history.push(WriteCommand(editor, "Hello "))
    history.push(WriteCommand(editor, "World"))
    print(f"Text: '{editor.get_text()}'")
    
    print(history.undo())
    print(f"Text: '{editor.get_text()}'")
    
    history.push(WriteCommand(editor, "Python!"))
    print(f"Text: '{editor.get_text()}'")
