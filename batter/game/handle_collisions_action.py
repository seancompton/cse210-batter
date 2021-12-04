from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    def __init__(self, physics_service) -> None:
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]

        if self._physics_service.is_collision(ball, paddle):
            velocity = ball.get_velocity()
            dx = velocity.get_x()
            dy = velocity.get_y()
            dy = dy * -1
            velocity = Point(dx, dy)
            ball.set_velocity(velocity)
        x = 0
        remove_bricks = []
        for brick in bricks:
            x = x + 1
            if self._physics_service.is_collision(ball, brick):
                velocity = ball.get_velocity()
                dx = velocity.get_x()
                dy = velocity.get_y()
                dy = dy * -1
                velocity = Point(dx, dy)
                ball.set_velocity(velocity)
                remove_bricks.append(x)

        for i in remove_bricks:
            bricks.pop(i - 1)
            