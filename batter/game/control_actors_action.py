from game.action import Action
from game import constants
class ControlActorsAction(Action):
    
    def __init__(self, input_service) -> None:
        super().__init__()
        self._input_service = input_service

    def execute(self, cast):
        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0]
        paddle.set_velocity(direction.scale(constants.PADDLE_SPEED))