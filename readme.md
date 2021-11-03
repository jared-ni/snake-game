# Project 2: Snek

## First, some more set up...
### Git Upstream
If you look in your local folder (repository), there is no `snek` folder! To get the latest code, you need to set up an `upstream` branch and `pull` from it.

In your terminal, type the following:
```
git remote add upstream https://github.com/crimtech/crimtech-comp-f21
git pull upstream master
git push origin master
```

The second line updates your local repository with the latest version of the original repo you forked from, and the third line pushes these changes to your own Github repository. If you get any merge conflicts, you need to edit the files where the conflict occurs, following git's instructions. Afterwards, run `git commit` to fix the merge conflict.

### `pip3 install pygame`
Please run `pip3 install pygame` to install the necessary module using pip.


## Acclimating to the Code
Run `cp snake_starter_code.py snake.py` to make a copy of the game, and run `python3 snake.py`. You should see a board with a red and black dot. The two blue dots represent the snake, and the red dot is the apple.

The board has 24 squares. The top-left square has location `(0,0)`, and the bottom-right square has location `(23,23)`.

We have two classes within `snake.py`: a `Snake` class and an `Apple` class. Then, we have a loop inside `main` that runs this game. You will see that there are many comments with `TODO` written on them. We will be implementing them in the next sections.

The snake's head body is represented by the `body` variable, which is a list containing the body from the head to the tail. So, `self.body[0]` would be referencing the head, and `self.body[:-1]` would reference everything except the tail.

### The `main` function
Here is what you need to understand about the main function:

We have two objects, `snake` and `apple`, which store the state of the snake and the apple. The `while True` loop is run 10 times a second, because of the `clock.tick(10)`.

During every loop, we perform the following actions:
* Check if there was any keypress
* Move the snake.
* Draw the new snake and the new apple, then update the display.
* Check if the snake is dead, and if so exit the game.

The best time to check whether the snake ate an apple, as done in section 5, is after the snake has just moved.

## Required Features
1. Move the snake!
Let's get the snake moving! Change the `move` function so that it will move the snake 1 unit in the correct direction.

Tips: Use the dictionary `DIR` and `self.direction` to figure out which way to move the snake. Change `self.direction` to make sure that the snake moves correctly in all directions.

2. Check for collision.
Now that the snake is moving, it will go off the screen into the vast void of sadness. That's not good! Change the `collision` function to return True if the snake is out of bounds. Change `move` to call the `kill` function when the snake goes out of bounds.

3. Turning the snake.
We need to be able to turn the snake. Modify the `turn` function so that after the function is called, `self.direction` is set to the new direction.

4. Self Collisions.
But, the snake can collide with itself! Change the `collision` function so that it returns `True` if the snake's head has hit another part of its body.

Tip: You may need to make the snake longer and slow down time (decrease the tick_time variable) to test this.

5. Eating the apple.
Detect when the snake is eating the apple. Right now, have the program print out "the snake at an apple!" when that occurs. In the next two parts, we will implement what happens when the snake moves the apple.

6. Moving the apple.
When the snake ate an apple, we need to move it! Move it to a location that is not on the snake.

7. Growing the snake.
The snake needs to grow! Change `move` so that the snake will grow in length once it eats an apple.

8. Display the score.
Display the score of the player. You will need to search up on Google how to display pygame text on screen.

## Optional Features
You need to implement *two* of the features below. Document which two features by inserting the following code block above where you made the change:
```
    # Implements feature #9
    <your code>
```

9. Incremental difficulty

    Right now the difficulty of the game is constant. However, we should challenge the player more as their snake gets longer. Change your code so that the snake moves faster as it gets longer, but maintain a good difficulty curve -- people don't like impossible games.

10. Wait for user input

    Right now the snake starts immediately as we open the game. Change your code so that the snake only starts moving when the user presses a key.

11. Try again!

    Change your code so that the game starts again once the snake dies.

12. Color themes
    
    Implement different color themes. For example, there may be a spaceship theme and you can access it by typing `python3 snake.py spaceship`. You may need to import the `sys` package.

13. Better Graphics
    
    For the artistically inclined, make a better looking snake than a bunch of differently colored squares.

14. Coyote Time
    
    Coyote time is a feature in many platformers that improve the game feel: see, for example, [here](https://www.youtube.com/watch?v=97_jvSPoRDo). In short, we hate when we pressed turn 0.01 second late and the game says we died. So, when the snake is about to die, give a 0.05-0.1 second leeway for the user to press another key.

    You will need to change your `move` and `coyote_time` function.s

    Tip: Start debugging by setting the coyote time amount to be much higher than 0.1 second.

## Submit!
```
git add -A
git commit -m "Submit Snek Project"
git push
```

Finally, make a pull request so we know you're finished!