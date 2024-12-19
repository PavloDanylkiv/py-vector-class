from __future__ import annotations
from math import sqrt, acos, degrees, sin, cos, radians


class Vector:
    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x + other.x,
            y_coordinate=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x - other.x,
            y_coordinate=self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            mul_obj_x = self.x * other.x
            mul_obj_y = self.y * other.y
            return mul_obj_x + mul_obj_y
        elif isinstance(other, (int, float)):
            mul_int_x = self.x * other
            mul_int_y = self.y * other
            return Vector(x_coordinate=mul_int_x, y_coordinate=mul_int_y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        result = ((end_point[0] - start_point[0]), end_point[1]
                  - start_point[1])
        return cls(
            x_coordinate=result[0],
            y_coordinate=result[1]
        )

    def get_length(self) -> int | float:
        return sqrt((self.x ** 2) + self.y ** 2)

    def get_normalized(self) -> Vector:
        result_x = self.x / self.get_length()
        result_y = self.y / self.get_length()
        return Vector(
            x_coordinate=result_x,
            y_coordinate=result_y
        )

    def angle_between(self, other: Vector) -> int:
        result = ((self.x * other.x + self.y * other.y)
                  / (sqrt(self.x ** 2 + self.y ** 2)
                     * (sqrt(other.x ** 2 + other.y ** 2))))
        return round(degrees(acos(result)))

    def get_angle(self) -> int:
        length = self.get_length()
        angle = degrees(acos(self.y / length))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            x_coordinate=self.x * cos(radians(degrees)) - self.y
                                * sin(radians(degrees)),
            y_coordinate=self.x * sin(radians(degrees)) + self.y
                                * cos(radians(degrees))
        )
