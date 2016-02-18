from sys import argv
import time
script, filename = argv
def advent_of_code_intro(project_num):
    print ""
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ---------------------------- Welcome to ----------------------------------'
    time.sleep(.1)
    print '  -------------------------- Advent of Code --------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ------------------ Created by: David Daly 2016 VA ------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ------- This project was done as part the adventofcode.com coding --------'
    time.sleep(.1)
    print '  ------- challenges. This is project %s. Each project has two parts. -------' % project_num
    time.sleep(.1)
    print '  ------- This program completes both parts. -------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  -------- You can find me on Github at github.com/ddjr --------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    print ""
    time.sleep(.8)
def open_file(filename):
    txt = open(filename)
    print "Openning file named: %r " % filename
    return txt.read()
def update_current_location(move,current_location):
    if move == "^":
        current_location[1] += 1
    elif move == "v":
        current_location[1] -= 1
    elif move == ">":
        current_location[0] += 1
    elif move == "<":
        current_location[0] -= 1
    return current_location
def add_item_if_not_in_list(item, _list):
    for l in _list:
        if l == item:
            return _list
    _list.append(item[:])
    return _list
def calculate_travel(move,current_location,houses_hit):
    current_location = update_current_location(move,current_location)
    return add_item_if_not_in_list(current_location, houses_hit)
def year_one_travel(travel_path): # santa only
    current_location = [0,0]
    houses_hit = [[0,0]]
    for move in travel_path:
        houses_hit = calculate_travel(move,current_location,houses_hit)
    print "santa hit %d houses in year one" % len(houses_hit)
def year_two_travel(travel_path): # santa and robo-santa
    robosantas_current_location = [0,0]
    santas_current_location = [0,0]
    houses_hit = [[0,0]]
    move_santa = True
    for move in travel_path:
        if move_santa:
            houses_hit = calculate_travel(move,santas_current_location,houses_hit)
            move_santa = False
        else:
            houses_hit = calculate_travel(move,robosantas_current_location,houses_hit)
            move_santa = True
    print "santa and robo-santa hit %d houses in year two" % len(houses_hit)

advent_of_code_intro(3)
travel_path = open_file(filename)
year_one_travel(travel_path)
year_two_travel(travel_path)
