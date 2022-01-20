'''
 Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green' , 'yellow' , or 'red' .
• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.
'''

alien_color = 'green'
points = 0

if alien_color == 'green':
    print('The color of the alien is green!')
    points = points + 5
else:
    print(f'The color of the alien is not green. The color is {alien_color}')

print(f'Your points: {points}')
