"""
This program takes the side length of two codes from a user and returns the volume of each cube 
"""
def main():
    side1 = int(input('enter then length of one side of your first cube'))
    side2 = int(input('enter the length of one side of your second cube'))
    result1 = cubeVolume(side1)
    result2 = cubeVolume(side2)
    print('A cube with side length',side1,'has a volume',result1)
    print('A cube with side length',side2,'has a volume',result2)
def cubeVolume(sidelength):
    volume = sidelength **3
    return volume
main()
