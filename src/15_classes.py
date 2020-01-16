# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
# YOUR CODE HERE


class LatLon:
    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.lon = longitude


x = LatLon(43, 122)
print('x : ', x.lat, x.lon)


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon`
# to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, latitude, longitude):
        super().__init__(latitude, longitude)
        self.name = name

    def __str__(self):
        return self.name


saved_point = Waypoint("unknown", 41, 33)
print('saved_point: ', saved_point.lat, saved_point.lon)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, latitude, longitude):
        super().__init__(name, latitude, longitude)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return self.name


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE
new_waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print('new_waypoint: ', new_waypoint.name, new_waypoint.lat, new_waypoint.lon)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(new_waypoint)


# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
# YOUR CODE HERE
new_geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print('new_geocache: ', new_geocache.difficulty)


# Print it--also make this print more nicely
print(new_geocache)
