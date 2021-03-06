from typing import Callable, Any, TYPE_CHECKING

from events.event_storage import EventStorage

if TYPE_CHECKING:
	from events.event_arguments import EventArguments


class PropertyStorage:

	def __init__(self) -> None:
		self.observers = EventStorage()
		self.value = None

	def dispatch(self, sender: Any, event_args: "EventArguments"):
		self.observers.dispatch(sender, event_args)

	def add_callback(self, callback: Callable):
		self.observers.add_callback(callback)

	def remove_callback(self, callback: Callable):
		self.observers.remove_callback(callback)
