import random
from game.control_actors_action import ControlActorsAction
from game.paddle import Paddle
from game.handle_off_screen_action import HandleOffScreenAction
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actor_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["bricks"] = []
    # TODO: Create bricks here and add them to the list
    for y in range(10, 250, 30):
        for x in range(10, 800, 57):
            brick = Brick()
            position = Point(x, y)
            brick.set_position(position)
            brick.set_width(constants.BRICK_WIDTH)
            brick.set_height(constants.BRICK_HEIGHT)
            brick.set_image(constants.IMAGE_BRICK)
            cast["bricks"].append(brick)


    cast["balls"] = []
    # TODO: Create a ball here and add it to the list
    ball = Ball()
    position = Point(0, 300)
    ball.set_position(position)
    ball.set_image(constants.IMAGE_BALL)
    ball.set_width(constants.BALL_WIDTH)
    ball.set_height(constants.BALL_HEIGHT)
    velocity = Point(10, 10)
    ball.set_velocity(velocity)
    cast["balls"].append(ball)

    cast["paddle"] = []
    # TODO: Create a paddle here and add it to the list
    paddle = Paddle()
    position = Point(400, 550)
    paddle.set_position(position)
    velocity = Point(0, 0)
    paddle.set_velocity(velocity)
    paddle.set_image(constants.IMAGE_PADDLE)
    paddle.set_width(constants.PADDLE_WIDTH)
    paddle.set_height(constants.PADDLE_HEIGHT)
    cast["paddle"].append(paddle)


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)

    draw_actors_action = DrawActorsAction(output_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [handle_off_screen_action, move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()