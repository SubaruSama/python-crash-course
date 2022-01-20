'''
Choose a color for an alien as you did in Exercise 5-3, and
write an if - else chain.

• If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block
'''

alien_color = 'green'
points = 0

if alien_color == 'green':
    print('You just earned 5 points!')
    points = points + 5
else:
    print('The color of alien isn\'t green. You just earned 10 points!')
    points = points + 10
