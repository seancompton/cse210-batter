from game.action import Action
from game.point import Point

class HandleOffScreenAction(Action):

    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        actors = cast["balls"]
        for actor in actors:
            position = actor.get_position()
            velocity = actor.get_velocity()
            dx = velocity.get_x()
            dy = velocity.get_y()
            x = position.get_x()
            y = position.get_y()

            if x == 0 or x == 800:
                dx = dx * -1
                
            elif y == 0 or y == 600:
                dy = dy * -1

            velocity = Point(dx, dy)
            actor.set_velocity(velocity)
            
            