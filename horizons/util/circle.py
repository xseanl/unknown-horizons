# ###################################################
# Copyright (C) 2009 The Unknown Horizons Team
# team@unknown-horizons.org
# This file is part of Unknown Horizons.
#
# Unknown Horizons is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# ###################################################


from point import Point

class Circle(object):
	"""Class for the shape of a circle
	You can access center and radius of the circle as public members."""
	def __init__(self, center, radius):
		assert isinstance(center, Point)
		self.center = center
		self.radius = radius

	def get_coordinates(self):
		"""Returns all coordinates, that are in the circle"""
		coords = []
		for i in self.tupel_iter():
			coords.append(i)
		return coords

	def contains(self, point):
		assert isinstance(point, Point)
		if point.distance_to_point(self.center) <= self.radius:
			return True
		else:
			return False

	def __str__(self):
		return "Circle(center=%s,radius=%s)" % (self.center, self.radius)

	def __eq__(self, other):
		try:
			if self.center == other.center and \
				 self.radius == other.radius:
				return True
			else:
				return False
		except AttributeError:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def __iter__(self):
		"""Iterates through all coords in circle as Point"""
		for x in range(self.center.x-self.radius, self.center.x+self.radius+1):
			for y in range(self.center.y-self.radius, self.center.y+self.radius+1):
				if self.center.distance_to_tuple((x, y)) <= self.radius:
					yield Point(x, y)

	def tupel_iter(self):
		"""Iterates through all coords in circle as tuple"""
		for x in range(self.center.x-self.radius, self.center.x+self.radius+1):
			for y in range(self.center.y-self.radius, self.center.y+self.radius+1):
				if self.center.distance_to_tuple((x, y)) <= self.radius:
					yield (x, y)




from encoder import register_classes
register_classes(Circle)
