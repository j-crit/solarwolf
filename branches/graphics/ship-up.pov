
#declare XMAX=1.2;
#declare XMIN=-XMAX;
#declare YMAX=1.2;
#declare YMIN=-YMAX;

#include "camera-ortho.inc"
#include "lights.inc"
#include "ship.inc"

object {
	Ship
	rotate -40 * x
}