from typing import Union

from core.math.geometry.collision_detection.line_ellipse.line_ellipse_collision_detection import \
	(get_inter_data_segment_circle, get_inter_data_segment_ellipse)
from core.math.geometry.geometry_objects import Segment


def get_distance_circle_circle(first_circle: "Circle", second_circle: "Circle") -> float:
	distance_center = (second_circle.center - first_circle.center).get_magnitude()
	distance = distance_center - (first_circle.radius + second_circle.radius)

	return distance


def get_distance_circle_ellipse(circle: "Circle", ellipse: "Ellipse") -> float:
	return get_inter_ellipse_ellipse(circle, ellipse, get_inter_data_segment_circle,
	                                 get_inter_data_segment_ellipse)


def get_distance_ellipse_circle(ellipse: "Ellipse", circle: "Circle") -> float:
	return get_inter_ellipse_ellipse(circle, ellipse, get_inter_data_segment_circle,
	                                 get_inter_data_segment_ellipse)


def get_distance_ellipse_ellipse(first_ellipse: "Ellipse", second_ellipse: "Ellipse") -> float:
	return get_inter_ellipse_ellipse(first_ellipse, second_ellipse, get_inter_data_segment_ellipse,
	                                 get_inter_data_segment_ellipse)


def get_inter_ellipse_ellipse(first_shape: Union["Circle", "Ellipse"],
                              second_shape: Union["Circle", "Ellipse"], segment_first_inter_func,
                              segment_second_inter_func) -> float:
	segment_through_centers = Segment(first_shape.center, second_shape.center)

	circle_inter_data = segment_first_inter_func(segment_through_centers, first_shape)
	ellipse_inter_data = segment_second_inter_func(segment_through_centers, second_shape)

	circle_inter_point = circle_inter_data.intersection_points[0]
	ellipse_inter_point = ellipse_inter_data.intersection_points[0]

	distance_to_circle_inter_point = (circle_inter_point - first_shape.center).get_magnitude()
	distance_to_ellipse_inter_point = (ellipse_inter_point - second_shape.center).get_magnitude()

	distance_between = (ellipse_inter_point - circle_inter_point).get_magnitude()

	# If an ellipse and a circle intersect with each other than segment-ellipse intersection point should lay
	# closer or at the same place as segment-circle intersection point
	if distance_to_ellipse_inter_point > distance_to_circle_inter_point:
		return distance_between

	return -distance_between
