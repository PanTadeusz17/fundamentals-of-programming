###
# A program to calculate the volume and surface area of ​​a cube.
# 
cube_edge_string = input('Enter cube edge lenght: ')
cube_edge = int(cube_edge_string)
cube_volume = cube_edge**3
cube_surface_area = (cube_edge**2) * 6
print(f'The volume of a cube with side {cube_edge} is {cube_volume}')
print(f'The surface area of a cube with side {cube_edge} is {cube_surface_area}')